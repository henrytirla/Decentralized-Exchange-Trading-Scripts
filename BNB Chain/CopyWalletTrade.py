print("Loading...")

from web3 import Web3
import datetime
import threading
import json
import asyncio
import requests
import time
import os
import sys
import config

from web3.middleware import geth_poa_middleware




# allows different colour text to be used


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




currentTimeStamp =""

def getTimestamp():
    while True:
        timeStampData = datetime.datetime.now()
        global currentTimeStamp
        currentTimeStamp = "[" + timeStampData.strftime("%H:%M:%S.%f")[:-3] + "]"


# -------------------------------- INITIALISE ------------------------------------------

timeStampThread = threading.Thread(target=getTimestamp)
timeStampThread.start()

#---Enter amount you want to snipe with
snipeBNBAmount = 0.0001
#print(getTimestamp())
print("current time", currentTimeStamp, )
# -------------------------------- INITIALISE ------------------------------------------
print(currentTimeStamp + " [Info] Using Snipe Amount: " + style.GREEN+ str(snipeBNBAmount), "BNB")

web3 = Web3(Web3.HTTPProvider("https://bsc-dataseed1.binance.org/"))
web3.middleware_onion.inject(geth_poa_middleware, layer=0)

#Your Wallet Address
walletAddress ="Enter your Wallet address"
if web3.isConnected():
    print(style.YELLOW + currentTimeStamp + " BSC Mainnet  Node successfully connected")
balance = web3.eth.getBalance(walletAddress) # here balance is in wei
b =web3.fromWei(balance,"ether")

# pancakeswap factory
#pancake_factory = '0xcA143Ce32Fe78f1f7019d7d551a6402fC5350c73'  #Testnet  #0x6725F303b657a9451d8BA641348b6761A6CC7a17

"""Connection to Pancakeswap"""
# #pancakeswap router
#pancakeSwapRouterAddress ="0x9Ac64Cc6e4415144C455BD8E4837Fea55603e5c3"  #Testnet
pancakeSwapRouterAddress ="0x10ED43C718714eb63d5aA57B78B54704E256024E"  #Mainnet


#pancakeswap router abi

pancake_abi ="Pancakeswap ABI"

tokenNameABI = 'TOken ABI'

contractbuy = web3.eth.contract(address=pancakeSwapRouterAddress, abi=pancake_abi)


# ------------------------------------- BUY SPECIFIED TOKEN ON PANCAKESWAP ----------------------------------------------------------

def Buy(tokenAddress):


    #tokenAddress =input("\n Enter Token address you want to buy: ")
    tokenAddress = web3.toChecksumAddress(tokenAddress)

    getTokenName = web3.eth.contract(address=tokenAddress,
                                     abi=tokenNameABI)
    tokenSymbol = getTokenName.functions.symbol().call()
    print("\nTrying to buy... ", tokenSymbol)


    tokenToBuy = web3.toChecksumAddress(tokenAddress)
    spend = web3.toChecksumAddress("0xbb4CdB9CBd36B01bD1cBaEBF2De08d9173bc095c")  # wbnb contract address

    #nonce = web3.eth.get_transaction_count(walletAddress)

    #swapExactTokensForTokensSupportingFeeOnTransferTokens(
    pancakeswap2_txn = contractbuy.functions.swapExactETHForTokens(

        # tokenA, tokenB when buying with 2 token
        0,  # tokenB,
        [spend, tokenToBuy],
        config.wallet_Address,
        (int(time.time()) + 10000)
    ).buildTransaction({

        'from': config.wallet_Address,
        #'value': web3.toWei(0.01, 'ether'),
        'value': web3.toWei(snipeBNBAmount, 'ether'),
        # This is the Token(BNB) amount you want to Swap from  | Comment out for token
        'gas': 300000,
        'gasPrice': web3.toWei('15', 'gwei'),
        'nonce': web3.eth.get_transaction_count(config.wallet_Address),
    })
    # Sign transaction with priavte key here
    signed_txn = web3.eth.account.sign_transaction(pancakeswap2_txn, config.private)
    tx_token = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
    print(currentTimeStamp,"Copying trade was successful, bought: ", 'https://bscscan.com/tx/' + web3.toHex(tx_token))

#
swap_functions =["swapETHForExactTokens","swapExactETHForTokens","swapExactETHForTokensSupportingFeeOnTransferTokens","swapExactTokensForETH","swapExactTokensForETHSupportingFeeOnTransferTokens","swapExactTokensForTokens","swapExactTokensForTokensSupportingFeeOnTransferTokens","swapTokensForExactETH","swapTokensForExactTokens","addLiquidityETH"]


method_function={"swapETHForExactTokens": True,"swapExactETHForTokens":True, "swapExactETHForTokensSupportingFeeOnTransferTokens": True,"swapExactTokensForETH": True}
arr =[]

#Wallet you want to copy trades as they are executed
copyWallet="Enter the Wallet you want to copytrade"


# Loop forever to scan the mempool
x= True
while x == True:
    try:
        while True:
            # Get the pending transactions in the mempool
            transactions = web3.eth.getBlock("pending")['transactions']
            ##print(transactions)
            for tx in transactions:

                tx_hash = web3.toHex(tx)
                trans = web3.eth.get_transaction(tx_hash)
                from_wallet = trans['from']
                #print("FROM", from_wallet)
                data = trans['input']
                to = trans['to']

                #print(to, tx_hash)

                if to == pancakeSwapRouterAddress:
                    decoded = contractbuy.decode_function_input(data)

                    tokenBought = decoded[1]['path'][1]
                    current_block = web3.eth.blockNumber


                    print(style.YELLOW+"PANCAKESWAP-------MEMEPOOL")
                    print(decoded)
                    print("FROM------",from_wallet)
                    print("TO-----",to)
                    print('https://.bscscan.com/tx/' + tx_hash)
                    print(decoded)
                    # for swapFunc in range(len(swap_functions)):
                    #     if swap_functions[swapFunc] in str(decoded[0]):
                    #         arr.append(swap_functions[swapFunc])


                    # print(style.GREEN+"METHOD-----",arr[-1] )
                    #method_function[arr[-1]] == True and
                    if  from_wallet == copyWallet:
                        print(style.GREEN+'https://.bscscan.com/tx/' + tx_hash,"Trade Detected--BUYING NOW")
                        Buy(tokenBought)




                else:
                    #print(style.RED+"NO trade found from Copy wallet")
                    pass






    except Exception as e:
        print(f'Error occurred: {e}')
        x = True
