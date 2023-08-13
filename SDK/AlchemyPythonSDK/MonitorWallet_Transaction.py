import asyncio
import json
import websockets
from web3 import Web3
import requests
from websockets import connect


from alchemy import Alchemy, Network
"""
for reference Subscription Type	Description
alchemy_minedTransactions	Emits full transaction objects or hashes that are mined on the network based on provided filters and block tags.
alchemy_pendingTransactions	Emits full transaction objects or hashes that are sent to the network, marked as "pending", based on provided filters.
newPendingTransactions	Emits transaction hashes that are sent to the network and marked as "pending".
newHeads	Emits new blocks that are added to the blockchain.
logs	Emits logs attached to a new block that match certain topic filters.

"""

api_key = "Enter your Alcheny API KEY HERE"
network = Network.ETH_MAINNET
# choose the maximum number of retries to perform, default is 5
max_retries = 3

url = f"https://eth-mainnet.g.alchemy.com/v2/{api_key}"
alchemy_ws_url="wss://eth-mainnet.g.alchemy.com/v2/WoUWFd2SYi7sNbmTTaT_fWMPCOUZ8yDI"


account = '0xbd2C6a28a156377bD75C363aD8f849c68922b4Dc'


alchemy= Alchemy(api_key,network)
mainet_wss="wss://eth-mainnet.g.alchemy.com/v2/WoUWFd2SYi7sNbmTTaT_fWMPCOUZ8yDI"
async def subscribe_to_pending_transactions():
    ws_url = alchemy_ws_url
    subscription_data = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "eth_subscribe",
        "params": ["alchemy_pendingTransactions", {
            "fromAddress":"0xbd2C6a28a156377bD75C363aD8f849c68922b4Dc" #The address you want to monitor be it from or to
            # "toAddress": "0x3fC91A3afd70395Cd496C647d5a6CC9D4B2b7FAD"
        }]
    }

    async with websockets.connect(ws_url) as websocket:
        await websocket.send(json.dumps(subscription_data))

        while True:
            response = await websocket.recv()
            response_data = json.loads(response)
            if "params" in response_data and "result" in response_data["params"]:
                #transaction_data = response_data["params"]['result']['from']
                transaction_data = response_data["params"]
                print(transaction_data)


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(subscribe_to_pending_transactions())

