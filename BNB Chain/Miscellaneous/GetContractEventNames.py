import web3
from web3 import Web3
import requests

contract_abi = "contract_abi_string"

web3 = Web3(Web3.HTTPProvider("https://bsc-dataseed2.binance.org/"))



contract_address =input("Enter Contract Address: ")

def get_contract_abi(contract_address):
    try:
        bscscan_api_key = 'YJ1VVGT761NZBN6RTC5JWPTZ511GN4VHGT'
        url = f'https://api.bscscan.com/api?module=contract&action=getsourcecode&address={contract_address}&apikey={bscscan_api_key}'
        response = requests.get(url)

        if response.status_code == 200:
            contract_info = response.json()
            if 'result' in contract_info and contract_info['result'] and 'ABI' in contract_info['result'][0]:
                return contract_info['result'][0]['ABI']
            else:
                return None
        else:
            return None
    except Exception as e:
        print(f"An error occurred while fetching contract ABI: {e}")
        return None


contract_tirla = web3.eth.contract(address=contract_address, abi=get_contract_abi(contract_address))

event = contract_tirla.events


for events in event:
    print(events)

