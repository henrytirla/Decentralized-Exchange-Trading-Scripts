import asyncio
import websockets
import json

wallet_address = "GHZuLHwS4w7hqF232H8Qg8k4CAUg7Zvr49VdYw3K6mtc"
seen_signatures = set()

async def run():
   count = 0
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
              # print(response)
              response_dict = json.loads(response)
             
              if response_dict['params']['result']['value']['err'] == None:

                  signature = response_dict['params']['result']['value']['signature']
                  if signature not in seen_signatures:
                      seen_signatures.add(signature)
                      count += 1
                      print(f"{count}-New update received: , {signature}")
                      print("=========================================")
                
              else:
                  # print("Unexpected response: ", response_dict)
                  pass

asyncio.run(run())
