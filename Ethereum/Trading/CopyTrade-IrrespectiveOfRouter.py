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
addresses = ["0x0f894fc241C8f211C9a6B6Cd01108D1C878845E4",
             "0x82E00E14288012C9033cDc6ce2AF0fe7b135EDB3",
             "0x66e3e90A4Cf3742c212Cf7c30603cE22F9Fa9c94",
             "0x3A52F0Aeef21b3EF1C92F4Be10e6b0738C829Dba",
             "0xfcDCAC15c9b2A4227A00BF050d31486fA8652FB8",
             "0x7b1184bF2aB8a2F0fB2522C3C8BA726A7ae44c1A",
             "0xFa9BeC18fB25E26320518F90eD63B68CB3A11671",
             "0xe267727A0c8614800A9CA10C1f135dCa094657c9",
             "0x1831322f48dBd8a9323b72d304d6018Cf37dD40E",
             "0x876cD87bF451b1764880fDf14Ee49212AE2a4d0f",
             "0x45107f30fbf5752c5767b1c70b03c41fc0f4b507",
             "0xe6C5e38110d841608DC44096c6673D69EbB681EB",
             "0x2e52c65e3Ffc8E87A13263867E042bf59A9ca6BD",
             "0x7e8D45eec0613731517E3E62e52755634711DbfC",
             "0x9660259A30Bb8ae9Bbcf28241d745b2D581280C1",
             "0x516449F7a5c75238326F6f770567D97F5c3F9b11",
             "0x0Ea06e9d6Be66e3E1fC67685F4797Ff7fc849667",
             "0x2C1433fA8dD5d550b8CEd8dD5C9eC065C124538b",
             "0x4D4368A6eB8262BC7C57aBeA1CB7f8Cf18397440",
             "0x0203458eE55e240140aE61B5DaFAF5605D1E011D",
             "0x0f894fc241C8f211C9a6B6Cd01108D1C878845E4",
             "0x89a976060B464bf41d7632E0C459bdA8Ae211D36",
             "0xb238e7a094E7f4fE6CCC9af2ef24d7c2184621b0",
             "0x609F4Da674397d16BF0422288B5e18b09572e863",
             "0x0Db098Ab5217dbd31aBc417dD71a2a8676398A79",
             "0xbd579c4f7886bfdDA1b5e3459f2FFB77d3741132",
             "0xAC12785Bf910513FD47192A34E23D4533312FB46",
             "0xFdfBeA492bcB16deb4b1390eA1A3c41464806cBE",
             "0x8A2955394DEC47d14AbaE7F506E7D183C37cF39e",
             "0x3fA027c1718AcD863eAaEeC33Ef33fC2377F4c88",
             "0x740De8cC9E916049CC493BEcAf186063d3F14ec5",
             "0xC7B9433D4E856e34F7519AEF92a9f8e9d9759330",
             "0xD1469EdA328e7E9cE63Ad704731C92CD69c475bC",
             "0x006f0537ED493f7F84340dc6c417a8381C6B1035",
             "0xe076A42bf0eFb5259AaE29e71A1F1abEd3206319",
             "0xD2d7cFcD0b4c6DC48a059B0b7Dd5819075C36345",
             "0x81021704a53630963159E14f467304218d86bE43",
             "0xcDA31b98131B059FE6464963F1F474De6e13eB2b",
             "0xb6380198D5D96D9a950714f9eFF9EBF283307180",
             "0x7ce9dA83253aFA7677c18815747a1adB271F92cA",
             "0x2f6fc19d5Da153F9610EBcaBA3E770b94F29f362",
             "0xdC449654E3fB063c0C6932CBF169Fb43fa8e2DD9",
             "0xa98D3AE9312192956be5F98DBdD87963ede57687",
             "0x3ba9692Bc12562eE15DC88B3F3e55339bd51C5b3",
             "0x9Fc5389C66bBfAC23b77bDef85700672928De555",
             "0x8d3B36AB2c9eF588d3472c8de0950796Ac8A2443",
             "0x42fc2073d081bea5Cea3cce9b05507Fb6d3c2a63",
             "0x4F8c93faD9282eA50A8b7e73ed5ef44c8c60BD4d",
             "0x3Ca9eC53D076784dcA3d8BB467e7ff78c29C73c4",
             "0xc03D38F89b175596859C99eaB231d31e1808358c",
             "0xAb819462df33618b383fe402f875260b683F11ac",
             "0xEE06aAc8BAc0d7a3A3B4A8554e8bF4E348a92700",
             "0x9fc4Baf5C37f23C3875c7bE693682EeAe6d632eD",
             "0xF891bF97f1a51D57bD4D2568f94A9f8882162050",
             "0x2d007C5C757cEf2fb53c593242331f50b159a72D",
             "0x6F7a0B2F75be0b106aAD8b355D6b59D93624DCA4",
             "0x7C7A2AD5037701593D76Fad7fb0AB0902366EFA3",
             "0x02Cf562FA7503C4743AE6A38737CFbC227466deE",
             "0x81d882e41D8d0b594aa7636f1303Cb9A5a4B4b2E",
             "0x691598900ceC00B6CBdb32aE821c4f8Fc0C727d4",
             "0xebb8c8e5FBdc556Eedab7757f4E26F79Df8E2269",
             "0xc03D38F89b175596859C99eaB231d31e1808358c",
             "0xbaA56bE07Be167D0eFaFFdEFD08689B77C7524fE"]

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
    print(style.GREEN+"=====Monitoring Targets Wallets To Copy Transaction====== ",style.RESET)
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
