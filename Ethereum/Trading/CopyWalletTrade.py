# Test on testnet

import asyncio
from web3 import Web3
import json
import requests

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


"""
Scenario Explanation
I want to copy a wallet trades this wallet can interact with different router's depending on the 
Dex Exchange used Assuming trades are done via a dex and not via a smart contract

I scan the memepool for transaction involving that wallet
If trade traced in the memepool is a Buy based on the swap function used
I will proceed to make a buy too


"""

#Goerli Testnet RPC
#w3 = Web3(Web3.HTTPProvider("https://eth-goerli.g.alchemy.com/v2/demo"))
w3 = Web3(Web3.HTTPProvider("https://eth-mainnet.g.alchemy.com/v2/lTlatSTYDZmCv6wVLRIDff7S3kZhL2dq"))


#TODO  ADD -Aggregation Router 0x1111111254EEB25477B68fb85Ed929f73A960582

#This list is to check for all interaction of target wallets with any of these routers
uniswap_router_addresses = [
    '0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D',  #Uniswap-V2 Router
    '0xE592427A0AEce92De3Edee1F18E0157C05861564',  #Uniswap-V3 Router
    '0x68b3465833fb72A70ecDF485E0e4C7bD8665Fc45',  #Uniswap-V3 02 Router
    '0xEf1c6E67703c7BD7107eed8303Fbe6EC2554BF6B', #OldUniversal-Router
    '0x3fC91A3afd70395Cd496C647d5a6CC9D4B2b7FAD', #Universal-Router

]

if w3.is_connected():
    #print(style.GREEN+"Connected To Goerli Testnet")
    print(style.GREEN + "Connected To Mainnet Testnet")

# print(w3.eth.get_block('latest'))

check_Buy_functions = {"swapETHForExactTokens": True, "swapExactETHForTokens": True,
                   "swapExactETHForTokensSupportingFeeOnTransferTokens": True,
                   'multicall': True, 'execute': True}

#Here is the wallet Address I wish to copy
Target_WalletAddress= "0xb6007a21D1c890742bd9a3A4E2C0CA8Df646b0Be"



count= 0
async def handle_new_block(block):
    global count
    for tx_hash in block['transactions']:
        try:
            tx = w3.eth.get_transaction(tx_hash)


            for router_address in uniswap_router_addresses:

                if tx['from'] == Target_WalletAddress and tx['to'] == router_address:
                    hash= tx['hash']
                    tx_hash = w3.to_hex(hash)
                    # function_name = decode_input_data(tx['input'], tx['to'])
                    # if function_name is not None:
                    #     count += 1



                    count+=1
                    print(count,style.YELLOW + "Tx_Hash: ",
                              "https://etherscan.io/tx/"+w3.to_hex(hash))

                    # print(style.GREEN+f"{function_name}")
                    print(style.RED+"------------------")
                    #break
                else:

                    continue

        except Exception as e:
            print("An error occurred while processing a transaction:", e,w3.to_hex(tx_hash))

async def track_new_blocks():
    current_block_number =  w3.eth.block_number


    while True:
        latest_block = w3.eth.get_block('latest')
        latest_block_number = latest_block['number']

        if latest_block_number > current_block_number:
            for block_number in range(current_block_number + 1, latest_block_number + 1):
                block =  w3.eth.get_block(block_number)
                await handle_new_block(block)

            current_block_number = latest_block_number

        # Delay between checking for new blocks
        await asyncio.sleep(5)

# Run the event loop
async def main():
    await track_new_blocks()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())