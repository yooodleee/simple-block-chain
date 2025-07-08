from typing import List


class TransactionPool:
    def __init__(self):
        self.transactions: List[str] = []
    
    def add_transaction(self, transaction: str):
        """새로운 트랜잭션을 풀에 추가"""
        self.transactions.append(transaction)
    
    def get_pending_transactions(self) -> List[str]:
        """모든 대기 중인 트랜잭션을 반환 (복사본)"""
        return list(self.transactions)
    
    def clear_transactions(self):
        """트랜잭션 풀 비우기 (블록에 포함되었을 때 호출)"""
        self.transactions.clear()