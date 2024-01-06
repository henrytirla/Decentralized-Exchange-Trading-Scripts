"Subscrine to a wallet and monitor the transactions"

#NOTE SOLANA supports only 1 wallet for this subscription

import asyncio
import websockets
import json

wallet_address = "Enter Wallet Transaction"

async def run():
   uri = "wss://api.mainnet-beta.solana.com"
   async with websockets.connect(uri) as websocket:
       # Send subscription request
       await websocket.send(json.dumps({
           "jsonrpc": "2.0",
           "id": 1,
           "method": "logsSubscribe",
           "params": [
               {"mentions": [wallet_address]},
               {"commitment": "finalized"}
           ]
       }))

       # Receive the first response
       first_resp = await websocket.recv()
       print(first_resp)
       response_dict = json.loads(first_resp)
       if 'result' in response_dict:
          print("Subscription successful. Subscription ID: ", response_dict['result'])

       # Continuously read from the WebSocket
       async for response in websocket:
           print(response)
           response_dict = json.loads(response)
           print(response_dict.values.err)
           if 'params' in response_dict:
              print("New update received: ", response_dict['params'])
              print("=========================================")
           else:
              print("Unexpected response: ", response_dict)

asyncio.run(run())