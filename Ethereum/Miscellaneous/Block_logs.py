
from web3 import Web3
w3 = Web3(Web3.HTTPProvider("https://eth-mainnet.g.alchemy.com/v2/lTlatSTYDZmCv6wVLRIDff7S3kZhL2dq"))




block = w3.eth.get_block(17828184)


block_number = 17828184  # Replace this with the block number you want to fetch


for transaction_hash in block['transactions']:
    transaction = w3.eth.get_transaction(transaction_hash)
    transaction_receipt = w3.eth.get_transaction_receipt(transaction_hash)

    if transaction_receipt and 'logs' in transaction_receipt:
        logs = transaction_receipt['logs']

        for log in logs:
            # Process the log data as needed
            print(f"Transaction Hash: {transaction_hash.hex()}, Log: {log}")