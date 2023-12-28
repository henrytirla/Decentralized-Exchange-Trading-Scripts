from eth_abi import abi
from web3 import Web3
# ABI for the transferFrom function
transfer_from_abi = ['address', 'address', 'uint256']
web3 = Web3(Web3.HTTPProvider('ENTER YOUR NODEURL'))

txn_hash="0xfdc9939cb6bd71bdec1f86eccd44dc7faa79f98c82dac2ae1910e383971fbe8d"

tx_log = web3.eth.get_transaction_receipt(txn_hash).logs
topics= tx_log[1]['topics'] # 5th log is the swap
#print(topics)
first_topic = web3.to_hex(topics[1])
second_topic =  web3.to_hex(topics[2])
third_topic = web3.to_hex(topics[3])

DATA =   topics[1] + topics[2] + topics[3]
decodedABI = abi.decode(transfer_from_abi, DATA)
print(decodedABI)

