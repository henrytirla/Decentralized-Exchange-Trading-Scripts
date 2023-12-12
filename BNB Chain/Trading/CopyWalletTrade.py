"""Copy Wallet Trade"""


import asyncio
import json
from web3 import Web3
from websockets import connect
import datetime
import asyncio

"""
Subscribes to pending transactions 
https://community.infura.io/t/web3-py-how-to-subscribe-to-pending-ethereum-transactions-in-python/5409
"""

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


def format_hex(original_hex):
    hex_without_prefix = original_hex[2:]

    desired_length = 64

    padded_hex = hex_without_prefix.zfill(desired_length)

    final_hex = "0x" + padded_hex

    return final_hex.lower()




infura_ws_url="wss://bsc-mainnet.core.chainstack.com/ws/a0f24337b06b05ec7b972078ce65d3ca"
infura_http_url = 'https://bsc-dataseed1.binance.org/'
web3 = Web3(Web3.HTTPProvider(infura_http_url))
WETH="0xbb4CdB9CBd36B01bD1cBaEBF2De08d9173bc095c"


#Enter list of Wallet Addresses to monitor and copyTrade
addresses = ["0x142aAbcc7D567e138384C1Fe637e3868e79eb9EB",
             "0xA80711c35543250191B52d3BDcABA125bceCC483",
             "0x981D4337876D3756d5BccbE2e1f3CF41C4496f7D"]

monitored_wallets_hex = [format_hex(address) for address in addresses]


async def get_event():
    async with connect(infura_ws_url) as ws:
        await ws.send('{"jsonrpc": "2.0", "id": 1, "method": "eth_subscribe", "params": ["newPendingTransactions"]}')
        subscription_response = await ws.recv()
        print(subscription_response)

        while True:
            try:
                message = await asyncio.wait_for(ws.recv(), timeout=15)
                response = json.loads(message)
                txHash = response['params']['result']
                receipt = web3.eth.get_transaction_receipt(txHash)
                # print(receipt)
                transfer_details = web3.eth.get_transaction(txHash)

                from_address = transfer_details['from']

                txn_hash = web3.to_hex(transfer_details['hash'])
                block_num = transfer_details['blockNumber']
                if receipt['status'] == 1:
                    # print(from_address)
                    #
                    # print(f"Transaction Successful,     TxnHash: https://bscscan.com/tx/{txn_hash}")

                    eth_value = None

                    for logs in receipt['logs']:
                        if logs['address'] == WETH and web3.to_hex(logs['topics'][
                                                                          0]) == "0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef":
                            hex_value = web3.to_hex(logs['data'])
                            integer_value = int(hex_value, 16)
                            eth_value = web3.from_wei(integer_value, 'ether')
                            eth_value = '{:.4f}'.format(eth_value)

                    if eth_value is not None:
                        for logs in receipt['logs']:
                            if logs['address'] != WETH:
                                if web3.to_hex(logs['topics'][
                                                      0]) == "0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef":
                                    if web3.to_hex(logs['topics'][2]) in monitored_wallets_hex:
                                        print(
                                            f" {getTimestamp()} {style.RED}{block_num}{style.RESET} {style.GREEN} TOKEN BOUGHT: {logs['address']} {style.RESET} {style.MAGENTA} WALLET_ADDRESS: {from_address}{style.RESET} For {eth_value} BNB",
                                            style.RESET)
                                        print(f"TxnHash:  https://bscscan.com/tx/{txn_hash} ")
                                        print(style.CYAN + "====BUYING TRADE SIMULATION======", style.RESET)
                                        # analyze_token(logs['address'])

                                elif web3.to_hex(logs['topics'][1]) in monitored_wallets_hex:
                                    print(
                                        f" {getTimestamp()} {style.RED}{block_num}{style.RESET} {style.YELLOW}TOKEN SOLD: {logs['address']}  {style.RESET}  {style.MAGENTA} WALLET_ADDRESS: {from_address}{style.RESET} For {eth_value} BNB",
                                        style.RESET)
                                    print(f"TxnHash:  https://bscscan.com/tx/{txn_hash} ")
                                    print(style.MAGENTA + "====SELLING TRADE SALE SIMULATION=====", style.RESET)
                    elif logs['address'] != WETH:
                        if web3.to_hex(
                                logs['topics'][
                                    0]) == "0x8c5be1e5ebec7d5bd14f71427d1e84f3dd0314c0f7b2291e5b200ac8c7c3b925":
                            if web3.to_hex(logs['topics'][1]) in monitored_wallets_hex:
                                print(
                                    f"{getTimestamp()} {style.RED}{block_num}{style.RESET}{style.MAGENTA} TOKEN APPROVED: {logs['address']}{style.RESET}{style.MAGENTA} WALLET_ADDRESS {from_address}{style.RESET} ",
                                    style.RESET)
                                print(f"TxnHash: https://bscscan.com/tx/{txn_hash}")
                                print(style.MAGENTA + "====APPROVED TRANSACTION=====", style.RESET)
                else:
                    pass
                    # print("Transaction Failed")
                    # print(f"TxnHash: https://bscscan.com/tx/{txn_hash}")
                    # print(style.RED + "====TRANSACTION FAILED=====", style.RESET)
            except Exception as e:
                 pass
                 #print("An error occurred while processing a transaction:", e)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    while True:
        loop.run_until_complete(get_event())