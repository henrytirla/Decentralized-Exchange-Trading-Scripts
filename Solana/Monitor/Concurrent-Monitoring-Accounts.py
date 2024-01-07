
# This script is used to monitor buys and sells of  multiple accounts concurrently on Solana.
import asyncio
import websockets
import json
import datetime
from solders.signature import Signature
from solana.rpc.api import Client
from solders.pubkey import Pubkey

solana_client = Client("https://api.mainnet-beta.solana.com")
#Max 5 addresses else you will get error.
wallet_addresses = ["Account Address1", "Account Address","Account Address 3","Account Address 4","Account Address 5"]
seen_signatures = set()
def getTimestamp():
    while True:
        timeStampData = datetime.datetime.now()
        currentTimeStamp = "[" + timeStampData.strftime("%H:%M:%S.%f")[:-3] + "]"
        return currentTimeStamp
class style():
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'
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
    #print(first_resp)
    response_dict = json.loads(first_resp)
    # if 'result' in response_dict:
    #    print("Subscription successful. Subscription ID: ", response_dict['result'])

    async for response in websocket:
        response_dict = json.loads(response)
        if response_dict['params']['result']['value']['err'] == None:
           signature = response_dict['params']['result']['value']['signature']
           if signature not in seen_signatures:
              seen_signatures.add(signature)
              hash = Signature.from_string(signature)
              hash_Detail = solana_client.get_transaction(hash, encoding="json", max_supported_transaction_version=0)
              try:
                  for ui in  hash_Detail.value.transaction.meta.pre_token_balances:

                      if ui.owner == Pubkey.from_string(wallet_address) and ui.mint == Pubkey.from_string("So11111111111111111111111111111111111111112"):
                          pre_amount = ui.ui_token_amount.amount
                      if ui.owner == Pubkey.from_string(wallet_address) and ui.mint != Pubkey.from_string("So11111111111111111111111111111111111111112"):
                          token_address = ui.mint
                  for ui in hash_Detail.value.transaction.meta.post_token_balances:
                      if ui.owner == Pubkey.from_string(wallet_address) and ui.mint == Pubkey.from_string("So11111111111111111111111111111111111111112"):
                          post_amount = ui.ui_token_amount.amount
                      if ui.owner == Pubkey.from_string(wallet_address) and ui.mint != Pubkey.from_string("So11111111111111111111111111111111111111112"):
                          token_address = ui.mint
                  if post_amount > pre_amount:
                      print("**************")
                      count += 1
                      print(f"{count}--{getTimestamp()}Account Address: {wallet_address}, {style.YELLOW}[Token SOLD]:{token_address}{style.RESET} , https://solscan.io/tx/{hash}")
                  else:
                      count+=1

                      print(f"{count}--{getTimestamp()}Account Address: {wallet_address}, {style.GREEN}[Token BOUGHT]:, {token_address}{style.RESET} , https://solscan.io/tx/{hash}")
              except Exception as e:
                  print('Error Occured',e,wallet_address,hash)
                  continue

tasks = [run(addr) for addr in wallet_addresses]

async def main():
   await asyncio.gather(*tasks)

asyncio.run(main())
