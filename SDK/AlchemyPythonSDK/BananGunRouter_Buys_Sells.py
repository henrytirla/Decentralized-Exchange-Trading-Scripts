import asyncio
import json
import websockets
from alchemy import Alchemy, Network
import datetime
import requests

alchemy_ws_url = "wss://eth-mainnet.g.alchemy.com/v2/BLHi-AZvCt6LjvO8W7nFtloBJFZa393M"
api_key = "BLHi-AZvCt6LjvO8W7nFtloBJFZa393M"
network = Network.ETH_MAINNET
alchemy = Alchemy(api_key, network)
WETH="0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2"

queue = []

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

def getTimestamp():
    while True:
        timeStampData = datetime.datetime.now()
        currentTimeStamp = "[" + timeStampData.strftime("%H:%M:%S.%f")[:-3] + "]"
        return currentTimeStamp
def get_creation_timestamp(contract_address):
    from datetime import datetime
    url = f'https://api.etherscan.io/api?module=account&action=txlist&address={contract_address}&startblock=0&endblock=99999999&page=1&offset=3&sort=asc&apikey=QSD4D9KG1NYTX3Y6CPAR62G9FBW16UZ81Z'
    response = requests.get(url)
    data = response.json()

    if data['status'] == '1':
        for tx in data['result']:
            if tx['to'] == contract_address.lower():
                timestamp = int(tx['timeStamp'])
                formatted_time = datetime.utcfromtimestamp(timestamp).strftime("%d-%m-%Y %H:%M:%S")
                return formatted_time
    else:
        raise Exception('Error while fetching transactions: ' + data['message'])
def calculate_time_difference(creation_time_str):
    from datetime import datetime, timedelta

    creation_time = datetime.strptime(creation_time_str, "%d-%m-%Y %H:%M:%S")
    current_time = datetime.utcnow()
    time_difference = current_time - creation_time

    # Extract days, hours, and minutes from the time difference
    days = time_difference.days
    hours, remainder = divmod(time_difference.seconds, 3600)
    minutes, _ = divmod(remainder, 60)

    return f"{days} days {hours} hours {minutes} minutes ago"

def getTotalBuys(to_address, contract_address):
    category = ["erc20"]
    with_metadata = False
    from_block = "0x0"
    to_block = "latest"
    from_address = None
    result = alchemy.core.get_asset_transfers(category,with_metadata,from_block,to_block,from_address,to_address,[contract_address])
    length= len(result['transfers'])
    token_name= result['transfers'][0].asset
    return length, token_name
def get_Days(creation_time_str):
    from datetime import datetime, timedelta

    creation_time = datetime.strptime(creation_time_str, "%d-%m-%Y %H:%M:%S")
    current_time = datetime.utcnow()
    time_difference = current_time - creation_time

    # Extract days, hours, and minutes from the time difference
    days = time_difference.days
    hours, remainder = divmod(time_difference.seconds, 3600)
    minutes, _ = divmod(remainder, 60)

    return days

async def process_transaction(transaction_hash):
    #await asyncio.sleep(5)  # Simulate some processing time
    print(f"{getTimestamp()} Processing transaction: {transaction_hash}")
    receipt =  alchemy.core.get_transaction_receipt(transaction_hash)
    WalletAddress = receipt['from']
    tokenBought = receipt['logs'][2]['address']
    if receipt['status'] == 1:
        if receipt['logs'][0]['address'] == WETH:

            try:
                numberOfBuys, tokenName = getTotalBuys(WalletAddress, tokenBought)
                creation_time = get_creation_timestamp(tokenBought)
                time_difference_str = calculate_time_difference(creation_time)
                num_days= get_Days(creation_time)
                print(numberOfBuys, tokenName)
                if numberOfBuys ==1 and num_days < 1:
                   print(style.GREEN + f"Buy Detected from {WalletAddress}: # of tokenBought {tokenBought} {style.RED}Creation Time: {time_difference_str} ",style.RESET)
            except Exception as e:
                print("Error",e)





            print("-----------------------")
        else:
            # numberOfBuys, tokenName = getTotalBuys(WalletAddress, tokenBought)
            # Number of Sells {numberOfBuys}
            # print(numberOfBuys,tokenName)
            print(style.MAGENTA + f"This is a sale {WalletAddress}: # of tokenSold {tokenBought}  ",
                  style.RESET)
            print("------------------------")



async def subscribe_to_pending_transactions():
    async with websockets.connect(alchemy_ws_url) as websocket:
        subscription_payload = {
            "jsonrpc": "2.0",
            "method": "eth_subscribe",
            "params": ["alchemy_minedTransactions", {"addresses": [{"to": "0x58dF81bAbDF15276E761808E872a3838CbeCbcf9"}], "includeRemoved": False, "hashesOnly": True}],
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
