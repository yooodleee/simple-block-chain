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