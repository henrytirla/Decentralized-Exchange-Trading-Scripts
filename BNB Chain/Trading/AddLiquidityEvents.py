"Using logs to listen to addingLiquity Events For All tokens on PancakeSwap"

import web3
import time
import datetime

url = "https://bsc-dataseed1.binance.org/"  # Replace with your Ethereum node URL

w3 = web3.Web3(web3.HTTPProvider(url))
def getTimestamp():
    while True:
        timeStampData = datetime.datetime.now()
        currentTimeStamp = "[" + timeStampData.strftime("%H:%M:%S.%f")[:-3] + "]"
        return currentTimeStamp

# Define Topic Filter
topic_filter = [
    "0x4c209b5fc8ad50758f13e2e1088ba56a560dff690a1c6fef26394f4c03821c4f",
    "0x00000000000000000000000010ed43c718714eb63d5aa57b78b54704e256024e"
]
while True:
    # Create an event filter with the specified event signature
    event_filter = w3.eth.filter({'topics': topic_filter})


    # Get changes in the filter to retrieve AddLiquidity events
    add_liquidity_events = w3.eth.get_filter_changes(event_filter.filter_id)


    for event in add_liquidity_events:
        txn_hash = event['transactionHash'].hex()
        txn_receipt= w3.eth.get_transaction(txn_hash)
        input_signature= txn_receipt['input'][:10].hex()
        #Filter with Add Liquidity Function Signature
        if input_signature.startswith('0xf305d719'):
            print("AddLiquidity Event:")
            print("Block Number:", event['blockNumber'])
            print("Transaction Hash:", event['transactionHash'].hex())
            print("Log Index:", event['logIndex'])
            print("Topics:", event['topics'])
            print("Data:", event['data'].hex())
            print("\n")

