from entity.block import Block
from entity.blockchain import Blockchain


def run_test():
    blockchain = Blockchain()

    block1 = Block(index=1, transactions=["yooodleee -> Bob: 10"], previous_hash="")
    blockchain.add_block(block1)

    block2 = Block(index=2, transactions=["Bob -> Charlie: 5"], previous_hash="")
    blockchain.add_block(block2)

    blockchain.print_chain()

    print("\nIs blockchain valid?", blockchain.is_chain_valid())


if __name__ == "__main__":
    run_test()