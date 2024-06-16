"Focus on buys immediately after liquitidy is added"
import sys

import requests
import json
from web3 import Web3

web3 = Web3(Web3.HTTPProvider("https://eth-mainnet.g.alchemy.com/v2/YOUR_API_KEY"))



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


api_key = 'QSD4D9KG1NYTX3Y6CPAR62G9FBW16UZ81Z'

# Prompt user to input the token contract address and number of wallets
contract_address = input("Enter the token contract address: ")
num_wallets = int(input("Enter the number of wallets to display: "))


WETH= "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2"

uniswap_factory = '0x5C69bEe701ef814a2B6a3EDD4B1652CB9cc5aA6f'  # Testnet  #0x6725F303b657a9451d8BA641348b6761A6CC7a17
uniswap_factory_abi = json.loads('[{"inputs":[{"internalType":"address","name":"_feeToSetter","type":"address"}],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"token0","type":"address"},{"indexed":true,"internalType":"address","name":"token1","type":"address"},{"indexed":false,"internalType":"address","name":"pair","type":"address"},{"indexed":false,"internalType":"uint256","name":"","type":"uint256"}],"name":"PairCreated","type":"event"},{"constant":true,"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"allPairs","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"allPairsLength","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"tokenA","type":"address"},{"internalType":"address","name":"tokenB","type":"address"}],"name":"createPair","outputs":[{"internalType":"address","name":"pair","type":"address"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"feeTo","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"feeToSetter","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"address","name":"","type":"address"}],"name":"getPair","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"_feeTo","type":"address"}],"name":"setFeeTo","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"_feeToSetter","type":"address"}],"name":"setFeeToSetter","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"}]')
contract = web3.eth.contract(address=uniswap_factory, abi=uniswap_factory_abi)
lp_address = contract.functions.getPair(contract_address, WETH).call()
print(f"LP Address: {lp_address}")
# sys.exit()

# Define the BscScan API URL
url = f"https://api.etherscan.io/api?module=account&action=tokentx&contractaddress={contract_address}&apikey={api_key}"

# Send a request to BscScan API and parse the JSON response
response = requests.get(url)
data = json.loads(response.text)

token_created_to=None
count=0

if data['status'] == "1":
    transactions = data['result']

    # Filter transactions and get the first 'num_wallets' wallet addresses
    wallets = []
    print(f"\nThe first {num_wallets} wallets that bought the token after liquidity was added:\n")
    for tx in transactions:
        #0x3fc91a3afd70395cd496c647d5a6cc9d4b2b7fad
        # print( tx)
        print("====================================")



        if tx['from'] != contract_address and tx['to'] != contract_address:

            if tx['from'] not in wallets:
                print(f"{style.RED} {tx['from']}---->{tx['to']}  {style.RESET}")

                if tx['to'] != lp_address.lower() and tx['from'] != token_created_to:

                    # wallets.append(tx['from'])
                    # print(wallets)

                    if tx['from']== "0x0000000000000000000000000000000000000000":
                        count+=1
                        token_created_to = tx['to']
                        print(f"{style.GREEN}[TOKEN CREATION]{style.RESET} Wallet: {tx['to']} ETHq_Balance {style.GREEN}[ {web3.from_wei(web3.eth.get_balance(web3.to_checksum_address(tx['to'])), 'ether')}]{style.RESET} , NONCE: {style.MAGENTA}{web3.eth.get_transaction_count(web3.to_checksum_address(tx['to']))} {style.RESET} --> {style.RED}{tx['blockNumber']} {style.RESET} ---> {style.YELLOW}{int(tx['value']) / 10 ** int(tx['tokenDecimal'])} {style.RESET} , TxHash: https://etherscan.io/tx/{tx['hash']}")
                    if tx['from']== token_created_to and count>0:
                        print(f"{style.GREEN}[INSIDER TRANSFER]{style.RESET} Wallet: {tx['to']} ETHq_Balance {style.GREEN}[ {web3.from_wei(web3.eth.get_balance(web3.to_checksum_address(tx['to'])), 'ether')}]{style.RESET} , NONCE: {style.MAGENTA}{web3.eth.get_transaction_count(web3.to_checksum_address(tx['to']))} {style.RESET} --> {style.RED}{tx['blockNumber']} {style.RESET} ---> {style.YELLOW}{int(tx['value']) / 10 ** int(tx['tokenDecimal'])} {style.RESET} , TxHash: https://etherscan.io/tx/{tx['hash']}")



                    if (tx['from'] == "0x3fc91a3afd70395cd496c647d5a6cc9d4b2b7fad" and tx['to']==lp_address.lower()) or (tx['from'] == "0x3fc91a3afd70395cd496c647d5a6cc9d4b2b7fad" and tx['to']==token_created_to):
                       continue
                    if tx['from'] == token_created_to and tx['to']== lp_address.lower():
                        count=0
                        print(f"{style.MAGENTA}[POOL ADDED]{style.RESET}  --> {style.RED}{tx['blockNumber']} {style.RESET} ---> {style.YELLOW}{int(tx['value']) / 10 ** int(tx['tokenDecimal'])} {style.RESET} , TxHash: https://etherscan.io/tx/{tx['hash']}")


                    print(f"{style.GREEN}[BUY]{style.RESET} Wallet: {tx['to']} ETHq_Balance {style.GREEN}[ {web3.from_wei(web3.eth.get_balance(web3.to_checksum_address(tx['to'])), 'ether')}]{style.RESET} , NONCE: {style.MAGENTA}{web3.eth.get_transaction_count(web3.to_checksum_address(tx['to']))} {style.RESET} --> {style.RED}{tx['blockNumber']} {style.RESET} ---> {style.YELLOW}{int(tx['value']) / 10 ** int(tx['tokenDecimal'])} {style.RESET} , TxHash: https://etherscan.io/tx/{tx['hash']}")

                elif  tx['from'] == token_created_to and count>0:
                    print(f"{style.MAGENTA}[INSIDER TRANSFER]{style.RESET} Wallet: {tx['to']} ETHq_Balance {style.GREEN}[ {web3.from_wei(web3.eth.get_balance(web3.to_checksum_address(tx['to'])), 'ether')}]{style.RESET} , NONCE: {style.MAGENTA}{web3.eth.get_transaction_count(web3.to_checksum_address(tx['to']))} {style.RESET} --> {style.RED}{tx['blockNumber']} {style.RESET} ---> {style.YELLOW}{int(tx['value']) / 10 ** int(tx['tokenDecimal'])} {style.RESET} , TxHash: https://etherscan.io/tx/{tx['hash']}")



                else:
                    print(f"{style.RED}[SELL]{style.RESET} Wallet: {tx['from']} ETHq_Balance {style.GREEN}[ {web3.from_wei(web3.eth.get_balance(web3.to_checksum_address(tx['from'])), 'ether')}]{style.RESET} , NONCE: {style.MAGENTA}{web3.eth.get_transaction_count(web3.to_checksum_address(tx['from']))} {style.RESET} --> {style.RED}{tx['blockNumber']} {style.RESET} ---> {style.YELLOW}{int(tx['value']) / 10 ** int(tx['tokenDecimal'])} {style.RESET} , TxHash: https://etherscan.io/tx/{tx['hash']}")


                # print(f"{len(wallets)}. Wallet: {tx['from']} ETHq_Balance {style.GREEN}[ {web3.from_wei(web3.eth.get_balance(web3.to_checksum_address(tx['from'])), 'ether') }]{style.RESET} , NONCE: {style.MAGENTA}{web3.eth.get_transaction_count(web3.to_checksum_address(tx['from']))} {style.RESET} --> {style.RED}{tx['blockNumber']} {style.RESET} ---> {style.YELLOW}{int(tx['value'])/10**int(tx['tokenDecimal'])} {style.RESET} , TxHash: https://etherscan.io/tx/{tx['hash']}")

                if len(wallets) >= num_wallets:
                    break
        # elif tx['to'] == contract_address.lower(): #and len(wallets) == 1:
        #     print(f"Liquidity added transaction: TxHash: {tx['hash']}\n")
else:
    print("Error fetching transactions. Please check the contract address and try again.")
