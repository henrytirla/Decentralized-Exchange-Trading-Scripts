

from web3 import Web3
import time

w3 = Web3(Web3.HTTPProvider("https://eth-mainnet.g.alchemy.com/v2/lTlatSTYDZmCv6wVLRIDff7S3kZhL2dq"))

uniswap_contract_address = '0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D'  # Replace with Uniswap contract address

def handle_new_block(block):
    for tx_hash in block['transactions']:

        try:
            tx = w3.eth.getTransaction(tx_hash)

            if tx['to'].lower() == uniswap_contract_address.lower():
                # Process the transaction
                print("Transaction interacting with Uniswap:", w3.toHex(tx['hash']))
                print("Input", tx['input'])
        except Exception as e:
            print("An error occurred while processing a transaction:", e)


def setup_block_filter():
    new_block_filter = w3.eth.filter('latest')

    while True:
        for block_hash in new_block_filter.get_new_entries():
            block = w3.eth.getBlock(block_hash)
            handle_new_block(block)

        # Sleep for a certain interval before checking for new blocks again
        time.sleep(1)

# Set up the block filter
setup_block_filter()