import json
import time
import datetime
from web3 import Web3
import requests
import re




web3 = Web3(Web3.HTTPProvider("https://bsc-dataseed1.binance.org/"))

def get_source_code(token_address):
    Eth_Api = "VFZUKK626NHN7SQTP1GAE5MK6TZN3BV2BR"  # Change this to your Etherscan API ID
    sourceCodeGetRequestURL = "https://api.bscscan.com/api?module=contract&action=getsourcecode&address=" + token_address + "&apikey=" + Eth_Api
    response = requests.get(url=sourceCodeGetRequestURL)
    resultSourceCode = response.json()

    # Check if the request was successful
    if 'status' in resultSourceCode and resultSourceCode['status'] == '1':
        sourceCode = resultSourceCode['result'][0]['SourceCode']
        #print(sourceCode)

        # Extract the Telegram link from the source code
        telegram_link = extract_telegram_link(str(sourceCode))
        print(telegram_link)
    else:
        print("Failed to get source code.")



def extract_telegram_link(source_code):
    pattern = r'(https?://t\.me/[^\s]+)'
    match = re.search(pattern, source_code)
    if match:
        return match.group(1)
    else:
        return None



source_code =get_source_code("0x2BF588C05dfF2d926095e10f2bC0a2667eC0ABDE")
