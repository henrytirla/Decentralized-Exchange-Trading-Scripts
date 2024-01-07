"MONITORING MULTIPLE ACCOUNTS CONCURRENTLY ON SOLANA"

import asyncio
import websockets
import json

wallet_addresses = ["Address1", "Address2", "Address3", "Address4", "Address5"]
seen_signatures = set()

async def run(wallet_address: str):
 count = 0
 uri = "wss://api.mainnet-beta.solana.com"
 async with websockets.connect(uri) as websocket:
    await websocket.send(json.dumps({
        "jsonrpc": "2.0",
        "id": 1,
        "method": "logsSubscribe",
        "params": [
            {"mentions": [wallet_address]},
            {"commitment": "finalized"}
        ]
    }))

    first_resp = await websocket.recv()
    print(first_resp)
    response_dict = json.loads(first_resp)
    if 'result' in response_dict:
       print("Subscription successful. Subscription ID: ", response_dict['result'])

    async for response in websocket:
        response_dict = json.loads(response)
        if response_dict['params']['result']['value']['err'] == None:
           signature = response_dict['params']['result']['value']['signature']
           if signature not in seen_signatures:
              seen_signatures.add(signature)
              count += 1
              print(f"{count}-{wallet_address}New update received: , {signature}")
              print("=========================================")

tasks = [run(addr) for addr in wallet_addresses]

async def main():
   await asyncio.gather(*tasks)

asyncio.run(main())
