import web3
from web3 import Web3
import requests

contract_abi = "contract_abi_string"

web3 = Web3(Web3.HTTPProvider("https://eth-mainnet.g.alchemy.com/v2/lTlatSTYDZmCv6wVLRIDff7S3kZhL2dq"))

# pinkysale ="0x71B5759d73262FBb223956913ecF4ecC51057641"
# unicript = "0x663A5C229c09b049E36dCc11a9B0d4a8Eb9db214"
# trustswap="0xE2fE530C047f2d85298b07D9333C05737f1435fB"

contract_address =input("Enter Contract Address: ")

def get_contract_abi(contract_address):
    try:
        bscscan_api_key = 'QSD4D9KG1NYTX3Y6CPAR62G9FBW16UZ81Z'
        url = f'https://api.etherscan.io/api?module=contract&action=getsourcecode&address={contract_address}&apikey={bscscan_api_key}'
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

