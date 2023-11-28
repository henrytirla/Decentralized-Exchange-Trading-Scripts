"Irrespective of routers used copy trade list of wallets---BUYS AND SELL-----*******"


"""-----ADD YOUR WALLETS ON LINE 65 -----"""

import asyncio
import json
import websockets
from web3 import Web3
import requests
from alchemy import Alchemy, Network
import datetime



class style():  # Class of different text colours - default is white
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



api_key = "Enter Your Alchemy API KEY"
network = Network.ETH_MAINNET
alchemy_ws_url="wss://eth-mainnet.g.alchemy.com/v2/"+api_key
alchemy= Alchemy(api_key,network)
WETH="0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2"
provider_url = "wss://eth-mainnet.g.alchemy.com/v2/"+api_key






def getTimestamp():
    while True:
        timeStampData = datetime.datetime.now()
        currentTimeStamp = "[" + timeStampData.strftime("%H:%M:%S.%f")[:-3] + "]"
        return currentTimeStamp


def format_hex(original_hex):
    hex_without_prefix = original_hex[2:]

    desired_length = 64

    padded_hex = hex_without_prefix.zfill(desired_length)

    final_hex = "0x" + padded_hex

    return final_hex.lower()



queue = asyncio.Queue()

# Enter List of Address you wish to Copy Trade as below seperated by commas eg "Address1","Address2","Address3 NB Delete this Two in the list "
addresses = ["0xae2Fc483527B8EF99EB5D9B44875F005ba1FaE13","0x6b75d8AF000000e20B7a7DDf000Ba900b4009A80"]

monitored_wallets_hex = [format_hex(address) for address in addresses]
async def process_transaction(transaction_hash):
    try:
        receipt = alchemy.core.get_transaction_receipt(transaction_hash)
        transfer_details = alchemy.core.get_transaction(transaction_hash)
        from_address=transfer_details['from']
        eth_value=alchemy.from_wei(transfer_details['value'], 'ether')
        txn_hash= alchemy.to_hex( transfer_details['hash'])
        block_num= transfer_details['blockNumber']

        print("=======================")

        if receipt['status'] == 1:
           for logs in receipt['logs']:
               if logs['address'] != WETH:
                  if alchemy.to_hex(logs['topics'][0]) == "0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef":
                      if alchemy.to_hex(logs['topics'][2]) in monitored_wallets_hex:
                          print(f" {getTimestamp()} {block_num} {style.GREEN} TOKEN BOUGHT {logs['address']} {style.RESET} {style.MAGENTA} {from_address}      {style.RESET} for {eth_value} ETH  TxnHash: https://etherscan.io/tx/{txn_hash}", style.RESET)
                          print(style.CYAN+"====COPY TRADING BUY TRADE SIMULATION======",style.RESET)

                      elif alchemy.to_hex(logs['topics'][1]) in monitored_wallets_hex:
                          print(f" {getTimestamp()} {block_num} {style.YELLOW}TOKEN SOLD {logs['address']}  {style.RESET}  {style.MAGENTA} {from_address}      {style.RESET} TxnHash:  https://etherscan.io/tx/{txn_hash} ", style.RESET)
                          print(style.MAGENTA+"====COPY TRADING TRADE SALE SIMULATION=====",style.RESET)
                      elif alchemy.to_hex(logs['topics'][0]) == "0x8c5be1e5ebec7d5bd14f71427d1e84f3dd0314c0f7b2291e5b200ac8c7c3b925":
                           if alchemy.to_hex(logs['topics'][1]) in monitored_wallets_hex:
                              print(f"{getTimestamp()} {style.RED}{block_num}{style.RESET} {style.YELLOW} TOKEN APPROVED {logs['address']} {style.RESET} {style.MAGENTA} {from_address} {style.RESET}  TxnHash: https://etherscan.io/tx/{txn_hash}",style.RESET)


           queue.task_done()




    except Exception as e:
        queue.task_done()




async def subscribe_to_pending_transactions():
    print("Connecting to WebSocket...")
    async with websockets.connect(alchemy_ws_url) as websocket:
        print("WebSocket connection established.")
    ws_url = alchemy_ws_url
    subscription_data = {
        "jsonrpc": "2.0",
        "method": "eth_subscribe",
        "params": ["alchemy_minedTransactions",
                   {"addresses": [{"from": address} for address in addresses], "includeRemoved": False,
                    "hashesOnly": True}],
        "id": 1
    }

    async with websockets.connect(ws_url) as websocket:
        await websocket.send(json.dumps(subscription_data))
        while True:
            response = await websocket.recv()
            response_data = json.loads(response)
            if "params" in response_data and "result" in response_data["params"]:
                transaction_hash = response_data["params"]["result"]['transaction']['hash']
                queue.put_nowait(transaction_hash)







async def process_queue():
    print(style.GREEN+"Scanning Transaction.....",style.RESET)
    while True:
        if queue.qsize() <= 3:
            wait_time =3
        else:
            wait_time = 1

        transaction_hash = await queue.get()
        print(getTimestamp(),transaction_hash)
        await asyncio.sleep(wait_time) 
        await process_transaction(transaction_hash)

if __name__ == "__main__":
    asyncio.gather(subscribe_to_pending_transactions(), process_queue())
    asyncio.get_event_loop().run_forever()
