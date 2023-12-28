from web3 import  Web3
from eth_abi import abi
tx_hash = '0xb9ae909908fc911f547845c853422832538ef97ff2c569ac403ecbd252840c6e'
web3 = Web3(Web3.HTTPProvider('Enter your node url'))

txn_log = web3.eth.get_transaction_receipt(tx_hash).logs
topics = txn_log[5]['topics']  # 5th log is the swap log
first_topic = web3.to_hex(topics[1])
second_topic =  web3.to_hex(topics[2])
third_topic = web3.to_hex(txn_log[5]['data'])

# Print the values of topics
# print("First Topic:", first_topic)
# print("Second Topic:", second_topic)
# print("Third Topic:", third_topic)

DATA = topics[1] + topics[2] + txn_log[5]['data']

decodedABI = abi.decode(['address', 'uint256', 'uint256', 'uint256','uint256','address'], DATA)
print(decodedABI)
