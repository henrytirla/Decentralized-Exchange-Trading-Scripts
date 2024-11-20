"Early Buyers of a token per block"



import sys
import requests
import json
import math
from web3 import Web3
from alchemy import Alchemy, Network
api_key = "YOUR ALCHEMY API KEY "
network = Network.ETH_MAINNET
alchemy = Alchemy(api_key, network)

web3 = Web3(Web3.HTTPProvider("https://eth-mainnet.g.alchemy.com/v2/Enter Your API"))

print(web3.is_connected())

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


contract_address =  input("Enter the token contract address: ")

num_blocks= int(input("Enter the number of blocks to check after liquidity is added:  "))

tokenmodel_abi = '[{"inputs":[],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"spender","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"sender","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount0","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount1","type":"uint256"},{"indexed":true,"internalType":"address","name":"to","type":"address"}],"name":"Burn","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"sender","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount0","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount1","type":"uint256"}],"name":"Mint","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"sender","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount0In","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount1In","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount0Out","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount1Out","type":"uint256"},{"indexed":true,"internalType":"address","name":"to","type":"address"}],"name":"Swap","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint112","name":"reserve0","type":"uint112"},{"indexed":false,"internalType":"uint112","name":"reserve1","type":"uint112"}],"name":"Sync","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"constant":true,"inputs":[],"name":"DOMAIN_SEPARATOR","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"MINIMUM_LIQUIDITY","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"PERMIT_TYPEHASH","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"address","name":"","type":"address"}],"name":"allowance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"}],"name":"approve","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"to","type":"address"}],"name":"burn","outputs":[{"internalType":"uint256","name":"amount0","type":"uint256"},{"internalType":"uint256","name":"amount1","type":"uint256"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"factory","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"getReserves","outputs":[{"internalType":"uint112","name":"_reserve0","type":"uint112"},{"internalType":"uint112","name":"_reserve1","type":"uint112"},{"internalType":"uint32","name":"_blockTimestampLast","type":"uint32"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"_token0","type":"address"},{"internalType":"address","name":"_token1","type":"address"}],"name":"initialize","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"kLast","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"to","type":"address"}],"name":"mint","outputs":[{"internalType":"uint256","name":"liquidity","type":"uint256"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"nonces","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"},{"internalType":"uint256","name":"deadline","type":"uint256"},{"internalType":"uint8","name":"v","type":"uint8"},{"internalType":"bytes32","name":"r","type":"bytes32"},{"internalType":"bytes32","name":"s","type":"bytes32"}],"name":"permit","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"price0CumulativeLast","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"price1CumulativeLast","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"to","type":"address"}],"name":"skim","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"uint256","name":"amount0Out","type":"uint256"},{"internalType":"uint256","name":"amount1Out","type":"uint256"},{"internalType":"address","name":"to","type":"address"},{"internalType":"bytes","name":"data","type":"bytes"}],"name":"swap","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[],"name":"sync","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"token0","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"token1","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"}],"name":"transfer","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"}],"name":"transferFrom","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"}]'

WETH= "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2"

uniswap_factory = '0x5C69bEe701ef814a2B6a3EDD4B1652CB9cc5aA6f'  # Testnet  #0x6725F303b657a9451d8BA641348b6761A6CC7a17
uniswap_factory_abi = json.loads('[{"inputs":[{"internalType":"address","name":"_feeToSetter","type":"address"}],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"token0","type":"address"},{"indexed":true,"internalType":"address","name":"token1","type":"address"},{"indexed":false,"internalType":"address","name":"pair","type":"address"},{"indexed":false,"internalType":"uint256","name":"","type":"uint256"}],"name":"PairCreated","type":"event"},{"constant":true,"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"allPairs","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"allPairsLength","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"tokenA","type":"address"},{"internalType":"address","name":"tokenB","type":"address"}],"name":"createPair","outputs":[{"internalType":"address","name":"pair","type":"address"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"feeTo","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"feeToSetter","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"address","name":"","type":"address"}],"name":"getPair","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"_feeTo","type":"address"}],"name":"setFeeTo","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"_feeToSetter","type":"address"}],"name":"setFeeToSetter","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"}]')
contract = web3.eth.contract(address=uniswap_factory, abi=uniswap_factory_abi)
lp_address = contract.functions.getPair(contract_address, WETH).call()
print(f"LP Address: {lp_address}")
# sys.exit()

def getOwnerPercentage_LpHash(contract_address, pair_address):
    contract = web3.eth.contract(address=contract_address, abi=tokenmodel_abi)
    decimals = contract.functions.decimals().call()
    DECIMAL = 10 ** decimals
    totalSupply = contract.functions.totalSupply().call() / DECIMAL

    asset_transfer = alchemy.core.get_asset_transfers(
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




def get_InitialLP(transaction_hash):


    receipt = alchemy.core.get_transaction_receipt(transaction_hash)

    target_topics = [
        Web3.to_bytes(hexstr="0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef")
    ]

    for log in receipt['logs']:
        if log['topics'][0:1] == target_topics and log['address'] =="0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2":
            hex_data = log['data'].hex()
            decoded_data = Web3.to_int(hexstr=hex_data)
            decoded_data_in_ether = Web3.from_wei(decoded_data, 'ether')
            return math.floor(decoded_data_in_ether * 10) / 10 #round(decoded_data_in_ether)

    return None

import requests
import json









def getFirstBlock_Buys(token_address, pair_address, api_key='QSD4D9KG1NYTX3Y6CPAR62G9FBW16UZ81Z', num_blocks_to_check=num_blocks):
    tokenmodel_abi = '[{"inputs":[],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"spender","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"sender","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount0","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount1","type":"uint256"},{"indexed":true,"internalType":"address","name":"to","type":"address"}],"name":"Burn","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"sender","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount0","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount1","type":"uint256"}],"name":"Mint","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"sender","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount0In","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount1In","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount0Out","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount1Out","type":"uint256"},{"indexed":true,"internalType":"address","name":"to","type":"address"}],"name":"Swap","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint112","name":"reserve0","type":"uint112"},{"indexed":false,"internalType":"uint112","name":"reserve1","type":"uint112"}],"name":"Sync","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"constant":true,"inputs":[],"name":"DOMAIN_SEPARATOR","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"MINIMUM_LIQUIDITY","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"PERMIT_TYPEHASH","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"address","name":"","type":"address"}],"name":"allowance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"}],"name":"approve","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"to","type":"address"}],"name":"burn","outputs":[{"internalType":"uint256","name":"amount0","type":"uint256"},{"internalType":"uint256","name":"amount1","type":"uint256"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"factory","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"getReserves","outputs":[{"internalType":"uint112","name":"_reserve0","type":"uint112"},{"internalType":"uint112","name":"_reserve1","type":"uint112"},{"internalType":"uint32","name":"_blockTimestampLast","type":"uint32"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"_token0","type":"address"},{"internalType":"address","name":"_token1","type":"address"}],"name":"initialize","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"kLast","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"to","type":"address"}],"name":"mint","outputs":[{"internalType":"uint256","name":"liquidity","type":"uint256"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"nonces","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"},{"internalType":"uint256","name":"deadline","type":"uint256"},{"internalType":"uint8","name":"v","type":"uint8"},{"internalType":"bytes32","name":"r","type":"bytes32"},{"internalType":"bytes32","name":"s","type":"bytes32"}],"name":"permit","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"price0CumulativeLast","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"price1CumulativeLast","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"to","type":"address"}],"name":"skim","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"uint256","name":"amount0Out","type":"uint256"},{"internalType":"uint256","name":"amount1Out","type":"uint256"},{"internalType":"address","name":"to","type":"address"},{"internalType":"bytes","name":"data","type":"bytes"}],"name":"swap","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[],"name":"sync","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"token0","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"token1","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"}],"name":"transfer","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"}],"name":"transferFrom","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"}]'
    token_address = web3.to_checksum_address(token_address)
    contract = web3.eth.contract(address=token_address, abi=tokenmodel_abi)
    decimals = contract.functions.decimals().call()
    DECIMAL = 10 ** decimals
    totalSupply = contract.functions.totalSupply().call() / DECIMAL

    # Fetch asset transfers
    asset_transfer = alchemy.core.get_asset_transfers(
        category=["erc20"],
        from_block="0x0",
        to_block="latest",
        with_metadata=False,
        exclude_zero_value=True,
        contract_addresses=[token_address],
        order="asc"
    )

    # Initialize tracking variables
    unique_hashes = set()

    count_from = set()
    address_addedLp = None
    first_block_for_pair = None
    added_liquidity = 0
    value_firstblock = 0
    first_transaction_block = None
    subsequent_values = [0] * num_blocks_to_check
    transactions_per_block = {}

    # Iterate over asset transfers
    for t in asset_transfer['transfers']:
        block_number = int(t.block_num, 16)
        from_address = t.frm
        to_address = t.to
        decoded_value = int(t.raw_contract.value, 16)
        hash_txn = t.hash

        # Identify the block where liquidity was added
        if to_address == pair_address.lower() and first_block_for_pair is None:
            address_addedLp = from_address
            added_liquidity = block_number
            first_block_for_pair = block_number
            print(f"LP ADDED ON BLOCK {style.RED}{added_liquidity}{style.RESET}")
            # Initialize transactions list for liquidity block
            transactions_per_block[added_liquidity] = []

            # Check if this is a buy transaction on the liquidity block
        if block_number == added_liquidity and t.frm != address_addedLp.lower() and t.to != address_addedLp.lower() and t.to != contract_address.lower():
            count_from.add(t.to)
            value_firstblock += decoded_value
            # Set first_transaction_block to added_liquidity if it's the first buy transaction
            if first_transaction_block is None:
                first_transaction_block = added_liquidity
                print(f"First Buy Transaction BLOCK {style.GREEN}{first_transaction_block}{style.RESET}", )

            # Add transaction details for the liquidity block
            transactions_per_block[block_number].append(
                f"{style.GREEN}[BUY]{style.RESET} Wallet: {web3.to_checksum_address(t.to)} ETHq_Balance "
                f"{style.GREEN}[ {web3.from_wei(web3.eth.get_balance(web3.to_checksum_address(t.to)), 'ether')}]{style.RESET} "
                f", NONCE: {style.MAGENTA}{web3.eth.get_transaction_count(web3.to_checksum_address(t.to))} {style.RESET} "
                f"--> {style.RED}{int(t.block_num, 16)} {style.RESET} ---> {style.YELLOW}{decoded_value / DECIMAL} {style.RESET}, "
                f"TxHash: https://etherscan.io/tx/{t.hash}"
            )
            unique_hashes.add(t.hash)

            # Set first_transaction_block if a buy transaction occurs after liquidity block
        elif added_liquidity and block_number > added_liquidity and first_transaction_block is None:
            if t.frm != address_addedLp.lower() and t.to != address_addedLp.lower():
                first_transaction_block = block_number
                # print("First transaction block after liquidity:", first_transaction_block)
                print(f"First Buy Transaction Block After LP Block {style.GREEN}{first_transaction_block}{style.RESET}", )






        
        if first_transaction_block and first_transaction_block <= block_number < first_transaction_block + num_blocks_to_check:
            block_offset = block_number - first_transaction_block
            subsequent_values[block_offset] += decoded_value

            # Track transactions in each subsequent block
            if block_number not in transactions_per_block:
                transactions_per_block[block_number] = []


            if t.to != contract_address.lower() and t.to != lp_address.lower():
                if t.hash not in unique_hashes:
                    unique_hashes.add(t.hash)
                    #web3.eth.get_transaction_count(web3.to_checksum_address(t.to)>0
                    transactions_per_block[block_number].append(
                        f"{style.GREEN}[BUY]{style.RESET} Wallet: {web3.to_checksum_address(t.to)} ETHq_Balance "
                        f"{style.GREEN}[ {web3.from_wei(web3.eth.get_balance(web3.to_checksum_address(t.to)), 'ether')}]{style.RESET} , "
                        f"NONCE: {style.MAGENTA}{web3.eth.get_transaction_count(web3.to_checksum_address(t.to))} {style.RESET} "
                        f"--> {style.RED}{int(t.block_num, 16)} {style.RESET} ---> {style.YELLOW}{decoded_value / DECIMAL} {style.RESET} , "
                        f"TxHash: https://etherscan.io/tx/{t.hash}"
                    )


    # Display results for the liquidity block
    percentage_bought_firstblock = (value_firstblock / DECIMAL) / totalSupply * 100
    print(f"PERCENT OF TOKEN BOUGHT ON LIQUIDITY BLOCK: {round(percentage_bought_firstblock, 1)}%")
    print(f"Number of wallets involved: {len(count_from)}")
    print(f"\n--- Transactions for block {added_liquidity} ---")
    for tx in transactions_per_block[added_liquidity]:
        print(tx)

    print("====================================================")
    print("DISPLAYING TRANSACTIONS FOR EACH SUBSEQUENT BLOCK")
    print("====================================================")

    if num_blocks_to_check > 1 or first_transaction_block != added_liquidity:
        # Flag to track if there are transactions after the initial block
        subsequent_transactions_exist = False
        if first_transaction_block == added_liquidity:
            first_transaction_block+=1

        # Display results for each block in the range after first_transaction_block
        for i in range(num_blocks_to_check):
            block_num = first_transaction_block + i
            percentage_bought = (subsequent_values[i] / DECIMAL) / totalSupply * 100

            # Check if there are transactions in this block
            if block_num in transactions_per_block and transactions_per_block[block_num]:
                subsequent_transactions_exist = True
                print(f"\nPERCENT OF TOKEN BOUGHT IN BLOCK {block_num}: {round(percentage_bought, 1)}%")
                print(f"--- Transactions for block {block_num} ---")
                for tx in transactions_per_block[block_num]:
                    print(tx)

        # If no subsequent transactions were found, print a message
        if not subsequent_transactions_exist:
            print("No subsequent blocks with transactions found after the initial liquidity block.")

    else:
        print("YOU REQUIRED ONLY 1 BLOCK")



try:
    initialOwner_Percentage, AddLp_Hash = getOwnerPercentage_LpHash(contract_address, lp_address)
    initial_lp = get_InitialLP(AddLp_Hash)
    print(initial_lp)
    print(f"Initial Owner Percentage: {initialOwner_Percentage}%")
    print(f"Add LP Hash: {AddLp_Hash}")
    getFirstBlock_Buys(contract_address,lp_address)


except Exception as e:
    initialOwner_Percentage=None
    AddLp_Hash= None
    initial_lp= "Not known"
    print(e)

