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


#Goerli Testnet RPC
w3 = Web3(Web3.HTTPProvider("https://eth-goerli.g.alchemy.com/v2/demo"))


uniswap_router_addresses = [
    '0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D',  #Uniswap-V2 Router
    '0xE592427A0AEce92De3Edee1F18E0157C05861564',  #Uniswap-V3 Router
    '0x68b3465833fb72A70ecDF485E0e4C7bD8665Fc45',  #Uniswap-V3 02 Router
    '0xEf1c6E67703c7BD7107eed8303Fbe6EC2554BF6B', #OldUniversal-Router
    '0x3fC91A3afd70395Cd496C647d5a6CC9D4B2b7FAD', #Universal-Router

]

print(w3.eth.get_block('latest'))
