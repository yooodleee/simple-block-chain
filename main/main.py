import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from entity.block import Block
from entity.blockchain import Blockchain
from entity.transaction_pool import TransactionPool


def run_test():
    blockchain = Blockchain()
    pool = TransactionPool()

    # 트래잭션 추가
    pool.add_transaction("yooodleee -> Bob: 10")
    pool.add_transaction("Bob -> Charile: 5")

    # 대기 중인 트랜잭션 확인
    pending = pool.get_pending_transactions()

    # 블록 생성 (대기 중인 트랜잭션 포함)
    new_block = Block(index=1, transactions=pending, previous_hash="")
    blockchain.add_block(new_block)

    # 트랜잭션 풀 비우기
    pool.clear_transactions()

    blockchain.print_chain()

    print("\nIs blockchain valid?", blockchain.is_chain_valid())


if __name__ == "__main__":
    run_test()