from typing import List
from entity.block import Block


class Blockchain:
    def __init__(self):
        self.chain: List[Block] = [self.create_genesis_block()]
        self.difficulty: int = 2
    
    def create_genesis_block(self) -> Block:
        return Block(index=0, transactions=["Genesis Block"], previous_hash="0")
    
    def get_latest_block(self) -> Block:
        return self.chain[-1]
    
    def add_block(self, new_block: Block):
        new_block.previous_hash = self.get_latest_block().hash
        new_block.hash = new_block.calculate_hash()

        while not new_block.hash.startswith("0" * self.difficulty):
            new_block.nonce += 1
            new_block.hash = new_block.calculate_hash()
        
        self.chain.append(new_block)
    
    def is_chain_valid(self) -> bool:
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i - 1]

            if current.hash != current.calculate_hash():
                print(f"[!] Invalid hash at block #{i}")
                return False
            if current.previous_hash != previous.hash:
                print(f"[!] Invalid link at block #{i}")
                return False
        return True
    
    def print_chain(self):
        for block in self.chain:
            print(block)