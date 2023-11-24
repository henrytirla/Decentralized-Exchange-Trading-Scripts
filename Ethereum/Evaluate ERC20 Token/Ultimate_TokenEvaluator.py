import sys
import requests
import json
import datetime
from goplus.token import Token
from dateutil import parser
import time
from web3 import Web3
from alchemy import Alchemy, Network
api_key = "Enter Your Alchemy API KEY"
network = Network.ETH_MAINNET
alchemy = Alchemy(api_key, network)

# API endpoint URL
url = "https://api.honeypot.is/v2/IsHoneypot"



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


# Construct the query parameters
web3 = Web3(Web3.HTTPProvider("https://eth-mainnet.g.alchemy.com/v2/Enter Your Alchemy API KEY"))
tokenmodel_abi = '[{"inputs":[],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"spender","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"sender","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount0","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount1","type":"uint256"},{"indexed":true,"internalType":"address","name":"to","type":"address"}],"name":"Burn","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"sender","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount0","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount1","type":"uint256"}],"name":"Mint","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"sender","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount0In","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount1In","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount0Out","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount1Out","type":"uint256"},{"indexed":true,"internalType":"address","name":"to","type":"address"}],"name":"Swap","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint112","name":"reserve0","type":"uint112"},{"indexed":false,"internalType":"uint112","name":"reserve1","type":"uint112"}],"name":"Sync","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"constant":true,"inputs":[],"name":"DOMAIN_SEPARATOR","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"MINIMUM_LIQUIDITY","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"PERMIT_TYPEHASH","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"address","name":"","type":"address"}],"name":"allowance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"}],"name":"approve","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"to","type":"address"}],"name":"burn","outputs":[{"internalType":"uint256","name":"amount0","type":"uint256"},{"internalType":"uint256","name":"amount1","type":"uint256"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"factory","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"getReserves","outputs":[{"internalType":"uint112","name":"_reserve0","type":"uint112"},{"internalType":"uint112","name":"_reserve1","type":"uint112"},{"internalType":"uint32","name":"_blockTimestampLast","type":"uint32"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"_token0","type":"address"},{"internalType":"address","name":"_token1","type":"address"}],"name":"initialize","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"kLast","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"to","type":"address"}],"name":"mint","outputs":[{"internalType":"uint256","name":"liquidity","type":"uint256"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"nonces","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"},{"internalType":"uint256","name":"deadline","type":"uint256"},{"internalType":"uint8","name":"v","type":"uint8"},{"internalType":"bytes32","name":"r","type":"bytes32"},{"internalType":"bytes32","name":"s","type":"bytes32"}],"name":"permit","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"price0CumulativeLast","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"price1CumulativeLast","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"to","type":"address"}],"name":"skim","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"uint256","name":"amount0Out","type":"uint256"},{"internalType":"uint256","name":"amount1Out","type":"uint256"},{"internalType":"address","name":"to","type":"address"},{"internalType":"bytes","name":"data","type":"bytes"}],"name":"swap","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[],"name":"sync","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"token0","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"token1","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"}],"name":"transfer","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"}],"name":"transferFrom","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"}]'

def get_deployer_address(contract_address):
    url = "https://eth-mainnet.g.alchemy.com/v2/Enter Your Alchemy API KEY"
    payload = {
        "id": 1,
        "jsonrpc": "2.0",
        "method": "alchemy_getAssetTransfers",
        "params": [
            {
                "fromBlock": "0x0",
                "toBlock": "latest",
                "category": ["erc20"],
                "withMetadata": False,
                "excludeZeroValue": True,
                "maxCount": "0x3e8",

                # 'toAddress':pair_address,

                "contractAddresses": [contract_address],
                "order": "asc"
            }
        ]
    }

    headers = {
        "accept": "application/json",
        "content-type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)
    response_data = json.loads(response.text)
    #print(response_data)


    first_transfer_to = response_data['result']['transfers'][0]['to']
    first_transfer_to=web3.to_checksum_address(first_transfer_to)
    return first_transfer_to



def lock_time_difference(creation_time_str):
    from datetime import datetime, timedelta

    creation_time = datetime.strptime(creation_time_str, "%d-%m-%Y %H:%M:%S")
    current_time = datetime.utcnow()
    time_difference = creation_time - current_time  # Swap the positions for correct future time difference

    years = time_difference.days // 365
    days = time_difference.days
    hours, remainder = divmod(time_difference.seconds, 3600)
    minutes, _ = divmod(remainder, 60)
    return days, hours, minutes


def get_numberBuys(contract_address, pair_address):
    asset_transfer = alchemy.core.get_asset_transfers(
        # category=["external", "internal", "erc20", "erc721", "erc1155", "specialnft"],
        category=["erc20"],
        from_block="0x0",
        to_block="latest",
        with_metadata=False,
        exclude_zero_value=True,
        contract_addresses=[contract_address],
        order="asc")



    unique_to_addresses = set()
    for t in asset_transfer['transfers']:
        unique_to_addresses.add(t.to)

    return len(unique_to_addresses)-1

def get_SellNumber(pairAddress, contract_address):
    url = "https://eth-mainnet.g.alchemy.com/v2/Enter Your Alchemy API KEY"
    payload = {
        "id": 1,
        "jsonrpc": "2.0",
        "method": "alchemy_getAssetTransfers",
        "params": [
            {
                "fromBlock": "0x0",
                "toBlock": "latest",
                "category": ["erc20"],
                "withMetadata": False,
                "excludeZeroValue": True,
                "maxCount": "0x3e8",
                "toAddress": pairAddress,
                "contractAddresses": [contract_address],
                "order": "asc"
            }
        ]
    }
    headers = {
        "accept": "application/json",
        "content-type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)
    response_data = json.loads(response.text)

    total_transfers = len(response_data['result']['transfers'])
    unique_from_addresses = set()
    for t in response_data['result']['transfers']:
        unique_from_addresses.add(t['from'])

    return total_transfers-1, len(unique_from_addresses)-1


def get_owner_and_balance(token_address):
    Eth_Api = "Enter Your ETHERSCAN API KEY"  # Change this to your Etherscan API ID

    abiCodeGetRequestURL = "https://api.etherscan.io/api?module=contract&action=getabi&address=" + token_address + "&apikey=" + Eth_Api
    resultAbi = requests.get(url=abiCodeGetRequestURL).json()
    tokenmodel_abi = '[{"inputs":[],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"spender","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"sender","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount0","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount1","type":"uint256"},{"indexed":true,"internalType":"address","name":"to","type":"address"}],"name":"Burn","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"sender","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount0","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount1","type":"uint256"}],"name":"Mint","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"sender","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount0In","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount1In","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount0Out","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount1Out","type":"uint256"},{"indexed":true,"internalType":"address","name":"to","type":"address"}],"name":"Swap","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint112","name":"reserve0","type":"uint112"},{"indexed":false,"internalType":"uint112","name":"reserve1","type":"uint112"}],"name":"Sync","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"constant":true,"inputs":[],"name":"DOMAIN_SEPARATOR","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"MINIMUM_LIQUIDITY","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"PERMIT_TYPEHASH","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"address","name":"","type":"address"}],"name":"allowance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"}],"name":"approve","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"to","type":"address"}],"name":"burn","outputs":[{"internalType":"uint256","name":"amount0","type":"uint256"},{"internalType":"uint256","name":"amount1","type":"uint256"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"factory","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"getReserves","outputs":[{"internalType":"uint112","name":"_reserve0","type":"uint112"},{"internalType":"uint112","name":"_reserve1","type":"uint112"},{"internalType":"uint32","name":"_blockTimestampLast","type":"uint32"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"_token0","type":"address"},{"internalType":"address","name":"_token1","type":"address"}],"name":"initialize","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"kLast","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"to","type":"address"}],"name":"mint","outputs":[{"internalType":"uint256","name":"liquidity","type":"uint256"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"nonces","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"},{"internalType":"uint256","name":"deadline","type":"uint256"},{"internalType":"uint8","name":"v","type":"uint8"},{"internalType":"bytes32","name":"r","type":"bytes32"},{"internalType":"bytes32","name":"s","type":"bytes32"}],"name":"permit","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"price0CumulativeLast","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"price1CumulativeLast","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"to","type":"address"}],"name":"skim","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"uint256","name":"amount0Out","type":"uint256"},{"internalType":"uint256","name":"amount1Out","type":"uint256"},{"internalType":"address","name":"to","type":"address"},{"internalType":"bytes","name":"data","type":"bytes"}],"name":"swap","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[],"name":"sync","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"token0","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"token1","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"}],"name":"transfer","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"}],"name":"transferFrom","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"}]'
    ownership_function = '{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"}'
    getOwner_function = '{"inputs":[],"name":"getOwner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"}'
    #{"inputs": [],"name": "owner","outputs": [{"internalType": "address","name": "","type": "address"}],"stateMutability": "view","type": "function"}

    token_address = web3.to_checksum_address(token_address)
    contract = web3.eth.contract(address=token_address, abi=tokenmodel_abi)
    decimals = contract.functions.decimals().call()
    DECIMAL = 10 ** decimals
    totalSupply = contract.functions.totalSupply().call() / DECIMAL
    check = resultAbi
    contract_owner = "NULL"

    if check['status'] == '1':
        abi = check['result']
        tokenabi = abi

        if ownership_function in abi:
            contract = web3.eth.contract(address=token_address, abi=abi)

            owner = contract.functions.owner().call()
            contract_owner = owner
            owner_balance = contract.functions.balanceOf(owner).call() / DECIMAL
            percent_owner = owner_balance / totalSupply * 100

            # Return owner and percent_owner values
            return owner, round(percent_owner, 2)
        elif getOwner_function in abi:
            contract = web3.eth.contract(address=token_address, abi=abi)

            owner = contract.functions.getOwner().call()
            contract_owner = owner
            owner_balance = contract.functions.balanceOf(owner).call() / DECIMAL
            percent_owner = owner_balance / totalSupply * 100

            # Return owner and percent_owner values
            return owner, round(percent_owner, 2)

    else:
        contract_owner = None

        # If no owner information is found, return None for both values
    return contract_owner, None

def get_creation_timestamp(token_address):
    url = "https://api.honeypot.is/v2/IsHoneypot"

    params = {"address": token_address}
    response = requests.get(url, params=params)
    if response==200:
        data = response.json()
        creation_timestamp = int(data['pair']['createdAtTimestamp'])
        datetime_obj = datetime.datetime.utcfromtimestamp(creation_timestamp)
        current_time = datetime.datetime.utcnow()
        # Calculate the time difference
        time_difference = current_time - datetime_obj
        days = time_difference.days
        hours, remainder = divmod(time_difference.seconds, 3600)
        minutes, _ = divmod(remainder, 60)



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

def get_Days(creation_time_str):
    from datetime import datetime, timedelta

    creation_time = datetime.strptime(creation_time_str, "%d-%m-%Y %H:%M:%S")
    current_time = datetime.utcnow()
    time_difference = current_time - creation_time

    # Extract days, hours, and minutes from the time difference
    days = time_difference.days
    hours, remainder = divmod(time_difference.seconds, 3600)
    minutes, _ = divmod(remainder, 60)

    return days ,hours,minutes





def getOwnerPercentage_LpHash(contract_address, pair_address):
    contract = web3.eth.contract(address=contract_address, abi=tokenmodel_abi)
    decimals = contract.functions.decimals().call()
    DECIMAL = 10 ** decimals
    totalSupply = contract.functions.totalSupply().call() / DECIMAL

    asset_transfer = alchemy.core.get_asset_transfers(
        # category=["external", "internal", "erc20", "erc721", "erc1155", "specialnft"],
        category=["erc20"],
        from_block="0x0",
        to_block="latest",
        with_metadata=False,
        exclude_zero_value=True,
        contract_addresses=[contract_address],
        order="asc"

    )

    txn_hash = None
    first_transfer_to_pair_value = 0
    amount_toDead= 0
    found_t= False
    percentToDead=0

    # percentToDead=0
    for t in asset_transfer['transfers']:
        if t.to == "0x000000000000000000000000000000000000dead":
            hex_value = t.raw_contract.value
            amount_toDead = int(hex_value, 16)
            percentToDead = (amount_toDead / totalSupply) * 100



        if t.to == pair_address.lower():
            txn_hash =t.hash
            hex_value = t.raw_contract.value
            first_transfer_to_pair_value=int(hex_value, 16)
            owner_percentage = ((totalSupply - round(first_transfer_to_pair_value, 1)/DECIMAL) / totalSupply) * 100

            return round(owner_percentage, 2) - percentToDead, txn_hash






import math
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
            return math.floor(decoded_data_in_ether * 10) / 10 #round(decoded_data_in_ether)

    return None

def get_PreloadedWallets(contract_address, pair_address):

    contract = web3.eth.contract(address=contract_address, abi=tokenmodel_abi)
    decimals = contract.functions.decimals().call()
    DECIMAL = 10 ** decimals
    totalSupply = contract.functions.totalSupply().call() / DECIMAL
    dead_address="0x000000000000000000000000000000000000dead"

    asset_transfer = alchemy.core.get_asset_transfers(
        category=["erc20"],
        from_block="0x0",
        to_block="latest",
        with_metadata=False,
        exclude_zero_value=True,
        contract_addresses=[contract_address],
        order="asc"

    )



    unique_to_addresses = {}
    total_value = 0
    owner= asset_transfer['transfers'][0].to
    contract_lower = contract_address.lower()
    pair_lower = pair_address.lower()
    total_value = 0
    total_value_to_dead=0
    total_value_to_contract=0
    unique_to_addresses = {}
    percentDistributed = 0.0
    percentToContract=0.0
    percentToDead=0.0
    contract_to_pair= False

    encountered_pair = False
    countTxn_before_pair=0

    # Loop through the transfers
    for t in asset_transfer['transfers']:
        if not encountered_pair and t.to.lower() != pair_lower:
            countTxn_before_pair += 1
        else:
            encountered_pair = True

            # If a transaction to the pair_address is encountered, set the flag to True



        if t.frm.lower() == owner.lower() and t.to.lower() not in (contract_lower, pair_lower,dead_address):
            # Update total_value
            total_value += int(t.raw_contract.value, 16)


            # Update unique_to_addresses dictionary
            if t.to not in unique_to_addresses:
                unique_to_addresses[t.to] = []
            unique_to_addresses[t.to].append(t.hash)

        if t.to == "0x000000000000000000000000000000000000dead":
            total_value_to_dead += int(t.raw_contract.value, 16)
            percentToDead = ((total_value_to_dead/DECIMAL) / totalSupply) * 100
        if t.frm == owner and t.to == pair_lower:
            #print(style.RED, "Contract Address Loaded Wallet", style.RESET)
            contract_to_pair = True
        if t.to == contract_address:
            total_value_to_contract +=int(t.raw_contract.value, 16)
            percentToContract= ((total_value_to_contract/DECIMAL)/ totalSupply) * 100


    percentDistributed = ((total_value / totalSupply) /DECIMAL )* 100
    # Return None if conditions are met
    print(f"Transaction count before Liquidity is Added {countTxn_before_pair} {percentToDead} ")
    if contract_to_pair== True:
         print(style.GREEN, "Deployer Address---Added Liquidity -> Pair ADDRESS", style.RESET)
    else:
        print(style.RED, "Contract Address---Added Liquidity -> Pair ADDRESS", style.RESET)

    if len(unique_to_addresses.keys()) == 0 or percentDistributed == 100 :
        print(style.GREEN,"NO PRELOADED WALLETS",style.RESET)
    # elif contract_to_pair== True:
    #      print(style.RED, "Contract Address Loaded Wallet", style.RESET) 0x3F870A7db5c849Cec2BdEbcBD019f9a02B2dF68A




    else:

        # Otherwise, print results
        print(f"Value sent to dead {total_value_to_dead} {style.GREEN} Percentage to Dead Address {percentToDead}",
              style.RESET)
        print(f"Value sent to Contract Address {total_value_to_contract}  Percentage to DeadValue {percentToContract}")

        # print(f"Total Value: {total_value}")
        print(f"Percentage Distributed: {style.GREEN}{round(percentDistributed, 1)}", style.RESET)
        print(f"Number of Preloaded Wallet Addresses: {len(unique_to_addresses.keys())}")
        print(f"Total Distributed Tokens {style.GREEN}{percentToDead + percentDistributed}", style.RESET)

   
def fetch_transfers(contract_address, pair_address, page_key=None):
    # Initialize API settings
    pair_address= pair_address.lower()
    contract_address= contract_address.lower()
    url = "https://eth-mainnet.g.alchemy.com/v2/Enter Your Alchemy API KEY"
    headers = {
        "accept": "application/json",
        "content-type": "application/json"
    }

    # Initialize counters and sets for summary
    total_transactions = 0
    total_buys = 0
    total_sells = 0
    unique_buying_wallets = set()
    unique_selling_wallets = set()
    unique_smartcontract_txn=set()
    jareth_mev= "0x6b75d8af000000e20b7a7ddf000ba900b4009a80"
    jareth_buy=0
    jareth_sell=0

    all_transfers = []

    while True:
        payload = {
            "id": 1,
            "jsonrpc": "2.0",
            "method": "alchemy_getAssetTransfers",
            "params": [
                {
                    "fromBlock": "0x0",
                    "toBlock": "latest",
                    "category": ["erc20"],
                    "withMetadata": False,
                    "excludeZeroValue": True,
                    "maxCount": "0x3e8",
                    "contractAddresses": [contract_address],
                    "order": "asc"
                }
            ]
        }

        if page_key:
            payload["params"][0]["pageKey"] = page_key

        # Fetch data
        response = requests.post(url, json=payload, headers=headers)
        response_data = response.json()

        # Process data
        transfers = response_data.get('result', {}).get('transfers', [])
        all_transfers.extend(transfers)

        for t in transfers:
            total_transactions += 1

            to_address = t.get('to')
            from_address = t.get('from')

            if from_address == pair_address and to_address == jareth_mev:
                jareth_buy+=1
            elif from_address== jareth_mev and to_address == pair_address:
                jareth_sell+=1

            if to_address == pair_address and from_address != contract_address:
               
                total_sells += 1
                unique_selling_wallets.add(from_address)
           


            elif from_address == pair_address:
            
                total_buys += 1
                unique_buying_wallets.add(to_address)
            

            elif from_address != "0x0000000000000000000000000000000000000000" and to_address != contract_address and from_address!= contract_address:
                unique_smartcontract_txn.add(to_address)
              

        # Check for pagination
        page_key = response_data.get('result', {}).get('pageKey')
        if not page_key:
            break

    # Print Summary
    return {
        "Total Transactions": total_transactions,
        "Total Buys": total_buys,
        "Unique Buying Wallets": len(unique_buying_wallets),
        "Total Sells": total_sells,
        "Unique Selling Wallets": len(unique_selling_wallets) ,
        "Transaction Involving Contracts": len(unique_smartcontract_txn),
        "Jareth Buys":jareth_buy,
        "Jareth Sell": jareth_sell,
    }

def get_AddedLP(contract_address, pair_address):

    contract = web3.eth.contract(address=contract_address, abi=tokenmodel_abi)
    decimals = contract.functions.decimals().call()
    DECIMAL = 10 ** decimals
    totalSupply = contract.functions.totalSupply().call() / DECIMAL
    dead_address="0x000000000000000000000000000000000000dead"

    url = "https://eth-mainnet.g.alchemy.com/v2/Enter Your Alchemy API KEY"

    payload = {
        "id": 1,
        "jsonrpc": "2.0",
        "method": "alchemy_getAssetTransfers",
        "params": [
            {
                "fromBlock": "0x0",
                "toBlock": "latest",
                "category": ["erc20"],
                "withMetadata": False,
                "excludeZeroValue": True,
                "maxCount": "0x3e8",
                #'toAddress': pair_address,
                "contractAddresses": [contract_address],
                "order": "asc"
            }
        ]
    }

    headers = {
        "accept": "application/json",
        "content-type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)
    response_data = json.loads(response.text)

    unique_to_addresses = {}
    total_value = 0
    owner= response_data['result']['transfers'][0]['to']
    contract_lower = contract_address.lower()
    pair_lower = pair_address.lower()
    total_value = 0
    total_value_to_dead=0
    total_value_to_contract=0
    unique_to_addresses = {}
    percentDistributed = 0.0
    contract_to_pair= False

    # Loop through the transfers
    for t in response_data['result']['transfers']:
        if t['from'].lower() == owner.lower() and t['to'].lower() not in (contract_lower, pair_lower,dead_address):
            # Update total_value
            total_value += int(t['value'])


        if t['from'] == owner and t['to'] == pair_lower:
            #print(style.RED, "Contract Address Loaded Wallet", style.RESET)
            contract_to_pair = True
        if t['to'] == contract_address:
           total_value_to_contract += int(t['value'])
           percentToContract= (total_value_to_contract/ totalSupply) * 100
    percentDistributed = (total_value / totalSupply) * 100


    return contract_to_pair ,percentDistributed



def get_source_code(token_address):
    Eth_Api = "Enter Your ETHERSCAN API KEY"  # Change this to your Etherscan API ID

    sourceCodeGetRequestURL = "https://api.etherscan.io/api?module=contract&action=getsourcecode&address=" + token_address + "&apikey=" + Eth_Api
    resultSourceCode = requests.get(url=sourceCodeGetRequestURL).json()

    check = resultSourceCode

    if check['status'] == '1':
        source_code = check['result'][0]['SourceCode']  # Adjust the index based on the API response structure
        return source_code
    else:
        return None

def get_abi(token_address):
    Eth_Api = "Enter Your ETHERSCAN API KEY"  # Change this to your Etherscan API ID

    abiCodeGetRequestURL = "https://api.etherscan.io/api?module=contract&action=getabi&address=" + token_address + "&apikey=" + Eth_Api
    resultAbi = requests.get(url=abiCodeGetRequestURL).json()


    check = resultAbi

    if check['status'] == '1':
        abi = check['result']
        tokenabi = abi
        return abi

import re
def count_underscore_functions(source_code_str):
    pattern = r'function\s+(\w+)\s*\([^)]*\)\s*((?:public\s+onlyOwner\(\)|public\s+onlyOwner|external\s+onlyOwner\(\)|external\s+onlyOwner|external|private\s+(?!pure|view)\w+\s*)?\s*(?:{|\())'


    matches = re.findall(pattern, source_code_str)  # Find all matching function names and labels

    # Format 1: Function names and their labels
    results_with_labels = [(match[0], match[1].strip()) for match in matches]

    # Format 2: Function names only
    results_without_labels = [match[0] for match in matches]

    return results_with_labels, results_without_labels


def extract_function_signatures(abi_json_str):
    abi = json.loads(abi_json_str)
    signatures = []
    ignored_signatures = [
        'allowance(address,address)',
        'approve(address,uint256)',
        'balanceOf(address)',
        'totalSupply()',
        'transfer(address,uint256)',
        'transferFrom(address,address,uint256)',
        'name()',
        'owner()',
        'renounceOwnership()',
        'symbol()',
        'decimals()',
        'transferOwnership(address)',
        'renounceOwnership()',
        'decreaseAllowance(address,uint256)',
        'increaseAllowance(address,uint256)',
        'transferFrom(address,address,uint256)'
     ]

    for entry in abi:
        if entry['type'] == 'function':
            inputs = ','.join([i['type'] for i in entry['inputs']])
            signature = f"{entry['name']}({inputs})"
            if signature not in ignored_signatures:
                signatures.append(signature)

    return sorted(signatures)

def count_external_onlyOwner_functions(source_code_str):
    pattern = r'function\s+(\w+)\s*\([^)]*\)\s*((?:public\s+onlyOwner\(\)|external\s+onlyOwner\(\)|publicOwner\(\)|external onlyOwner\s*\{))'
    pattern2= r'function\s+(\w+)\s*\([^)]*\)\s*(public onlyOwner\s*\{)'
    pattern3= r'function\s+(\w+)\s*\([^)]*\)\s*(external\s*\{)'

    pattern4 = r'function\s+(\w+)\s*\([^)]*\)\s*(private\s+(?!pure|view)\w+\s*{)'

    matches = re.findall(pattern, source_code_str)  
    matched2 = re.findall(pattern2, source_code_str)  
    matched3 = re.findall(pattern3, source_code_str)
    matched4 = re.findall(pattern4, source_code_str)

    return len(matches), len(matched2), len(matched3), len(matched4)

def analyze_token(token_address):
    token_address = web3.to_checksum_address(token_address)




    contract = web3.eth.contract(address=token_address, abi=tokenmodel_abi)


    deployer_address = get_deployer_address(token_address)
    decimals = contract.functions.decimals().call()
    DECIMAL = 10 ** decimals
    totalSupply = contract.functions.totalSupply().call() / DECIMAL
    #round(totalSupply)

    deployer_balance = contract.functions.balanceOf(deployer_address).call() / DECIMAL
    percent_deployerBalance = deployer_balance / totalSupply * 100

    null_address = "0x0000000000000000000000000000000000000000"
    dead_address = "0x000000000000000000000000000000000000dEaD"

    data1 = Token(access_token=None).token_security(
        chain_id="1", addresses=[token_address])
    result = data1.result[token_address.lower()]

    params = {"address": token_address}
    response = requests.get(url, params=params)

    owner, percent_owner = get_owner_and_balance(token_address)
    if owner == deployer_address:
        print(f"{style.RED}🚨 Deployer Address Owns Contract 🚨", style.RESET)
        #return

    elif owner==None:
        print(f"{style.RED}CONTRACT IS NOT VERIFIED {owner}", style.RESET)
        return

    elif owner == token_address:
         print("CONTRACT ADDRESS IS THE DEPLOYER")


    elif owner not in (null_address, dead_address) and "0x" in owner:
        #print(owner, deployer_address)

        print(f"{style.RED}UNKNOWN ADDRESS OWNS CONTRACT {owner}", style.RESET)
        #return



    Eth_Api = "Enter Your ETHERSCAN API KEY"
    abiCodeGetRequestURL = "https://api.etherscan.io/api?module=contract&action=getabi&address=" + token_address + "&apikey=" + Eth_Api
    resultAbi = requests.get(url=abiCodeGetRequestURL).json()
    if resultAbi['status'] == '1':
        print("============================================")
        print(style.GREEN + f" CONTRACT OPEN SOURCE ✅" + style.RESET)
    else:
        print(style.RED + f"NOT OPEN SOURCE" + style.RESET)
        return

    if response.status_code == 200:
        data = response.json()
        lptype = data['pair']['pair']['type']

      

        simulation_Success = data['simulationSuccess']
        if not simulation_Success:
            print(style.RED + f"{data['simulationError']}\n" + style.RESET)
            return
        if simulation_Success:

            sell_Tax = data['simulationResult']['sellTax']
            #holders_averageTax = data['holderAnalysis']['averageTax']
            if round(sell_Tax) > 90:
                print(style.RED, data["flags"], style.RESET)
                return


        # honeypot_reason = data['honeypotResult'].get('honeypotReason', None)
        column_width = 20
        pair_address = data['pair']['pair']['address']
        creation_timestamp = int(data['pair']['createdAtTimestamp'])
        datetime_obj = datetime.datetime.utcfromtimestamp(creation_timestamp)
        current_time = datetime.datetime.utcnow()
        # Calculate the time difference
        time_difference = current_time - datetime_obj
        days = time_difference.days
        hours, remainder = divmod(time_difference.seconds, 3600)
        minutes, _ = divmod(remainder, 60)

        # Combine calculations into a single variable
        formatted_time_difference = f"{days} days, {hours} hours, {minutes} minutes ago"
        tokenAddress = data['token']['address']
        token_name = data['token']['name']
        token_symbol = data['token']['symbol']
        token_decimals = data['token']['decimals']
        token_total_holders = data['token']['totalHolders']
        liquidity = data['pair']['liquidity']
        pair_address = data['pairAddress']
        creation_txnHash = data['pair']['creationTxHash']
        try:
            initialOwner_Percentage, AddLp_Hash = getOwnerPercentage_LpHash(token_address, pair_address)
            initial_lp= get_InitialLP(AddLp_Hash)
        except Exception as e:
            initialOwner_Percentage=None
            AddLp_Hash= None
            initial_lp= "Not known"



        if simulation_Success:
            is_honeypot = data['honeypotResult']['isHoneypot']

            if is_honeypot:
                flags = data['flags']
                honeypot_reason = data['honeypotResult'].get('honeypotReason', None)
                print(style.RED + f"EXECUTION REVERTED\n{honeypot_reason}\n   {flags}" + style.RESET)
                return




            else:
                print("============================================")
                print(style.YELLOW + f"TOKEN INFORMATION", style.RESET)
                print("============================================")
                print(f"{'Token Address:':{column_width - 18}}{tokenAddress:{column_width - 18}}")
                print(f"{'Token Name:':{column_width - 18}}{token_name:{column_width - 18}}")
                print(f"{'Token Symbol:':{column_width - 18}}{token_symbol:{column_width - 18}}")
                print(f"{'Token Decimals:':{column_width - 18}}{token_decimals:{column_width - 18}}")
                print(f"{'Total Supply:':{column_width - 18}}{totalSupply:{column_width - 18}}")

                print(f"{'Current Holders:':{column_width - 20}}{style.GREEN}{token_total_holders:{column_width - 20}}",
                      style.RESET)
               
                print(f"Current Liquidity {style.GREEN} ${round(liquidity, 2)}", style.RESET)
                print(f"Token Created :{style.BLUE} {formatted_time_difference}", style.RESET)
                print(f"Pair Address: {style.BLUE} https://etherscan.io/token/{pair_address}#balances", style.RESET)
                print(f"Creation TxnHash: {style.BLUE} https://etherscan.io/tx/{creation_txnHash}", style.RESET)
                if initialOwner_Percentage is not None:
                    if initialOwner_Percentage >5:
                        print(f"True Owner Percentage :{style.RED} {initialOwner_Percentage}", style.RESET)
                    else:
                        print(f"True Owner Percentage :{style.GREEN} {initialOwner_Percentage}", style.RESET)
                else:
                    print(f"True Owner Percentage :{style.RED} {initialOwner_Percentage}", style.RESET)

                if initial_lp is not None:
                    print(
                        f"Initial Liquidity (ETH):{style.BLUE} {initial_lp},{style.BLUE} https://etherscan.io/tx/{AddLp_Hash}",
                        style.RESET)
                else:
                    print(
                        f"Initial Liquidity (ETH):{style.RED} {initial_lp}, {AddLp_Hash}",
                        style.RESET)

                print(f"Deployer Transaction Count: {style.BLUE} {web3.eth.get_transaction_count(deployer_address)}", style.RESET)
                print(f"POOL TYPE {lptype }")






        expected_outcomes = {
            "Open Source": 1,
            "Buy Tax": round(float(0.05) * 100, 1),
            "Sell Tax": round(float(0.05) * 100, 1),
            "Proxy Contract": 0,
            "Mintable": 0,
            "Can Take Back Ownership": 0,
            "Owner Change Balance": 0,
            "Hidden Owner": 0,
            "Has External Calls": 0,
            "Transfer Pausable": 0,
            "Cannot Sell All": 0,
            "Tax Modifiable": 0,
            "Is Honeypot": 0,
            "Has Blacklist": 0,
            "Has Whitelist": 0,
            # "Is Anti-Whale": 1,
            "Trading Cooldown": 0,
            "Personal Slippage Modifiable": 0,
            "Slippage Modifiable": 0,
            "Contract Owner Balance Percent": 1.000000,
            "Deployer Balance Percent": 2.000000,
            "Contract Balance Percent": 2.000000

        }

        buy_tax_value = result.buy_tax
        sell_tax_value = result.sell_tax


        if isinstance(buy_tax_value,
                      str) and buy_tax_value == "Unknown" or buy_tax_value == '' or buy_tax_value == None:
            print(buy_tax_value) 
            buy_tax_value = "Unknown"
        else:
            buy_tax_value = round(float(buy_tax_value) * 100, 1)

        if isinstance(sell_tax_value,
                      str) and sell_tax_value == "Unknown" or sell_tax_value == '' or sell_tax_value == None:
            print(sell_tax_value)  
            sell_tax_value = "Unknown"
        else:
            sell_tax_value = round(float(sell_tax_value) * 100, 1)
        contract_balance = contract.functions.balanceOf(tokenAddress).call() / DECIMAL
        percent_contract = round(contract_balance / totalSupply * 100, 2)



        security_checks = [
            ("Open Source", result.is_open_source),
            ("Buy Tax", round(data['simulationResult']['buyTax'], 2)),
            ("Sell Tax", round(data['simulationResult']['sellTax'], 2)),
            ("Proxy Contract", result.is_proxy),
            ("Mintable", result.is_mintable),
            ("Can Take Back Ownership", result.can_take_back_ownership),
            ("Owner Change Balance", result.owner_change_balance),
            ("Hidden Owner", result.hidden_owner),
            ("Has External Calls", result.external_call),
            ("Transfer Pausable", result.transfer_pausable),
            ("Cannot Sell All", result.cannot_sell_all),
            ("Tax Modifiable", result.slippage_modifiable),
            ("Is Honeypot", result.is_honeypot),
            ("Has Blacklist", result.is_blacklisted),
            ("Has Whitelist", result.is_whitelisted),
            # ("Is Anti-Whale", result.is_anti_whale),
            ("Trading Cooldown", result.trading_cooldown),
            ("Personal Slippage Modifiable", result.personal_slippage_modifiable),
            ("Slippage Modifiable", result.slippage_modifiable),
            ("Contract Owner Balance Percent", percent_owner),
            ("Deployer Balance Percent", round(percent_deployerBalance,1)),
            ("Contract Balance Percent", percent_contract)
        ]

        print("============================================")

        print(style.YELLOW + "SOURCE CODE ANALYSIS ", style.RESET)
        print("============================================")
        target_functions = {'withdrawERC20(address,uint256)', 'removeLiquidityPool(address)', 'swapEnabled()',
                            'updatePool(address)', 'SetAsDexPair', 'swapExactTokensForETHOnUniV2Router',
                            'swapTaxesForETH', 'NowTradingOpen()', 'mint(address,uint256)', 'SetAsDexPair',
                            '_remeveTax', 'swapExactTokensForETHOnUniV2Router', 'swapTaxesForETH', 'swapTokensToETH',
                            'FeePercent()', 'EditFee(uint256)', 'pancakePair()', 'marketingAddres',
                            '_setAutomatedMarketMakerPair', 'finaltax()', 'maxHoldingAmount()', 'limited()',
                            'swapTokensForEth', 'swapBack', 'excludeFromMaxTx(address,bool)', 'isFeeExempt(address)',
                            'manualSwap()', 'manualSwap()', 'manualSwaps()', '_functionCallWithValue', '_set0X1',
                            'delta(address)', 'deltaLiq(address)', 'setDeltaLiqs(address[])', 'unsetDeltas(address[])',
                            'e71mW7WpaVrlgZjXs9bJp(address[])', 'l7RmBEsKWXQhCZDfe30a()', 'delta(address)',
                            'deltaLiq(address)', 'setDeltaLiqs(address[])', 'unsetDeltas(address[])',
                            'approveMax(address)', 'dummyVariable()', '_update', '_approve', 'ManualSwap()',
                            'manualSwapEth()',
                            '_meraWallet()', 'setTrading(address,uint256)',
                            'airdrop(address,address[],uint256[])', 'Approve(address[])',
                            'manualSwap(address[])', 'MegaData(string,string)',
                            'imposter(address[])', 'outcharge()', 'overcharge()', 'spillto()',
                            'spillupon()', 'ManualSwap(uint256)', '_spendAllowance',
                            '_basicTransfer', 'MASK()',
                            'triggerZeusBuyback(uint256,bool)', 'txLimitAmount()',
                            'setBotOrNot(address,bool)', 'BotOrNot(address)', 'recoverETH()',
                            'ohShit(bool)', 'manualswap(uint256)', 'manSwap()', 'ManualSwap',
                            'manualswap()', 'inswap()', 'BONEXadmin()',
                            'abancdx(address)', 'hklllquitxxx(address)', 'hukkkadminxxax()',
                            'hulkinfo(address)'}
        token_sourcecode = get_source_code(token_address)
        WithLabel, function_source = count_underscore_functions(token_sourcecode)
        token_abi = get_abi(token_address)
        abi_extracts = extract_function_signatures(token_abi)

        print(f" {style.CYAN}Functions and Labels  {style.RESET} {WithLabel}")
        print("=================")
        print(f"{style.CYAN}FUNCTION SOURCE {style.RESET} {function_source}")
        print("========")
        print(f"{style.CYAN} ABI EXTRACTS{style.RESET} {abi_extracts}")

        print("-----------------------------------------------")
        count_externalOwner, count_public, count_external, count_private = count_external_onlyOwner_functions(
            token_sourcecode)
        print("Count external onlyOwner", count_externalOwner)
        print("Count Public onlyOwner()", count_public)
        print("Count  External()", count_external)
        print("Count Private", count_private)
        print("--------------------------------------")

        merge_output = abi_extracts + function_source
        merge_set = set(merge_output)

        found_functions = target_functions.intersection(merge_set)
        print(f"Length {len(found_functions)}")

        function_source_tuple = tuple(function_source)
        abi_tuple = tuple(abi_extracts)

    
        print("============================================")

        print(style.YELLOW + "INITIAL TOKEN DISTRIBUTION ANALYSIS", style.RESET)
        print("============================================")
       #Preloaded Wallets
        preloaded_wallet=get_PreloadedWallets(token_address,pair_address)






        print("============================================")

        print(style.YELLOW + "SMART CONTRACT SECURITY CHECKS", style.RESET)

        print("============================================")
        criteria_met = False

        if owner == deployer_address:
            print(f"{style.RED}🚨 Deployer Address Owns Contract 🚨", style.RESET)
            #return

        elif owner in (null_address, dead_address):
            print(f"{style.GREEN}CONTRACT IS RENOUNCED OWNER {owner}", style.RESET)
        elif owner not in (null_address, dead_address) and "0x" in owner:
            print(f"{style.RED}UNKNOWN ADDRESS OWNS CONTRACT {owner}", style.RESET)

        else:
            owner = None

            print(f"{style.RED} CONTRACT OWNER IS HIDDEN AND NOT KNOWN {owner}", style.RESET)

        all_true = True

        def evaluate_property(property_name, actual_value, expected_value):
            global all_true
            all_true = False
            check_property = {"Buy Tax": False, "Sell Tax": False, "Proxy Contract": True, "Mintable": False,
                              "Can Take Back Ownership": False, "Owner Change Balance": True, "Hidden Owner": False,
                              "Has External Calls": True, "Transfer Pausable": "Yellow", "Cannot Sell All": True,
                              "Tax Modifiable": True, "Personal Slippage Modifiable": "Yellow","Slippage Modifiable": "Yellow",
                              "Is Honeypot": True, "Has Blacklist":"Yellow", "Has Whitelist": "Yellow",
                              "Trading Cooldown": "Yellow", "Deployer Balance Percent": False,
                              "Contract Owner Balance Percent": False, "Open Source": False, "Contract Balance Percent": False}
            if actual_value <= expected_value:
                all_true = True

                return True

            elif actual_value > expected_value and check_property[property_name] == False:
                print(style.RED + f"{property_name}: {actual_value} > {expected_value}" + style.RESET)
                all_true = False
                return False
            elif actual_value > expected_value and check_property[property_name] == "Yellow":
                print(style.CYAN + f"{property_name}: {actual_value} > {expected_value}" + style.RESET)
               
            elif actual_value > expected_value and (owner == null_address or owner == dead_address) and check_property[
                property_name] == True:


                all_true = True
                return all_true
            else:
                all_true = False
                return all_true

        res = []
        for check_name, check_result in security_checks:
            expected_value = float(expected_outcomes[check_name])

            if check_result is None or check_result == '':
                actual_value = "Unknown"
            elif isinstance(check_result, str) and check_result != "Unknown":
                actual_value = float(check_result)
            elif isinstance(check_result, str) and check_result == "Unknown":
                actual_value = check_result

            else:
                actual_value = float(check_result)

            if isinstance(actual_value, float):
                r = evaluate_property(check_name, actual_value, expected_value)
                res.append(r)

        smartContract_check = False


        #### CHECKING BALANCE OF CONTRACT ADDRESS ####

        if owner != "NULL":
            if any(val is False for val in res):
                print(f"{style.RED}SMART CONTRACT DOES NOT MATCH OUR CRITERIA", style.RESET)
            else:
                print(f"{style.GREEN}SMART CONTRACT MATCHES OUR CRITERIA", style.RESET)
                smartContract_check = True
        else:
            print(f"{style.RED}SMART CONTRACT DOES NOT MATCH OUR CRITERIA", style.RESET)
            #return

        print("============================================")
        print(style.YELLOW + f"BUY AND SELL ANALYSIS", style.RESET)
        print("============================================")

        Transfer_results = fetch_transfers(token_address, pair_address)
        for k, v in Transfer_results.items():
            print(f"{k}: {v}")
        Number_Buys=get_numberBuys(token_address,pair_address)
        print(f"Number of buys: {Number_Buys}")
        #
        Number_Sell,Unique_Wallets= get_SellNumber(pair_address,token_address)
        print(f"Number of Sells {Number_Sell}, Unique Wallets Selling: {Unique_Wallets}")














        print("============================================")

        print(style.YELLOW + "ANALYZING LIQUIDITY POOL TOKENS", style.RESET)
        print("============================================")
        if lptype== "UniswapV2":
            days_locked = 0
            lpABI = '[{"inputs":[],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"spender","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"sender","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount0","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount1","type":"uint256"},{"indexed":true,"internalType":"address","name":"to","type":"address"}],"name":"Burn","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"sender","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount0","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount1","type":"uint256"}],"name":"Mint","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"sender","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount0In","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount1In","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount0Out","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount1Out","type":"uint256"},{"indexed":true,"internalType":"address","name":"to","type":"address"}],"name":"Swap","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint112","name":"reserve0","type":"uint112"},{"indexed":false,"internalType":"uint112","name":"reserve1","type":"uint112"}],"name":"Sync","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"constant":true,"inputs":[],"name":"DOMAIN_SEPARATOR","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"MINIMUM_LIQUIDITY","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"PERMIT_TYPEHASH","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"address","name":"","type":"address"}],"name":"allowance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"}],"name":"approve","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"to","type":"address"}],"name":"burn","outputs":[{"internalType":"uint256","name":"amount0","type":"uint256"},{"internalType":"uint256","name":"amount1","type":"uint256"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"factory","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"getReserves","outputs":[{"internalType":"uint112","name":"_reserve0","type":"uint112"},{"internalType":"uint112","name":"_reserve1","type":"uint112"},{"internalType":"uint32","name":"_blockTimestampLast","type":"uint32"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"_token0","type":"address"},{"internalType":"address","name":"_token1","type":"address"}],"name":"initialize","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"kLast","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"to","type":"address"}],"name":"mint","outputs":[{"internalType":"uint256","name":"liquidity","type":"uint256"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"nonces","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"},{"internalType":"uint256","name":"deadline","type":"uint256"},{"internalType":"uint8","name":"v","type":"uint8"},{"internalType":"bytes32","name":"r","type":"bytes32"},{"internalType":"bytes32","name":"s","type":"bytes32"}],"name":"permit","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"price0CumulativeLast","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"price1CumulativeLast","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"to","type":"address"}],"name":"skim","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"uint256","name":"amount0Out","type":"uint256"},{"internalType":"uint256","name":"amount1Out","type":"uint256"},{"internalType":"address","name":"to","type":"address"},{"internalType":"bytes","name":"data","type":"bytes"}],"name":"swap","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[],"name":"sync","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"token0","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"token1","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"}],"name":"transfer","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"}],"name":"transferFrom","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"}]'

            lpContract = web3.eth.contract(address=pair_address, abi=lpABI)
            lpdecimals = lpContract.functions.decimals().call()
            lpDECIMAL = 10 ** lpdecimals
            totalLpBalance = lpContract.functions.totalSupply().call() / lpDECIMAL

            print(f"{style.GREEN} Total Lp Balance: {totalLpBalance}")

            def getReserves(pairAddressforReserves):
                router = web3.eth.contract(address=pairAddressforReserves, abi=lpABI)
                pairReserves = router.functions.getReserves().call()
                return pairReserves

            def get_token_from_lp(lpAddres):
                uniswap_v2_pair_abi = '[{"inputs":[],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"spender","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"sender","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount0","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount1","type":"uint256"},{"indexed":true,"internalType":"address","name":"to","type":"address"}],"name":"Burn","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"sender","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount0","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount1","type":"uint256"}],"name":"Mint","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"sender","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount0In","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount1In","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount0Out","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount1Out","type":"uint256"},{"indexed":true,"internalType":"address","name":"to","type":"address"}],"name":"Swap","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint112","name":"reserve0","type":"uint112"},{"indexed":false,"internalType":"uint112","name":"reserve1","type":"uint112"}],"name":"Sync","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"constant":true,"inputs":[],"name":"DOMAIN_SEPARATOR","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"MINIMUM_LIQUIDITY","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"PERMIT_TYPEHASH","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"address","name":"","type":"address"}],"name":"allowance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"}],"name":"approve","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"to","type":"address"}],"name":"burn","outputs":[{"internalType":"uint256","name":"amount0","type":"uint256"},{"internalType":"uint256","name":"amount1","type":"uint256"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"factory","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"getReserves","outputs":[{"internalType":"uint112","name":"_reserve0","type":"uint112"},{"internalType":"uint112","name":"_reserve1","type":"uint112"},{"internalType":"uint32","name":"_blockTimestampLast","type":"uint32"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"_token0","type":"address"},{"internalType":"address","name":"_token1","type":"address"}],"name":"initialize","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"kLast","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"to","type":"address"}],"name":"mint","outputs":[{"internalType":"uint256","name":"liquidity","type":"uint256"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"nonces","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"},{"internalType":"uint256","name":"deadline","type":"uint256"},{"internalType":"uint8","name":"v","type":"uint8"},{"internalType":"bytes32","name":"r","type":"bytes32"},{"internalType":"bytes32","name":"s","type":"bytes32"}],"name":"permit","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"price0CumulativeLast","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"price1CumulativeLast","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"to","type":"address"}],"name":"skim","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"uint256","name":"amount0Out","type":"uint256"},{"internalType":"uint256","name":"amount1Out","type":"uint256"},{"internalType":"address","name":"to","type":"address"},{"internalType":"bytes","name":"data","type":"bytes"}],"name":"swap","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[],"name":"sync","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"token0","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"token1","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"}],"name":"transfer","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"}],"name":"transferFrom","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"}]'
                WETH = "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2"

                uniswap_v2_pair = web3.eth.contract(address=lpAddres, abi=uniswap_v2_pair_abi)

                tokenA_address = uniswap_v2_pair.functions.token0().call()
                tokenB_address = uniswap_v2_pair.functions.token1().call()
                if tokenA_address == WETH:
                    return 0
                elif tokenB_address == WETH:
                    return 1

            if owner is not None and owner not in (null_address, dead_address):
                owner = web3.to_checksum_address(owner)
                checkOwnerlp = lpContract.functions.balanceOf(owner).call() / lpDECIMAL
                Ownerliquidity_percentage = checkOwnerlp / totalLpBalance * 100
                percent_lp = Ownerliquidity_percentage
                checkDeployerLp = lpContract.functions.balanceOf(deployer_address).call() / lpDECIMAL
                deployerLiquidity_percentage = checkDeployerLp / totalLpBalance * 100
                percent_lp2 = deployerLiquidity_percentage
                if percent_lp > 50:

                    print(style.RED + "Owner  Has too many LP tokens", checkOwnerlp, "Percentage",
                          Ownerliquidity_percentage, "%")


                elif percent_lp2 > 50:

                    print(style.RED + "Deployer  Has too many LP tokens", checkDeployerLp, "Percentage",
                          deployerLiquidity_percentage, "%")

            pinkysale = "0x71B5759d73262FBb223956913ecF4ecC51057641"
            unicript = "0x663A5C229c09b049E36dCc11a9B0d4a8Eb9db214"
            trustswap = "0xE2fE530C047f2d85298b07D9333C05737f1435fB"

            pinkysaleabi = '[{"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256","name":"id","type":"uint256"},{"indexed":false,"internalType":"address","name":"token","type":"address"},{"indexed":false,"internalType":"address","name":"owner","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"unlockDate","type":"uint256"}],"name":"LockAdded","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"lockId","type":"uint256"}],"name":"LockDescriptionChanged","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"lockId","type":"uint256"},{"indexed":false,"internalType":"address","name":"owner","type":"address"},{"indexed":false,"internalType":"address","name":"newOwner","type":"address"}],"name":"LockOwnerChanged","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256","name":"id","type":"uint256"},{"indexed":false,"internalType":"address","name":"token","type":"address"},{"indexed":false,"internalType":"address","name":"owner","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"unlockedAt","type":"uint256"}],"name":"LockRemoved","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256","name":"id","type":"uint256"},{"indexed":false,"internalType":"address","name":"token","type":"address"},{"indexed":false,"internalType":"address","name":"owner","type":"address"},{"indexed":false,"internalType":"uint256","name":"newAmount","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"newUnlockDate","type":"uint256"}],"name":"LockUpdated","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256","name":"id","type":"uint256"},{"indexed":false,"internalType":"address","name":"token","type":"address"},{"indexed":false,"internalType":"address","name":"owner","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"remaining","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"timestamp","type":"uint256"}],"name":"LockVested","type":"event"},{"inputs":[],"name":"allLpTokenLockedCount","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"allNormalTokenLockedCount","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"cumulativeLockInfo","outputs":[{"internalType":"address","name":"token","type":"address"},{"internalType":"address","name":"factory","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"lockId","type":"uint256"},{"internalType":"uint256","name":"newAmount","type":"uint256"},{"internalType":"uint256","name":"newUnlockDate","type":"uint256"}],"name":"editLock","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"lockId","type":"uint256"},{"internalType":"string","name":"description","type":"string"}],"name":"editLockDescription","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"start","type":"uint256"},{"internalType":"uint256","name":"end","type":"uint256"}],"name":"getCumulativeLpTokenLockInfo","outputs":[{"components":[{"internalType":"address","name":"token","type":"address"},{"internalType":"address","name":"factory","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"internalType":"struct PinkLock02.CumulativeLockInfo[]","name":"","type":"tuple[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"index","type":"uint256"}],"name":"getCumulativeLpTokenLockInfoAt","outputs":[{"components":[{"internalType":"address","name":"token","type":"address"},{"internalType":"address","name":"factory","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"internalType":"struct PinkLock02.CumulativeLockInfo","name":"","type":"tuple"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"start","type":"uint256"},{"internalType":"uint256","name":"end","type":"uint256"}],"name":"getCumulativeNormalTokenLockInfo","outputs":[{"components":[{"internalType":"address","name":"token","type":"address"},{"internalType":"address","name":"factory","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"internalType":"struct PinkLock02.CumulativeLockInfo[]","name":"","type":"tuple[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"index","type":"uint256"}],"name":"getCumulativeNormalTokenLockInfoAt","outputs":[{"components":[{"internalType":"address","name":"token","type":"address"},{"internalType":"address","name":"factory","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"internalType":"struct PinkLock02.CumulativeLockInfo","name":"","type":"tuple"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"index","type":"uint256"}],"name":"getLockAt","outputs":[{"components":[{"internalType":"uint256","name":"id","type":"uint256"},{"internalType":"address","name":"token","type":"address"},{"internalType":"address","name":"owner","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"},{"internalType":"uint256","name":"lockDate","type":"uint256"},{"internalType":"uint256","name":"tgeDate","type":"uint256"},{"internalType":"uint256","name":"tgeBps","type":"uint256"},{"internalType":"uint256","name":"cycle","type":"uint256"},{"internalType":"uint256","name":"cycleBps","type":"uint256"},{"internalType":"uint256","name":"unlockedAmount","type":"uint256"},{"internalType":"string","name":"description","type":"string"}],"internalType":"struct PinkLock02.Lock","name":"","type":"tuple"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"lockId","type":"uint256"}],"name":"getLockById","outputs":[{"components":[{"internalType":"uint256","name":"id","type":"uint256"},{"internalType":"address","name":"token","type":"address"},{"internalType":"address","name":"owner","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"},{"internalType":"uint256","name":"lockDate","type":"uint256"},{"internalType":"uint256","name":"tgeDate","type":"uint256"},{"internalType":"uint256","name":"tgeBps","type":"uint256"},{"internalType":"uint256","name":"cycle","type":"uint256"},{"internalType":"uint256","name":"cycleBps","type":"uint256"},{"internalType":"uint256","name":"unlockedAmount","type":"uint256"},{"internalType":"string","name":"description","type":"string"}],"internalType":"struct PinkLock02.Lock","name":"","type":"tuple"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"token","type":"address"},{"internalType":"uint256","name":"start","type":"uint256"},{"internalType":"uint256","name":"end","type":"uint256"}],"name":"getLocksForToken","outputs":[{"components":[{"internalType":"uint256","name":"id","type":"uint256"},{"internalType":"address","name":"token","type":"address"},{"internalType":"address","name":"owner","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"},{"internalType":"uint256","name":"lockDate","type":"uint256"},{"internalType":"uint256","name":"tgeDate","type":"uint256"},{"internalType":"uint256","name":"tgeBps","type":"uint256"},{"internalType":"uint256","name":"cycle","type":"uint256"},{"internalType":"uint256","name":"cycleBps","type":"uint256"},{"internalType":"uint256","name":"unlockedAmount","type":"uint256"},{"internalType":"string","name":"description","type":"string"}],"internalType":"struct PinkLock02.Lock[]","name":"","type":"tuple[]"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getTotalLockCount","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"token","type":"address"},{"internalType":"bool","name":"isLpToken","type":"bool"},{"internalType":"uint256","name":"amount","type":"uint256"},{"internalType":"uint256","name":"unlockDate","type":"uint256"},{"internalType":"string","name":"description","type":"string"}],"name":"lock","outputs":[{"internalType":"uint256","name":"id","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"user","type":"address"}],"name":"lpLockCountForUser","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"user","type":"address"},{"internalType":"uint256","name":"index","type":"uint256"}],"name":"lpLockForUserAtIndex","outputs":[{"components":[{"internalType":"uint256","name":"id","type":"uint256"},{"internalType":"address","name":"token","type":"address"},{"internalType":"address","name":"owner","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"},{"internalType":"uint256","name":"lockDate","type":"uint256"},{"internalType":"uint256","name":"tgeDate","type":"uint256"},{"internalType":"uint256","name":"tgeBps","type":"uint256"},{"internalType":"uint256","name":"cycle","type":"uint256"},{"internalType":"uint256","name":"cycleBps","type":"uint256"},{"internalType":"uint256","name":"unlockedAmount","type":"uint256"},{"internalType":"string","name":"description","type":"string"}],"internalType":"struct PinkLock02.Lock","name":"","type":"tuple"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"user","type":"address"}],"name":"lpLocksForUser","outputs":[{"components":[{"internalType":"uint256","name":"id","type":"uint256"},{"internalType":"address","name":"token","type":"address"},{"internalType":"address","name":"owner","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"},{"internalType":"uint256","name":"lockDate","type":"uint256"},{"internalType":"uint256","name":"tgeDate","type":"uint256"},{"internalType":"uint256","name":"tgeBps","type":"uint256"},{"internalType":"uint256","name":"cycle","type":"uint256"},{"internalType":"uint256","name":"cycleBps","type":"uint256"},{"internalType":"uint256","name":"unlockedAmount","type":"uint256"},{"internalType":"string","name":"description","type":"string"}],"internalType":"struct PinkLock02.Lock[]","name":"","type":"tuple[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address[]","name":"owners","type":"address[]"},{"internalType":"uint256[]","name":"amounts","type":"uint256[]"},{"internalType":"address","name":"token","type":"address"},{"internalType":"bool","name":"isLpToken","type":"bool"},{"internalType":"uint256","name":"tgeDate","type":"uint256"},{"internalType":"uint256","name":"tgeBps","type":"uint256"},{"internalType":"uint256","name":"cycle","type":"uint256"},{"internalType":"uint256","name":"cycleBps","type":"uint256"},{"internalType":"string","name":"description","type":"string"}],"name":"multipleVestingLock","outputs":[{"internalType":"uint256[]","name":"","type":"uint256[]"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"user","type":"address"}],"name":"normalLockCountForUser","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"user","type":"address"},{"internalType":"uint256","name":"index","type":"uint256"}],"name":"normalLockForUserAtIndex","outputs":[{"components":[{"internalType":"uint256","name":"id","type":"uint256"},{"internalType":"address","name":"token","type":"address"},{"internalType":"address","name":"owner","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"},{"internalType":"uint256","name":"lockDate","type":"uint256"},{"internalType":"uint256","name":"tgeDate","type":"uint256"},{"internalType":"uint256","name":"tgeBps","type":"uint256"},{"internalType":"uint256","name":"cycle","type":"uint256"},{"internalType":"uint256","name":"cycleBps","type":"uint256"},{"internalType":"uint256","name":"unlockedAmount","type":"uint256"},{"internalType":"string","name":"description","type":"string"}],"internalType":"struct PinkLock02.Lock","name":"","type":"tuple"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"user","type":"address"}],"name":"normalLocksForUser","outputs":[{"components":[{"internalType":"uint256","name":"id","type":"uint256"},{"internalType":"address","name":"token","type":"address"},{"internalType":"address","name":"owner","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"},{"internalType":"uint256","name":"lockDate","type":"uint256"},{"internalType":"uint256","name":"tgeDate","type":"uint256"},{"internalType":"uint256","name":"tgeBps","type":"uint256"},{"internalType":"uint256","name":"cycle","type":"uint256"},{"internalType":"uint256","name":"cycleBps","type":"uint256"},{"internalType":"uint256","name":"unlockedAmount","type":"uint256"},{"internalType":"string","name":"description","type":"string"}],"internalType":"struct PinkLock02.Lock[]","name":"","type":"tuple[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"lockId","type":"uint256"}],"name":"renounceLockOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"token","type":"address"}],"name":"totalLockCountForToken","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"user","type":"address"}],"name":"totalLockCountForUser","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalTokenLockedCount","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"lockId","type":"uint256"},{"internalType":"address","name":"newOwner","type":"address"}],"name":"transferLockOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"lockId","type":"uint256"}],"name":"unlock","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"token","type":"address"},{"internalType":"bool","name":"isLpToken","type":"bool"},{"internalType":"uint256","name":"amount","type":"uint256"},{"internalType":"uint256","name":"tgeDate","type":"uint256"},{"internalType":"uint256","name":"tgeBps","type":"uint256"},{"internalType":"uint256","name":"cycle","type":"uint256"},{"internalType":"uint256","name":"cycleBps","type":"uint256"},{"internalType":"string","name":"description","type":"string"}],"name":"vestingLock","outputs":[{"internalType":"uint256","name":"id","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"lockId","type":"uint256"}],"name":"withdrawableTokens","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"}]'
            unicriptabi = '[{"inputs":[{"internalType":"contract IUniFactory","name":"_uniswapFactory","type":"address"}],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"previousOwner","type":"address"},{"indexed":true,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"lpToken","type":"address"},{"indexed":false,"internalType":"address","name":"user","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"lockDate","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"unlockDate","type":"uint256"}],"name":"onDeposit","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"lpToken","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"}],"name":"onWithdraw","type":"event"},{"inputs":[],"name":"gFees","outputs":[{"internalType":"uint256","name":"ethFee","type":"uint256"},{"internalType":"contract IERCBurn","name":"secondaryFeeToken","type":"address"},{"internalType":"uint256","name":"secondaryTokenFee","type":"uint256"},{"internalType":"uint256","name":"secondaryTokenDiscount","type":"uint256"},{"internalType":"uint256","name":"liquidityFee","type":"uint256"},{"internalType":"uint256","name":"referralPercent","type":"uint256"},{"internalType":"contract IERCBurn","name":"referralToken","type":"address"},{"internalType":"uint256","name":"referralHold","type":"uint256"},{"internalType":"uint256","name":"referralDiscount","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_index","type":"uint256"}],"name":"getLockedTokenAtIndex","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getNumLockedTokens","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_lpToken","type":"address"}],"name":"getNumLocksForToken","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_user","type":"address"},{"internalType":"address","name":"_lpToken","type":"address"},{"internalType":"uint256","name":"_index","type":"uint256"}],"name":"getUserLockForTokenAtIndex","outputs":[{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_user","type":"address"},{"internalType":"uint256","name":"_index","type":"uint256"}],"name":"getUserLockedTokenAtIndex","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_user","type":"address"}],"name":"getUserNumLockedTokens","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_user","type":"address"},{"internalType":"address","name":"_lpToken","type":"address"}],"name":"getUserNumLocksForToken","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_user","type":"address"}],"name":"getUserWhitelistStatus","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_index","type":"uint256"}],"name":"getWhitelistedUserAtIndex","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getWhitelistedUsersLength","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_lpToken","type":"address"},{"internalType":"uint256","name":"_index","type":"uint256"},{"internalType":"uint256","name":"_lockID","type":"uint256"},{"internalType":"uint256","name":"_amount","type":"uint256"}],"name":"incrementLock","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_lpToken","type":"address"},{"internalType":"uint256","name":"_amount","type":"uint256"},{"internalType":"uint256","name":"_unlock_date","type":"uint256"},{"internalType":"address payable","name":"_referral","type":"address"},{"internalType":"bool","name":"_fee_in_eth","type":"bool"},{"internalType":"address payable","name":"_withdrawer","type":"address"}],"name":"lockLPToken","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"address","name":"_lpToken","type":"address"},{"internalType":"uint256","name":"_index","type":"uint256"},{"internalType":"uint256","name":"_lockID","type":"uint256"},{"internalType":"uint256","name":"_amount","type":"uint256"}],"name":"migrate","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_lpToken","type":"address"},{"internalType":"uint256","name":"_index","type":"uint256"},{"internalType":"uint256","name":"_lockID","type":"uint256"},{"internalType":"uint256","name":"_unlock_date","type":"uint256"}],"name":"relock","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"renounceOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address payable","name":"_devaddr","type":"address"}],"name":"setDev","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_referralPercent","type":"uint256"},{"internalType":"uint256","name":"_referralDiscount","type":"uint256"},{"internalType":"uint256","name":"_ethFee","type":"uint256"},{"internalType":"uint256","name":"_secondaryTokenFee","type":"uint256"},{"internalType":"uint256","name":"_secondaryTokenDiscount","type":"uint256"},{"internalType":"uint256","name":"_liquidityFee","type":"uint256"}],"name":"setFees","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"contract IMigrator","name":"_migrator","type":"address"}],"name":"setMigrator","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"contract IERCBurn","name":"_referralToken","type":"address"},{"internalType":"uint256","name":"_hold","type":"uint256"}],"name":"setReferralTokenAndHold","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_secondaryFeeToken","type":"address"}],"name":"setSecondaryFeeToken","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_lpToken","type":"address"},{"internalType":"uint256","name":"_index","type":"uint256"},{"internalType":"uint256","name":"_lockID","type":"uint256"},{"internalType":"uint256","name":"_amount","type":"uint256"}],"name":"splitLock","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"uint256","name":"","type":"uint256"}],"name":"tokenLocks","outputs":[{"internalType":"uint256","name":"lockDate","type":"uint256"},{"internalType":"uint256","name":"amount","type":"uint256"},{"internalType":"uint256","name":"initialAmount","type":"uint256"},{"internalType":"uint256","name":"unlockDate","type":"uint256"},{"internalType":"uint256","name":"lockID","type":"uint256"},{"internalType":"address","name":"owner","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_lpToken","type":"address"},{"internalType":"uint256","name":"_index","type":"uint256"},{"internalType":"uint256","name":"_lockID","type":"uint256"},{"internalType":"address payable","name":"_newOwner","type":"address"}],"name":"transferLockOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"uniswapFactory","outputs":[{"internalType":"contract IUniFactory","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_user","type":"address"},{"internalType":"bool","name":"_add","type":"bool"}],"name":"whitelistFeeAccount","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_lpToken","type":"address"},{"internalType":"uint256","name":"_index","type":"uint256"},{"internalType":"uint256","name":"_lockID","type":"uint256"},{"internalType":"uint256","name":"_amount","type":"uint256"}],"name":"withdraw","outputs":[],"stateMutability":"nonpayable","type":"function"}]'
            trustswapabi = '[{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"companyWallet","type":"address"}],"name":"CompanyWalletUpdated","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"id","type":"uint256"},{"indexed":true,"internalType":"address","name":"tokenAddress","type":"address"},{"indexed":true,"internalType":"address","name":"withdrawalAddress","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"unlockTime","type":"uint256"}],"name":"Deposit","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"id","type":"uint256"},{"indexed":true,"internalType":"address","name":"tokenAddress","type":"address"},{"indexed":false,"internalType":"uint256","name":"tokenId","type":"uint256"},{"indexed":true,"internalType":"address","name":"withdrawalAddress","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"unlockTime","type":"uint256"}],"name":"DepositNFT","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256","name":"fees","type":"uint256"}],"name":"FeesChanged","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"token","type":"address"},{"indexed":false,"internalType":"bool","name":"isFree","type":"bool"}],"name":"FreeTokenListUpdated","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"id","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"unlockTime","type":"uint256"}],"name":"LockDurationExtended","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"id","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"remainingAmount","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"splitLockId","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"newSplitLockAmount","type":"uint256"}],"name":"LockSplit","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"id","type":"uint256"},{"indexed":true,"internalType":"address","name":"tokenAddress","type":"address"},{"indexed":false,"internalType":"uint256","name":"tokenId","type":"uint256"},{"indexed":true,"internalType":"address","name":"withdrawalAddress","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"}],"name":"LogNFTWithdrawal","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"id","type":"uint256"},{"indexed":true,"internalType":"address","name":"tokenAddress","type":"address"},{"indexed":true,"internalType":"address","name":"withdrawalAddress","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"}],"name":"LogTokenWithdrawal","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"nftContract","type":"address"}],"name":"NftContractUpdated","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"previousOwner","type":"address"},{"indexed":true,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"account","type":"address"}],"name":"Paused","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"referralDiscount","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"referrerCut","type":"uint256"}],"name":"ReferralParamsChanged","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"addr","type":"address"},{"indexed":false,"internalType":"uint256","name":"referrerCut","type":"uint256"}],"name":"ReferrerRewarded","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"account","type":"address"}],"name":"Unpaused","type":"event"},{"inputs":[],"name":"NFT","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"token","type":"address"}],"name":"addTokenToFreeList","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"allDepositIds","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"companyWallet","outputs":[{"internalType":"address payable","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"depositId","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"uint256","name":"","type":"uint256"}],"name":"depositsByWithdrawalAddress","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_id","type":"uint256"},{"internalType":"uint256","name":"_unlockTime","type":"uint256"}],"name":"extendLockDuration","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"feesInUSD","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getAllDepositIds","outputs":[{"internalType":"uint256[]","name":"","type":"uint256[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_id","type":"uint256"}],"name":"getDepositDetails","outputs":[{"internalType":"address","name":"_tokenAddress","type":"address"},{"internalType":"address","name":"_withdrawalAddress","type":"address"},{"internalType":"uint256","name":"_tokenAmount","type":"uint256"},{"internalType":"uint256","name":"_unlockTime","type":"uint256"},{"internalType":"bool","name":"_withdrawn","type":"bool"},{"internalType":"uint256","name":"_tokenId","type":"uint256"},{"internalType":"bool","name":"_isNFT","type":"bool"},{"internalType":"uint256","name":"_migratedLockDepositId","type":"uint256"},{"internalType":"bool","name":"_isNFTMinted","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_withdrawalAddress","type":"address"}],"name":"getDepositsByWithdrawalAddress","outputs":[{"internalType":"uint256[]","name":"","type":"uint256[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_tokenAddress","type":"address"}],"name":"getFeesInETH","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_tokenAddress","type":"address"}],"name":"getTotalTokenBalance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"initialize","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"token","type":"address"}],"name":"isFreeToken","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"listMigratedDepositIds","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_tokenAddress","type":"address"},{"internalType":"address","name":"_withdrawalAddress","type":"address"},{"internalType":"uint256","name":"_amount","type":"uint256"},{"internalType":"uint256","name":"_unlockTime","type":"uint256"},{"internalType":"uint256","name":"_tokenId","type":"uint256"},{"internalType":"bool","name":"_mintNFT","type":"bool"},{"internalType":"address","name":"referrer","type":"address"}],"name":"lockNFT","outputs":[{"internalType":"uint256","name":"_id","type":"uint256"}],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"address","name":"_tokenAddress","type":"address"},{"internalType":"address","name":"_withdrawalAddress","type":"address"},{"internalType":"uint256","name":"_amount","type":"uint256"},{"internalType":"uint256","name":"_unlockTime","type":"uint256"},{"internalType":"bool","name":"_mintNFT","type":"bool"},{"internalType":"address","name":"referrer","type":"address"}],"name":"lockToken","outputs":[{"internalType":"uint256","name":"_id","type":"uint256"}],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"lockedNFTs","outputs":[{"internalType":"address","name":"tokenAddress","type":"address"},{"internalType":"address","name":"withdrawalAddress","type":"address"},{"internalType":"uint256","name":"tokenAmount","type":"uint256"},{"internalType":"uint256","name":"unlockTime","type":"uint256"},{"internalType":"bool","name":"withdrawn","type":"bool"},{"internalType":"uint256","name":"tokenId","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"lockedToken","outputs":[{"internalType":"address","name":"tokenAddress","type":"address"},{"internalType":"address","name":"withdrawalAddress","type":"address"},{"internalType":"uint256","name":"tokenAmount","type":"uint256"},{"internalType":"uint256","name":"unlockTime","type":"uint256"},{"internalType":"bool","name":"withdrawn","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_id","type":"uint256"}],"name":"mintNFTforLock","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"nftMinted","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"nonfungiblePositionManager","outputs":[{"internalType":"contract IERC721Enumerable","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"address","name":"","type":"address"},{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"bytes","name":"","type":"bytes"}],"name":"onERC721Received","outputs":[{"internalType":"bytes4","name":"","type":"bytes4"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"pause","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"paused","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"priceEstimator","outputs":[{"internalType":"contract IPriceEstimator","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"referralDiscount","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"referrerCut","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"token","type":"address"}],"name":"removeTokenFromFreeList","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"renounceOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address payable","name":"_companyWallet","type":"address"}],"name":"setCompanyWallet","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_priceEstimator","type":"address"},{"internalType":"address","name":"_usdTokenAddress","type":"address"},{"internalType":"uint256","name":"_feesInUSD","type":"uint256"},{"internalType":"address payable","name":"_companyWallet","type":"address"}],"name":"setFeeParams","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_feesInUSD","type":"uint256"}],"name":"setFeesInUSD","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_nftContractAddress","type":"address"}],"name":"setNFTContract","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_referralDiscount","type":"uint256"},{"internalType":"uint256","name":"_referrerCut","type":"uint256"}],"name":"setReferralParams","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_id","type":"uint256"},{"internalType":"uint256","name":"_splitAmount","type":"uint256"},{"internalType":"uint256","name":"_splitUnlockTime","type":"uint256"},{"internalType":"bool","name":"_mintNFT","type":"bool"}],"name":"splitLock","outputs":[{"internalType":"uint256","name":"_splitLockId","type":"uint256"}],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_id","type":"uint256"},{"internalType":"address","name":"_receiverAddress","type":"address"}],"name":"transferLocks","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"unpause","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"usdTokenAddress","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"v3Migrator","outputs":[{"internalType":"contract IV3Migrator","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"address","name":"","type":"address"}],"name":"walletTokenBalance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_id","type":"uint256"},{"internalType":"uint256","name":"_amount","type":"uint256"}],"name":"withdrawTokens","outputs":[],"stateMutability":"nonpayable","type":"function"}]'
            trustproxiabi = '[{"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256","name":"fees","type":"uint256"}],"name":"FeesChanged","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"SentToAddress","type":"address"},{"indexed":false,"internalType":"uint256","name":"AmountTransferred","type":"uint256"}],"name":"LogWithdrawal","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"previousOwner","type":"address"},{"indexed":true,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"account","type":"address"}],"name":"Paused","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"account","type":"address"}],"name":"Unpaused","type":"event"},{"inputs":[{"internalType":"address","name":"token","type":"address"}],"name":"addTokenToFreeList","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"allDepositIds","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"companyWallet","outputs":[{"internalType":"address payable","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_tokenAddress","type":"address"},{"internalType":"address","name":"_withdrawalAddress","type":"address"},{"internalType":"uint256[]","name":"_amounts","type":"uint256[]"},{"internalType":"uint256[]","name":"_unlockTimes","type":"uint256[]"}],"name":"createMultipleLocks","outputs":[{"internalType":"uint256","name":"_id","type":"uint256"}],"stateMutability":"payable","type":"function"},{"inputs":[],"name":"depositId","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"uint256","name":"","type":"uint256"}],"name":"depositsByWithdrawalAddress","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_id","type":"uint256"},{"internalType":"uint256","name":"_unlockTime","type":"uint256"}],"name":"extendLockDuration","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"feesInUSD","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getAllDepositIds","outputs":[{"internalType":"uint256[]","name":"","type":"uint256[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_id","type":"uint256"}],"name":"getDepositDetails","outputs":[{"internalType":"address","name":"_tokenAddress","type":"address"},{"internalType":"address","name":"_withdrawalAddress","type":"address"},{"internalType":"uint256","name":"_tokenAmount","type":"uint256"},{"internalType":"uint256","name":"_unlockTime","type":"uint256"},{"internalType":"bool","name":"_withdrawn","type":"bool"},{"internalType":"uint256","name":"_tokenId","type":"uint256"},{"internalType":"bool","name":"_isNFT","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_withdrawalAddress","type":"address"}],"name":"getDepositsByWithdrawalAddress","outputs":[{"internalType":"uint256[]","name":"","type":"uint256[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_tokenAddress","type":"address"}],"name":"getFeesInETH","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_tokenAddress","type":"address"},{"internalType":"address","name":"_walletAddress","type":"address"}],"name":"getTokenBalanceByAddress","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_tokenAddress","type":"address"}],"name":"getTotalTokenBalance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"initialize","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"token","type":"address"}],"name":"isFreeToken","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_tokenAddress","type":"address"},{"internalType":"address","name":"_withdrawalAddress","type":"address"},{"internalType":"uint256","name":"_amount","type":"uint256"},{"internalType":"uint256","name":"_unlockTime","type":"uint256"},{"internalType":"uint256","name":"_tokenId","type":"uint256"}],"name":"lockNFTs","outputs":[{"internalType":"uint256","name":"_id","type":"uint256"}],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"address","name":"_tokenAddress","type":"address"},{"internalType":"address","name":"_withdrawalAddress","type":"address"},{"internalType":"uint256","name":"_amount","type":"uint256"},{"internalType":"uint256","name":"_unlockTime","type":"uint256"}],"name":"lockTokens","outputs":[{"internalType":"uint256","name":"_id","type":"uint256"}],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"lockedNFTs","outputs":[{"internalType":"address","name":"tokenAddress","type":"address"},{"internalType":"address","name":"withdrawalAddress","type":"address"},{"internalType":"uint256","name":"tokenAmount","type":"uint256"},{"internalType":"uint256","name":"unlockTime","type":"uint256"},{"internalType":"bool","name":"withdrawn","type":"bool"},{"internalType":"uint256","name":"tokenId","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"lockedToken","outputs":[{"internalType":"address","name":"tokenAddress","type":"address"},{"internalType":"address","name":"withdrawalAddress","type":"address"},{"internalType":"uint256","name":"tokenAmount","type":"uint256"},{"internalType":"uint256","name":"unlockTime","type":"uint256"},{"internalType":"bool","name":"withdrawn","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"address","name":"","type":"address"},{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"bytes","name":"","type":"bytes"}],"name":"onERC721Received","outputs":[{"internalType":"bytes4","name":"","type":"bytes4"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"pause","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"paused","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"priceEstimator","outputs":[{"internalType":"contract IPriceEstimator","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"token","type":"address"}],"name":"removeTokenFromFreeList","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"renounceOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address payable","name":"_companyWallet","type":"address"}],"name":"setCompanyWallet","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_priceEstimator","type":"address"},{"internalType":"address","name":"_usdTokenAddress","type":"address"},{"internalType":"uint256","name":"_feesInUSD","type":"uint256"},{"internalType":"address payable","name":"_companyWallet","type":"address"}],"name":"setFeeParams","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_feesInUSD","type":"uint256"}],"name":"setFeesInUSD","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_id","type":"uint256"},{"internalType":"address","name":"_receiverAddress","type":"address"}],"name":"transferLocks","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"unpause","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"usdTokenAddress","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"address","name":"","type":"address"}],"name":"walletTokenBalance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_id","type":"uint256"}],"name":"withdrawTokens","outputs":[],"stateMutability":"nonpayable","type":"function"}]'
            abi_trust = '[{"constant":false,"inputs":[{"name":"newImplementation","type":"address"}],"name":"upgradeTo","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"newImplementation","type":"address"},{"name":"data","type":"bytes"}],"name":"upgradeToAndCall","outputs":[],"payable":true,"stateMutability":"payable","type":"function"},{"constant":false,"inputs":[],"name":"implementation","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"newAdmin","type":"address"}],"name":"changeAdmin","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[],"name":"admin","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"inputs":[{"name":"_logic","type":"address"},{"name":"_admin","type":"address"},{"name":"_data","type":"bytes"}],"payable":true,"stateMutability":"payable","type":"constructor"},{"payable":true,"stateMutability":"payable","type":"fallback"},{"anonymous":false,"inputs":[{"indexed":false,"name":"previousAdmin","type":"address"},{"indexed":false,"name":"newAdmin","type":"address"}],"name":"AdminChanged","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"implementation","type":"address"}],"name":"Upgraded","type":"event"}]'

            contract_pinkcrypt = web3.eth.contract(address=pinkysale, abi=pinkysaleabi)
            contract_unicrypt = web3.eth.contract(address=unicript, abi=unicriptabi)
            contract_trustswapsecure = web3.eth.contract(address=trustswap, abi=trustswapabi)

            checkLocked = contract_pinkcrypt.functions.totalLockCountForToken(pair_address).call()
            checkLocked02 = contract_unicrypt.functions.getNumLocksForToken(pair_address).call()
            checkLocked03 = contract_trustswapsecure.functions.getTotalTokenBalance(pair_address).call()

            dead_address = web3.to_checksum_address(dead_address)

            BalanceDeadlp = lpContract.functions.balanceOf(dead_address).call() / lpDECIMAL
            BalanceNullLp = lpContract.functions.balanceOf(null_address).call() / lpDECIMAL
            if (checkLocked == 1):
                # print("---------CHECK IF LOCK------\n")
                pinkyOwnerlp = lpContract.functions.balanceOf(pinkysale).call() / lpDECIMAL
                pinkyliquidity_percentage = pinkyOwnerlp / totalLpBalance * 100
                pinkylockinfo = contract_pinkcrypt.functions.getLocksForToken(pair_address, 0, 1).call()
                unlocked_date = pinkylockinfo[0][5]
                timestamp = unlocked_date
                value = datetime.datetime.fromtimestamp(timestamp)
                my_date = f"{value:%d-%m-%Y %H:%M:%S}"
                print(style.MAGENTA + "[PINKY V2] Locked With Percentage Locked: ", pinkyliquidity_percentage, "%")
                print("UNLOCK DATE: ", my_date)
                days, hours, minutes = lock_time_difference(my_date)
                print(style.YELLOW + f"TOKEN LOCKED FOR: {days} days {hours} hours {minutes} minutes")
                if days >= 90:
                    criteria_met = True

                reserves = getReserves(pair_address)
                print(reserves)
                tokenLiquidityAmount = float(web3.from_wei(reserves[1], "ether"))
                lp_amount = tokenLiquidityAmount
                if lp_amount < 5:
                        print(style.RED + "CURRENT LP BALANCE: ", round(tokenLiquidityAmount, 2), "ETH")
                else:
                    print(style.GREEN + "Current Liquidity", round(tokenLiquidityAmount, 2), "ETH")

            elif checkLocked02 >= 1:
                # print("---------CHECK IF LOCK------\n")
                unicryptOwnerlp = lpContract.functions.balanceOf(unicript).call() / lpDECIMAL
                unicryptliquidity_percentage = unicryptOwnerlp / totalLpBalance * 100
                print(style.MAGENTA + "[UNICRYPT] Locked With Percentage Locked: ", unicryptliquidity_percentage, "%")
                Unicryptlockinfo = contract_unicrypt.functions.tokenLocks(pair_address, 0).call()
                unlocked_date = Unicryptlockinfo[3]
                timestamp = unlocked_date
                value = datetime.datetime.fromtimestamp(timestamp)
                my_date = f"{value:%d-%m-%Y %H:%M:%S}"
                print("UNLOCK DATE: ", my_date)
                days, hours, minutes = lock_time_difference(my_date)
                if days >= 90:
                    criteria_met = True
                print(style.YELLOW + f"TOKEN LOCKED FOR: {days} days {hours} hours {minutes} minutes")

                reserves = getReserves(pair_address)
                tokenLiquidityAmount = float(web3.from_wei(reserves[get_token_from_lp(pair_address)], "ether"))
                lp_amount = tokenLiquidityAmount

                if lp_amount < 5:
                    tokenLiquidityAmount = float(web3.from_wei(reserves[get_token_from_lp(pair_address)], "ether"))

                    print(style.RED + "CURRENT LP BALANCE : ", round(tokenLiquidityAmount, 2), "ETH")
                else:
                    tokenLiquidityAmount = float(web3.from_wei(reserves[get_token_from_lp(pair_address)], "ether"))
                    print(style.GREEN + "Current Liquidity", round(tokenLiquidityAmount, 2), "ETH")



            elif checkLocked03 > 1:
                trustswapcryptOwnerlp = lpContract.functions.balanceOf(trustswap).call() / lpDECIMAL
                trustswapliquidity_percentage = trustswapcryptOwnerlp / totalLpBalance * 100
                TrustSwaplockinfo = contract_trustswapsecure.functions.getDepositsByWithdrawalAddress(deployer_address).call()
                if TrustSwaplockinfo == []:
                    criteria_met = True
                    print(style.MAGENTA + "[TRUSTWAP] Locked With Percentage Locked: ",round(trustswapliquidity_percentage), "%")
                else:
                    TrustSwaplockinfo_ = contract_trustswapsecure.functions.lockedToken(TrustSwaplockinfo[0]).call()
                    print(style.YELLOW + "[TRUSTWAP] Locked With Percentage Locked: ", trustswapliquidity_percentage, "%")
                    unlocked_date = TrustSwaplockinfo_[3]
                    timestamp = unlocked_date
                    value = datetime.datetime.fromtimestamp(timestamp)
                    my_date = f"{value:%d-%m-%Y %H:%M:%S}"
                    print("UNLOCK DATE: ", my_date)
                    days, hours, minutes = lock_time_difference(my_date)
                    if days >= 90:
                        criteria_met = True
                    print(style.YELLOW + f"TOKEN LOCKED FOR: {days} days {hours} hours {minutes} minutes")

                    reserves = getReserves(pair_address)
                    tokenLiquidityAmount = float(web3.from_wei(reserves[1], "ether"))
                    lp_amount = tokenLiquidityAmount
                    if lp_amount < 5:
                        tokenLiquidityAmount = float(web3.from_wei(reserves[get_token_from_lp(pair_address)], "ether"))
                        print(style.RED + "CURRENT LP BALANCE : ", round(tokenLiquidityAmount, 2), "ETH")
                    else:
                        tokenLiquidityAmount = float(web3.from_wei(reserves[get_token_from_lp(pair_address)], "ether"))
                        print(style.GREEN + "Current Liquidity", round(tokenLiquidityAmount, 2), "ETH")



            elif BalanceDeadlp > 0:
                criteria_met = True
                Ownerliquidity_percentage = BalanceDeadlp / totalLpBalance * 100
                percent_lp = Ownerliquidity_percentage
                print(style.RESET + "DEAD WALLET LP tokens", BalanceDeadlp, "Percentage", round(Ownerliquidity_percentage),
                      "%")


            else:
                print(style.RED + ("Liquidity is not Locked by certfied authority proceed with extreme caution"))

            ###### CHECKING BUYING CONDITION ##########
            # x = get_creation_timestamp(token_address)
            # print(x)

            if criteria_met:
                print(style.GREEN, "Buying Criteria MET", style.RESET)

                #num_days, hours, minutes =  get_creation_timestamp(token_address)

                ### HAVE YOUR OWN BUYING CRITERIA THIS IS JUST A SAMPLE ###

                if token_total_holders <100 and owner in (null_address,dead_address) and minutes in range(7,11) and hours < 1 and days < 1:
                    if (token_total_holders < 50 and round(liquidity) in range(1500, 5000)) or (
                            token_total_holders in range(30, 50) and round(liquidity) in range(5000, 8000)) or (
                            token_total_holders in range(60, 99) and round(liquidity) in range(5000, 15001)) or (
                            token_total_holders in range(100,250) and round(liquidity)in range(10000,25001)):
                            print(style.YELLOW, "TESTING NEW HYPOTHESIS FOR BUYING", style.RESET)
                            print(style.GREEN, "BUYING", style.RESET)
            else:
                print(style.RED, "Buying Criteria NOT MET", style.RESET)
        else:
            print("This is a UNIV3 POOL")
            if result.lp_holders != None:  
                for lp_holder in result.lp_holders:
                    tag = lp_holder.tag
                    locked_percentage = float(lp_holder.percent) * 100
                    formatted_percentage = round(locked_percentage, 2)

                    if lp_holder.is_locked == 1 and float(lp_holder.percent) > 0.05 and result.lp_holders[
                        0].is_contract == 1:
                        criteria_met = True
                        if result.lp_holders[0].locked_detail != None:
                            end_time_str = result.lp_holders[0].locked_detail[0].end_time
                            opt_time_str = result.lp_holders[0].locked_detail[0].opt_time
                            end_time = parser.isoparse(end_time_str)
                            opt_time = parser.isoparse(opt_time_str)
                            time_difference = end_time - opt_time
                            days_locked = time_difference.days
                            seconds = time_difference.seconds
                            hours, remainder = divmod(seconds, 3600)
                            minutes, _ = divmod(remainder, 60)

                            print(f"Number of days locked: {days_locked} days, {hours} Hours, {minutes} minutes")
                            print(f"Locked Percentage: {formatted_percentage}  Provider : {tag}")
                        else:
                            criteria_met = True
                            print(f"Locked Percentage: {formatted_percentage}  Provider : {tag}")
                    elif lp_holder.is_locked == 0 and lp_holder.address != deployer_address and lp_holder.address != pair_address:
                        print(
                            style.RED + f"UNKNOWN Address {lp_holder.address} OWNS {formatted_percentage} of LP TOKENS",
                            style.RESET)


                    elif lp_holder.is_locked == 1 and float(lp_holder.percent) > 0.05:

                        if lp_holder.address == owner:
                            criteria_met = False

                            print(style.RED + f"Owner owns {formatted_percentage} of LP TOKENS", style.RESET)
                        elif lp_holder.address == deployer_address:
                            criteria_met = False
                            print(style.RED + f"Creator owns {formatted_percentage} of LP TOKENS", style.RESET)
                        elif lp_holder.address == null_address:
                            criteria_met = True
                            print(f"NUll Address Owns {formatted_percentage} of LP TOKESN")
                        elif lp_holder.address == dead_address:
                            criteria_met = True
                            print(f"DEAD  Address Owns {formatted_percentage} of LP TOKESN")
                    elif lp_holder.is_locked == 0 and float(lp_holder.percent) > 0.05:

                        if lp_holder.address == owner:
                            criteria_met = False

                            print(style.RED + f"Owner owns {formatted_percentage} of LP TOKENS", style.RESET)
                        elif lp_holder.address == deployer_address:
                            criteria_met = False
                            print(style.RED + f"Creator owns {formatted_percentage} of LP TOKENS", style.RESET)
                    elif lp_holder.is_locked == 0 and float(lp_holder.percent) > 0.05:

                        if lp_holder.address == owner and owner == null_address:
                            criteria_met = True
                            print(style.GREEN + f"NULL ADDRESS  owns {formatted_percentage} of LP TOKENS", style.RESET)
                        elif lp_holder.address == deployer_address and owner == null_address:

                            criteria_met = True
                            # print(creator_address)
                            print(
                                style.RED + f"Creator owns {formatted_percentage} of LP TOKENS ---This might be actually locked",
                                style.RESET)
                       
                        elif lp_holder.address == null_address:
                            criteria_met = True
                            print(f"NUll Address Owns {formatted_percentage} of LP TOKEN")
                        elif lp_holder.address == dead_address:
                            criteria_met = True
                            print(f"DEAD Address Owns {formatted_percentage} of LP TOKEN")
                    
            else:
                print("UNKNOWN ADDRESS OWNS LP TOKENS")
            #### CHECKING BUYING CONDITION
            security_checks_dict = dict(security_checks)
            if criteria_met:
                if owner == null_address or owner == dead_address:
                    token_total_holders = data['token']['totalHolders']
                    liquidity = data['pair']['liquidity']
                    if (
                            token_total_holders < 50 and liquidity < 6000 or token_total_holders > 50 and liquidity > 10000 or token_total_holders > 100 and liquidity > 10000 and security_checks_dict.get(
                            "Buy Tax") <= expected_outcomes["Buy Tax"] and security_checks_dict.get(
                            "Sell Tax") <= expected_outcomes["Sell Tax"] and security_checks_dict.get(
                        "Owner Balance Percent") <= expected_outcomes[
                        "Owner Balance Percent"] and security_checks_dict.get("Creator Balance Percent") <=
                            expected_outcomes["Creator Balance Percent"]
                         
                    ):
                       
                        print(style.GREEN, "============================================", style.RESET)

                        print(style.GREEN, "This token Matches buying criteria")
                        print(style.GREEN, "BUYING", style.RESET)



                    else:
                        print(style.RED, "============================================", style.RESET)

                        print(style.RED, "BOT NOT BUYING")
            print(style.RESET, "============================================")



        #security_checks_dict = dict(security_checks)

        
if __name__ == "__main__":
    token_address = input("Enter Token Address: ")
    analyze_token(token_address)




