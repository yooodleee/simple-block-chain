import hashlib
import time
from typing import List, Any


class Block:
    def __init__(self, index: int, transactions: List[Any], previous_hash: str, nonce: int = 0):
        self.index = index
        self.timestamp = time.time()
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.nonce = nonce
        self.hash = self.calculate_hash()
    
    def calculate_hash(self):
        block_data = f"{self.index}{self.timestamp}{self.transactions}{self.previous_hash}{self.nonce}"
        return hashlib.sha256(block_data.encode()).hexdigest()
    
    def __repr__(self):
        return (
            f"Block(index={self.index}, hash={self.hash[:10]}..., "
            f"prev_hash={self.previous_hash[:10]}..., transactions={self.transactions})"
        )


class Blockchain:
    def __init__(self):
        self.chain: List[Block] = [self.create_genesis_block()]
        self.difficulty: int = 2 # 앞에 0이 몇 개 나와야 유효한 블록인지
    
    def create_genesis_block(self) -> Block:
        return Block(index=0, transactions=["Genesis Block"], previous_hash="0")
    
    def get_latest_block(self) -> Block:
        return self.chain[-1]
    
    def add_block(self, new_block: Block):
        new_block.previous_hash = self.get_latest_block().hash
        new_block.hash = new_block.calculate_hash()

        # Proof of Work: 해시가 difficulty만큼 0으로 시작할 때까지 nonce 증가
        while not new_block.hash.startswith("0" * self.difficulty):
            new_block.nonce += 1
            new_block.hash = new_block.calculate_hash()
        
        self.chain.append(new_block)
    
    def is_chain_valid(self) -> bool:
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i - 1]

            if current.hash != current.calculate_hash():
                print(f"[!] Block #{i} has invalid previous hash link.")
                return False
        return True
    
    def print_chain(self):
        for block in self.chain:
            print(block)