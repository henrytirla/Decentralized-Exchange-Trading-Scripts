import asyncio
import json
import websockets
from alchemy import Alchemy, Network
import datetime

alchemy_ws_url = "wss://eth-mainnet.g.alchemy.com/v2/BLHi-AZvCt6LjvO8W7nFtloBJFZa393M"
api_key = "Enter your Alchemy API"
network = Network.ETH_GOERLI
alchemy = Alchemy(api_key, network)

queue = []

def getTimestamp():
    while True:
        timeStampData = datetime.datetime.now()
        currentTimeStamp = "[" + timeStampData.strftime("%H:%M:%S.%f")[:-3] + "]"
        return currentTimeStamp


async def process_transaction(transaction_hash):
    await asyncio.sleep(5)  # Simulate some processing time
    print(f"{getTimestamp()} Processing transaction: {transaction_hash}")

async def subscribe_to_pending_transactions():
    async with websockets.connect(alchemy_ws_url) as websocket:
        subscription_payload = {
            "jsonrpc": "2.0",
            "method": "eth_subscribe",
            "params": ["alchemy_minedTransactions", {"addresses": [{"from": "0xae2Fc483527B8EF99EB5D9B44875F005ba1FaE13"}], "includeRemoved": False, "hashesOnly": True}],
            "id": 1
        }

        await websocket.send(json.dumps(subscription_payload))

        while True:
            response = await websocket.recv()
            response_data = json.loads(response)
            #print(response_data)
            if "params" in response_data and "result" in response_data["params"]:
                transaction_hash = response_data["params"]["result"]['transaction']['hash']
                queue.append(transaction_hash)

async def process_queue():
    while True:
        if queue:
            transaction_hash = queue.pop(0)
            await process_transaction(transaction_hash)
        else:
            await asyncio.sleep(1)  # Sleep for a while if queue is empty

async def main():
    subscribe_task = asyncio.create_task(subscribe_to_pending_transactions())
    process_queue_task = asyncio.create_task(process_queue())

    await asyncio.gather(subscribe_task, process_queue_task)

if __name__ == "__main__":
    asyncio.run(main())
