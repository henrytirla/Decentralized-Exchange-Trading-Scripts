import csv
import webbrowser
from web3 import Web3
from alchemy import Alchemy, Network
import datetime
import requests
import os
from queue import Queue
import threading

from web3.exceptions import TransactionNotFound


alchemy_ws_url = "wss://eth-mainnet.g.alchemy.com/v2/BLHi-AZvCt6LjvO8W7nFtloBJFZa393M"
api_key = "BLHi-AZvCt6LjvO8W7nFtloBJFZa393M"
network = Network.ETH_MAINNET
alchemy = Alchemy(api_key, network)

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


w3 = Web3(Web3.HTTPProvider("https://eth-mainnet.g.alchemy.com/v2/lTlatSTYDZmCv6wVLRIDff7S3kZhL2dq"))

WETH_ADDRESS = '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2'
WETH_ABI = '[{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"guy","type":"address"},{"name":"wad","type":"uint256"}],"name":"approve","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"src","type":"address"},{"name":"dst","type":"address"},{"name":"wad","type":"uint256"}],"name":"transferFrom","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"wad","type":"uint256"}],"name":"withdraw","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"}],"name":"balanceOf","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"dst","type":"address"},{"name":"wad","type":"uint256"}],"name":"transfer","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[],"name":"deposit","outputs":[],"payable":true,"stateMutability":"payable","type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"},{"name":"","type":"address"}],"name":"allowance","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"payable":true,"stateMutability":"payable","type":"fallback"},{"anonymous":false,"inputs":[{"indexed":true,"name":"src","type":"address"},{"indexed":true,"name":"guy","type":"address"},{"indexed":false,"name":"wad","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"src","type":"address"},{"indexed":true,"name":"dst","type":"address"},{"indexed":false,"name":"wad","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"dst","type":"address"},{"indexed":false,"name":"wad","type":"uint256"}],"name":"Deposit","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"src","type":"address"},{"indexed":false,"name":"wad","type":"uint256"}],"name":"Withdrawal","type":"event"}]'

weth_contract = w3.eth.contract(address=WETH_ADDRESS, abi=WETH_ABI)
sellAbi = '[{"inputs":[{"internalType":"string","name":"_NAME","type":"string"},{"internalType":"string","name":"_SYMBOL","type":"string"},{"internalType":"uint256","name":"_DECIMALS","type":"uint256"},{"internalType":"uint256","name":"_supply","type":"uint256"},{"internalType":"uint256","name":"_txFee","type":"uint256"},{"internalType":"uint256","name":"_lpFee","type":"uint256"},{"internalType":"uint256","name":"_MAXAMOUNT","type":"uint256"},{"internalType":"uint256","name":"SELLMAXAMOUNT","type":"uint256"},{"internalType":"address","name":"routerAddress","type":"address"},{"internalType":"address","name":"tokenOwner","type":"address"}],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"spender","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"minTokensBeforeSwap","type":"uint256"}],"name":"MinTokensBeforeSwapUpdated","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"previousOwner","type":"address"},{"indexed":true,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"tokensSwapped","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"ethReceived","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"tokensIntoLiqudity","type":"uint256"}],"name":"SwapAndLiquify","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"bool","name":"enabled","type":"bool"}],"name":"SwapAndLiquifyEnabledUpdated","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"inputs":[],"name":"_liquidityFee","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"_maxTxAmount","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"_owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"_taxFee","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"spender","type":"address"}],"name":"allowance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"approve","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"claimTokens","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"decimals","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"subtractedValue","type":"uint256"}],"name":"decreaseAllowance","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"tAmount","type":"uint256"}],"name":"deliver","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"excludeFromFee","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"excludeFromReward","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"geUnlockTime","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"includeInFee","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"includeInReward","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"addedValue","type":"uint256"}],"name":"increaseAllowance","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"isExcludedFromFee","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"isExcludedFromReward","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"time","type":"uint256"}],"name":"lock","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"numTokensSellToAddToLiquidity","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"tAmount","type":"uint256"},{"internalType":"bool","name":"deductTransferFee","type":"bool"}],"name":"reflectionFromToken","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"renounceOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"liquidityFee","type":"uint256"}],"name":"setLiquidityFeePercent","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"maxTxPercent","type":"uint256"}],"name":"setMaxTxPercent","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"swapNumber","type":"uint256"}],"name":"setNumTokensSellToAddToLiquidity","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bool","name":"_enabled","type":"bool"}],"name":"setSwapAndLiquifyEnabled","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"taxFee","type":"uint256"}],"name":"setTaxFeePercent","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"swapAndLiquifyEnabled","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"rAmount","type":"uint256"}],"name":"tokenFromReflection","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalFees","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transfer","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"sender","type":"address"},{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transferFrom","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"uniswapV2Pair","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"uniswapV2Router","outputs":[{"internalType":"contract IUniswapV2Router02","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"unlock","outputs":[],"stateMutability":"nonpayable","type":"function"},{"stateMutability":"payable","type":"receive"}]'

def getTotalBuys(to_address, contract_address):
    category = ["erc20"]
    with_metadata = False
    from_block = "0x0"
    to_block = "latest"
    from_address = None
    result = alchemy.core.get_asset_transfers(category,with_metadata,from_block,to_block,from_address,to_address,[contract_address])
    length= len(result['transfers'])
    try:
        token_name= result['transfers'][0].asset
    except Exception as e:
        token_name ="Unknown"
    return length, token_name

jareth_address="0xae2Fc483527B8EF99EB5D9B44875F005ba1FaE13"
jareth_mev={"0x6b75d8AF000000e20B7a7DDf000Ba900b4009A80":True}

last_processed_block = w3.eth.block_number
count=0



uniswap_v2_pair_abi = '[{"inputs":[],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"spender","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"sender","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount0","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount1","type":"uint256"},{"indexed":true,"internalType":"address","name":"to","type":"address"}],"name":"Burn","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"sender","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount0","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount1","type":"uint256"}],"name":"Mint","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"sender","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount0In","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount1In","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount0Out","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount1Out","type":"uint256"},{"indexed":true,"internalType":"address","name":"to","type":"address"}],"name":"Swap","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint112","name":"reserve0","type":"uint112"},{"indexed":false,"internalType":"uint112","name":"reserve1","type":"uint112"}],"name":"Sync","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"constant":true,"inputs":[],"name":"DOMAIN_SEPARATOR","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"MINIMUM_LIQUIDITY","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"PERMIT_TYPEHASH","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"address","name":"","type":"address"}],"name":"allowance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"}],"name":"approve","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"to","type":"address"}],"name":"burn","outputs":[{"internalType":"uint256","name":"amount0","type":"uint256"},{"internalType":"uint256","name":"amount1","type":"uint256"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"factory","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"getReserves","outputs":[{"internalType":"uint112","name":"_reserve0","type":"uint112"},{"internalType":"uint112","name":"_reserve1","type":"uint112"},{"internalType":"uint32","name":"_blockTimestampLast","type":"uint32"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"_token0","type":"address"},{"internalType":"address","name":"_token1","type":"address"}],"name":"initialize","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"kLast","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"to","type":"address"}],"name":"mint","outputs":[{"internalType":"uint256","name":"liquidity","type":"uint256"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"nonces","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"},{"internalType":"uint256","name":"deadline","type":"uint256"},{"internalType":"uint8","name":"v","type":"uint8"},{"internalType":"bytes32","name":"r","type":"bytes32"},{"internalType":"bytes32","name":"s","type":"bytes32"}],"name":"permit","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"price0CumulativeLast","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"price1CumulativeLast","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"to","type":"address"}],"name":"skim","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"uint256","name":"amount0Out","type":"uint256"},{"internalType":"uint256","name":"amount1Out","type":"uint256"},{"internalType":"address","name":"to","type":"address"},{"internalType":"bytes","name":"data","type":"bytes"}],"name":"swap","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[],"name":"sync","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"token0","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"token1","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"}],"name":"transfer","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"}],"name":"transferFrom","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"}]'

#uniswap_v2_pair = w3.eth.contract(address=lp_address, abi=uniswap_v2_pair_abi)



def getTimestamp():
    while True:
        timeStampData = datetime.datetime.now()
        currentTimeStamp = "[" + timeStampData.strftime("%H:%M:%S.%f")[:-3] + "]"
        return currentTimeStamp


def get_token_from_lp(lpAddres):
    uniswap_v2_pair = w3.eth.contract(address=lpAddres, abi=uniswap_v2_pair_abi)

    tokenA_address = uniswap_v2_pair.functions.token0().call()
    tokenB_address = uniswap_v2_pair.functions.token1().call()
    if tokenA_address == "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2":
        return tokenB_address
    else:
        return tokenA_address

def get_TokenMetaData(token_address):
    url = "https://api.honeypot.is/v2/IsHoneypot"

    params = {"address": token_address}
    response = requests.get(url, params=params)
    if response.status_code==200:
        data = response.json()
        token_name = data['token']['name']
        token_symbol = data['token']['symbol']
        token_decimals = data['token']['decimals']
        token_total_holders = data['token']['totalHolders']
        liquidity = data['pair']['liquidity']
        pair_address = data['pairAddress']
        creation_txnHash = data['pair']['creationTxHash']

        return  token_name,token_symbol,token_decimals,token_total_holders,liquidity,pair_address,creation_txnHash

def get_creation_timestamp(token_address):
    url = "https://api.honeypot.is/v2/IsHoneypot"

    params = {"address": token_address}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        creation_timestamp = int(data['pair']['createdAtTimestamp'])
        datetime_obj = datetime.datetime.utcfromtimestamp(creation_timestamp)
        current_time = datetime.datetime.utcnow()
        # Calculate the time difference
        time_difference = current_time - datetime_obj
        days = time_difference.days
        hours, remainder = divmod(time_difference.seconds, 3600)
        minutes, _ = divmod(remainder, 60)


    return days,hours,minutes
def format_hex(original_hex):
    hex_without_prefix = original_hex[2:]

    desired_length = 64

    padded_hex = hex_without_prefix.zfill(desired_length)

    final_hex = "0x" + padded_hex

    return final_hex.lower()
def tokenBought_Amount(txhash,tokenAddress,pairAddress,tokenDecimal):
    receipt = alchemy.core.get_transaction_receipt(txhash)
    format_pair = format_hex(pairAddress)
    target_topics = [
        alchemy.to_bytes(hexstr="0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef"),
        Web3.to_bytes(hexstr=format_pair),
        Web3.to_bytes(hexstr="0x0000000000000000000000006b75d8af000000e20b7a7ddf000ba900b4009a80")
    ]

    # print(receipt)
    for log in receipt['logs']:
        #print(log['topics'], log['address'])

        if log['topics'][0:3] == target_topics and log['address'] == tokenAddress:
            hex_data = log['data'].hex()
            decoded_data = alchemy.to_int(hexstr=hex_data)
            decoded_data_in_ether = decoded_data / 10 ** tokenDecimal
            return decoded_data_in_ether

def get_InitialLP(transaction_hash):


    receipt = alchemy.core.get_transaction_receipt(transaction_hash)

    target_topics = [
        Web3.to_bytes(hexstr="0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef")
        #Web3.to_bytes(hexstr="0x0000000000000000000000007a250d5630b4cf539739df2c5dacb4c659f2488d")
    ]

    for log in receipt['logs']:
        if log['topics'][0:1] == target_topics and log['address'] =="0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2":
            hex_data = log['data'].hex()
            decoded_data = Web3.to_int(hexstr=hex_data)
            decoded_data_in_ether = Web3.from_wei(decoded_data, 'ether')
            return decoded_data_in_ether

    return None



def get_Address(txnhash,toAddress):
    receipt = alchemy.core.get_transaction_receipt(txnhash)
    hex_to=format_hex(toAddress)

    target_topics = [
        alchemy.to_bytes(hexstr="0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef"),
        alchemy.to_bytes(hexstr=hex_to)
    ]

    # print(receipt)
    for log in receipt['logs']:
        # print(log['topics'],log['address'])
        if log['topics'][0:2] == target_topics:

            # print(log['address'])
            return log['address']

def jareth_TokenBalance(TokenAddrress):
    # define the sender address and prints the balance (in ETH)
    #TokenAddrress =input("Enter Token Address ")
    #amt= input("Enter Amount in Eth ")
    web3 = Web3(Web3.HTTPProvider("https://eth-mainnet.g.alchemy.com/v2/lTlatSTYDZmCv6wVLRIDff7S3kZhL2dq"))

    tokenAbi = [
        {"constant": True, "inputs": [], "name": "decimals", "outputs": [{"name": "", "type": "uint8"}],
         "payable": False, "stateMutability": "view", "type": "function"},
        {"constant": True, "inputs": [], "name": "name", "outputs": [{"name": "", "type": "string"}], "payable": False,
         "stateMutability": "view", "type": "function"},
        {"constant": True, "inputs": [], "name": "symbol", "outputs": [{"name": "", "type": "string"}],
         "payable": False, "stateMutability": "view", "type": "function"},
        {"constant": True, "inputs": [{"name": "owner", "type": "address"}], "name": "balanceOf",
         "outputs": [{"name": "", "type": "uint256"}], "payable": False, "stateMutability": "view", "type": "function"}
    ]
    web3.to_checksum_address(TokenAddrress)
    sender_address = "0x6b75d8AF000000e20B7a7DDf000Ba900b4009A80"
    # balance = web3.eth.get_balance(sender_address)
    # print("This address has:", web3.from_wei(balance, "ether"), "ETH")

    # specify token to buy
    token_to_buy = web3.to_checksum_address(TokenAddrress)
    getTokenName = web3.eth.contract(address=TokenAddrress,abi=tokenAbi)
    tokenSymbol = getTokenName.functions.symbol().call()
    tokenContract = web3.eth.contract(address=TokenAddrress, abi=sellAbi)
    decimals = tokenContract.functions.decimals().call()
    DECIMAL = 10 ** decimals
    Token_balance = tokenContract.functions.balanceOf(sender_address).call()
    return Token_balance / DECIMAL

processed_events = set()  # Initialize a set to keep track of processed events
processed_destinations = set()


event_queue = Queue()
csv_file_path = "jareth_details.csv"
fieldnames = ['Block', 'Amount', 'From', 'To', 'Tx_Hash', 'Token_Name', 'Token_Symbol', 'Token_Decimals',
             'Token_Total_Holders', 'Liquidity', 'Token_Address', 'Initial_Liquidity']

if not os.path.exists(csv_file_path):
    with open(csv_file_path, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
def process_event(log):
    tx_hash = w3.to_hex(log.transactionHash)
    if log.args.dst not in processed_destinations:
        if log.args.src in jareth_mev:
            #processed_destinations.add(log.args.dst)

            try:
                token_address= get_Address(tx_hash,log.args.dst)


                num_days, hours, minutes = get_creation_timestamp(token_address)
                formatted_time_difference = f"{num_days} days, {hours} hours, {minutes} minutes ago"
                if num_days>1:
                    processed_destinations.add(log.args.dst)

            except Exception as e:
                print(e)

            numberOfBuys, tokenName = getTotalBuys(log.args.src, token_address)
            #if num_days <1 and hours <1:
            print(style.GREEN + f" {latest_block} {numberOfBuys, tokenName} {style.YELLOW}Token Address: {token_address}{style.RESET} {style.RESET} {style.RED} {formatted_time_difference}",
                      style.RESET)
            if numberOfBuys == 1 and num_days< 1 and hours < 1:
                print(style.BLUE, "======FIRST BUY=========", style.RESET)

                amt_eth = w3.from_wei(log.args.wad, 'ether')
                rounded_amt_eth = round(amt_eth, 1)
                token_name, token_symbol, token_decimals, token_total_holders, liquidity, pair_address, creation_txnHash = get_TokenMetaData(
                    token_address)
                amount_bought = tokenBought_Amount(tx_hash, token_address,pair_address, token_decimals)
                tokenAmount_left= jareth_TokenBalance(token_address)
                url = "https://dexscreener.com/ethereum/"+pair_address
                webbrowser.open(url)

                print(f"Token Address: ,{token_address} {style.MAGENTA} Amount of tokens Received {amount_bought}{style.RESET}, Token Left: {style.RED} {tokenAmount_left} {style.RESET}")

                try:
                    Initial_liquidity = get_InitialLP(creation_txnHash)
                except TransactionNotFound:
                    print(f"Transaction with hash: '{creation_txnHash}' not found.")
                    Initial_liquidity = None

                with open(csv_file_path, 'a', newline='') as csvfile:
                    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                    writer.writerow({
                        'Block': latest_block,
                        'Amount': rounded_amt_eth,
                        'From': log.args.src,
                        'To': log.args.dst,
                        'Tx_Hash': f"https://etherscan.io/tx/{tx_hash}",
                        'Token_Name': token_name,
                        'Token_Symbol': token_symbol,
                        'Token_Decimals': token_decimals,
                        'Token_Total_Holders': token_total_holders,
                        'Liquidity': liquidity,
                        'Token_Address': token_address,
                        'Initial_Liquidity': Initial_liquidity
                    })

                print(
                    f"{getTimestamp()} Transfer of {latest_block} {rounded_amt_eth} WETH  from {log.args.src} to {log.args.dst} Tx_HASH:  https://etherscan.io/tx/{w3.to_hex(log.transactionHash)}")

                print(style.GREEN + f"{numberOfBuys, tokenName} {style.RESET} {style.RED} {formatted_time_difference}",
                      style.RESET)
                print("Token Amount Left",tokenAmount_left)

                print("------------------")

def process_queue():
    while True:
        log = event_queue.get()
        process_event(log)
        event_queue.task_done()

thread = threading.Thread(target=process_queue)
thread.daemon = True
thread.start()
print(style.YELLOW,"SCANNING FOR NEW BUYS FOR NEWLY CREATED PAIRS.....",style.RESET)

while True:
    try:
        latest_block = w3.eth.block_number
        logs = weth_contract.events.Transfer().get_logs(
            fromBlock=last_processed_block + 1,
            toBlock=latest_block
        )

        for log in logs:
            event_queue.put(log)


        last_processed_block = latest_block

    except Exception as e:
        pass