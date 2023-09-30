import requests
import datetime
from goplus.token import Token
from dateutil import parser
import time
from web3 import Web3



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

web3 = Web3(Web3.HTTPProvider("https://eth-mainnet.g.alchemy.com/v2/lTlatSTYDZmCv6wVLRIDff7S3kZhL2dq"))
tokenmodel_abi = '[{"inputs":[],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"spender","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"sender","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount0","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount1","type":"uint256"},{"indexed":true,"internalType":"address","name":"to","type":"address"}],"name":"Burn","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"sender","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount0","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount1","type":"uint256"}],"name":"Mint","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"sender","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount0In","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount1In","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount0Out","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount1Out","type":"uint256"},{"indexed":true,"internalType":"address","name":"to","type":"address"}],"name":"Swap","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint112","name":"reserve0","type":"uint112"},{"indexed":false,"internalType":"uint112","name":"reserve1","type":"uint112"}],"name":"Sync","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"constant":true,"inputs":[],"name":"DOMAIN_SEPARATOR","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"MINIMUM_LIQUIDITY","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"PERMIT_TYPEHASH","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"address","name":"","type":"address"}],"name":"allowance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"}],"name":"approve","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"to","type":"address"}],"name":"burn","outputs":[{"internalType":"uint256","name":"amount0","type":"uint256"},{"internalType":"uint256","name":"amount1","type":"uint256"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"factory","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"getReserves","outputs":[{"internalType":"uint112","name":"_reserve0","type":"uint112"},{"internalType":"uint112","name":"_reserve1","type":"uint112"},{"internalType":"uint32","name":"_blockTimestampLast","type":"uint32"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"_token0","type":"address"},{"internalType":"address","name":"_token1","type":"address"}],"name":"initialize","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"kLast","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"to","type":"address"}],"name":"mint","outputs":[{"internalType":"uint256","name":"liquidity","type":"uint256"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"nonces","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"},{"internalType":"uint256","name":"deadline","type":"uint256"},{"internalType":"uint8","name":"v","type":"uint8"},{"internalType":"bytes32","name":"r","type":"bytes32"},{"internalType":"bytes32","name":"s","type":"bytes32"}],"name":"permit","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"price0CumulativeLast","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"price1CumulativeLast","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"to","type":"address"}],"name":"skim","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"uint256","name":"amount0Out","type":"uint256"},{"internalType":"uint256","name":"amount1Out","type":"uint256"},{"internalType":"address","name":"to","type":"address"},{"internalType":"bytes","name":"data","type":"bytes"}],"name":"swap","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[],"name":"sync","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"token0","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"token1","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"}],"name":"transfer","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"}],"name":"transferFrom","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"}]'


def get_deployer_address(contract_address):
    url = f'https://api.etherscan.io/api?module=account&action=txlist&address={contract_address}&startblock=0&endblock=99999999&page=1&offset=3&sort=asc&apikey=QSD4D9KG1NYTX3Y6CPAR62G9FBW16UZ81Z'
    response = requests.get(url)
    data = response.json()

    if data['status'] == '1':
        for tx in data['result']:
            if tx['to'] == contract_address.lower():
                deployer = web3.to_checksum_address(tx['from'])
                return deployer
    else:
        raise Exception('Error while fetching transactions: ' + data['message'])

def lock_time_difference(creation_time_str):

    from datetime import datetime, timedelta

    creation_time = datetime.strptime(creation_time_str, "%d-%m-%Y %H:%M:%S")
    current_time = datetime.utcnow()
    time_difference = creation_time - current_time  

    years = time_difference.days // 365
    days = time_difference.days
    hours, remainder = divmod(time_difference.seconds, 3600)
    minutes, _ = divmod(remainder, 60)
    return days ,hours, minutes

def get_owner_and_balance(token_address):
    Eth_Api = "QSD4D9KG1NYTX3Y6CPAR62G9FBW16UZ81Z"  # Change this to your Etherscan API ID

    abiCodeGetRequestURL = "https://api.etherscan.io/api?module=contract&action=getabi&address=" + token_address + "&apikey=" + Eth_Api
    resultAbi = requests.get(url=abiCodeGetRequestURL).json()
    tokenmodel_abi = '[{"inputs":[],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"spender","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"sender","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount0","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount1","type":"uint256"},{"indexed":true,"internalType":"address","name":"to","type":"address"}],"name":"Burn","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"sender","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount0","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount1","type":"uint256"}],"name":"Mint","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"sender","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount0In","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount1In","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount0Out","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount1Out","type":"uint256"},{"indexed":true,"internalType":"address","name":"to","type":"address"}],"name":"Swap","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint112","name":"reserve0","type":"uint112"},{"indexed":false,"internalType":"uint112","name":"reserve1","type":"uint112"}],"name":"Sync","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"constant":true,"inputs":[],"name":"DOMAIN_SEPARATOR","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"MINIMUM_LIQUIDITY","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"PERMIT_TYPEHASH","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"address","name":"","type":"address"}],"name":"allowance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"}],"name":"approve","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"to","type":"address"}],"name":"burn","outputs":[{"internalType":"uint256","name":"amount0","type":"uint256"},{"internalType":"uint256","name":"amount1","type":"uint256"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"factory","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"getReserves","outputs":[{"internalType":"uint112","name":"_reserve0","type":"uint112"},{"internalType":"uint112","name":"_reserve1","type":"uint112"},{"internalType":"uint32","name":"_blockTimestampLast","type":"uint32"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"_token0","type":"address"},{"internalType":"address","name":"_token1","type":"address"}],"name":"initialize","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"kLast","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"to","type":"address"}],"name":"mint","outputs":[{"internalType":"uint256","name":"liquidity","type":"uint256"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"nonces","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"},{"internalType":"uint256","name":"deadline","type":"uint256"},{"internalType":"uint8","name":"v","type":"uint8"},{"internalType":"bytes32","name":"r","type":"bytes32"},{"internalType":"bytes32","name":"s","type":"bytes32"}],"name":"permit","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"price0CumulativeLast","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"price1CumulativeLast","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"to","type":"address"}],"name":"skim","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"uint256","name":"amount0Out","type":"uint256"},{"internalType":"uint256","name":"amount1Out","type":"uint256"},{"internalType":"address","name":"to","type":"address"},{"internalType":"bytes","name":"data","type":"bytes"}],"name":"swap","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[],"name":"sync","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"token0","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"token1","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"}],"name":"transfer","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"}],"name":"transferFrom","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"}]'
    ownership_function = '{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"}'
    getOwner_function = '{"inputs":[],"name":"getOwner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"}'
    token_address= web3.to_checksum_address(token_address)
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
            return owner, round(percent_owner, 2)
        elif getOwner_function in abi:
            contract = web3.eth.contract(address=token_address, abi=abi)

            owner = contract.functions.getOwner().call()
            contract_owner = owner
            owner_balance = contract.functions.balanceOf(owner).call() / DECIMAL
            percent_owner = owner_balance / totalSupply * 100

            return owner, round(percent_owner, 2)
       
    else:
        contract_owner = None

    return contract_owner, None





def analyze_token(token_address):
    token_address = web3.to_checksum_address(token_address)


    contract = web3.eth.contract(address=token_address, abi=tokenmodel_abi)
    deployer_address = get_deployer_address(token_address)
    decimals = contract.functions.decimals().call()
    DECIMAL = 10 ** decimals
    totalSupply = contract.functions.totalSupply().call() / DECIMAL

    deployer_balance = contract.functions.balanceOf(deployer_address).call() / DECIMAL
    percent_deployerBalance = deployer_balance / totalSupply * 100

    null_address = "0x0000000000000000000000000000000000000000"
    dead_address = "0x000000000000000000000000000000000000dEaD"
    #dead_address = "0x000000000000000000000000000000000000dead"

    ##GOPLUS SECURITY####
    data1 = Token(access_token=None).token_security(
        chain_id="1", addresses=[token_address])
    result = data1.result[token_address.lower()]
    params = {"address": token_address}
    response = requests.get(url, params=params)
    Eth_Api = "QSD4D9KG1NYTX3Y6CPAR62G9FBW16UZ81Z"
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
     
        simulation_Success= data['simulationSuccess']
       
        column_width = 20
        pair_address = data['pair']['pair']['address']
        creation_timestamp = int(data['pair']['createdAtTimestamp'])
        datetime_obj = datetime.datetime.utcfromtimestamp(creation_timestamp)
        current_time = datetime.datetime.utcnow()
        time_difference = current_time - datetime_obj
        days = time_difference.days
        hours, remainder = divmod(time_difference.seconds, 3600)
        minutes, _ = divmod(remainder, 60)

        formatted_time_difference = f"{days} days, {hours} hours, {minutes} minutes ago"
        tokenAddress= data['token']['address']
        token_name = data['token']['name']
        token_symbol = data['token']['symbol']
        token_decimals = data['token']['decimals']
        token_total_holders = data['token']['totalHolders']
        liquidity = data['pair']['liquidity']
        pair_address= data['pairAddress']
        creation_txnHash=data['pair']['creationTxHash']

        if simulation_Success :
           is_honeypot= data['honeypotResult']['isHoneypot']

           if  is_honeypot :
               flags = data['flags']
               honeypot_reason = data['honeypotResult'].get('honeypotReason', None)
               print(style.RED + f"EXECUTION REVERTED\n{honeypot_reason}\n   {flags}" + style.RESET)
               return




           else:
                print("============================================")
                print(style.YELLOW+f"TOKEN INFORMATION",style.RESET)
                print("============================================")
                print(f"{'Token Address:':{column_width - 18}}{tokenAddress:{column_width - 18}}")
                print(f"{'Token Name:':{column_width - 18}}{token_name:{column_width - 18}}")
                print(f"{'Token Symbol:':{column_width - 18}}{token_symbol:{column_width - 18}}")
                print(f"{'Token Decimals:':{column_width - 18}}{token_decimals:{column_width - 18}}")
                print(f"{'Current Holders:':{column_width - 20}}{style.GREEN}{token_total_holders:{column_width - 20}}",
                      style.RESET)
               # print(f"{'AverageTax:':{column_width - 20}}{style.RED}{round(average_tax,2):{column_width - 20}}", style.RESET)
                #print(f"{'Highest Tax:':{column_width - 20}}{style.RED}{highest_tax:{column_width - 20}}", style.RESET)
                print(f"Current Liquidity {style.GREEN} ${round(liquidity, 2)}", style.RESET)
                print(f"Token Created :{style.BLUE} {formatted_time_difference}", style.RESET)
                print(f"Pair Address: {style.BLUE} https://etherscan.io/token/{pair_address}#balances", style.RESET)
                print(f"Creation TxnHash: {style.BLUE} https://etherscan.io/tx/{creation_txnHash}", style.RESET)

      

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
            "Owner Balance Percent": 1.000000,
            "Creator Balance Percent": 1.000000,
            "Contract Balance Percent": 1.000000

        }
        
        buy_tax_value = result.buy_tax
        sell_tax_value = result.sell_tax


        if isinstance(buy_tax_value, str) and buy_tax_value == "Unknown" or buy_tax_value == '':
            print(buy_tax_value)  # This will print "Unknown"
            buy_tax_value = "Unknown"
        else:
            buy_tax_value = round(float(buy_tax_value) * 100, 1)

        if isinstance(sell_tax_value, str) and sell_tax_value == "Unknown" or sell_tax_value == '':
            print(sell_tax_value)  # This will print "Unknown"
            sell_tax_value = "Unknown"
        else:
            sell_tax_value = round(float(sell_tax_value) * 100, 1)

        owner, percent_owner = get_owner_and_balance(token_address)
        contract_balance = contract.functions.balanceOf(tokenAddress).call() / DECIMAL
        percent_contract = round(contract_balance / totalSupply * 100,2)



        security_checks = [
            ("Open Source", result.is_open_source),
            ("Buy Tax", round(data['simulationResult']['buyTax'],2)),
            ("Sell Tax", round(data['simulationResult']['sellTax'],2)),
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
            ("Owner Balance Percent", percent_owner),
            ("Creator Balance Percent", percent_deployerBalance),
            ("Contract Balance Percent",percent_contract)
        ]
        print("============================================")

        print(style.YELLOW+"SMART CONTRACT SECURITY CHECKS",style.RESET)

        print("============================================")
        criteria_met = False
        print(owner,deployer_address)
        if owner == deployer_address:
            print(f"{style.RED}🚨 Deployer Address Owns Contract 🚨", style.RESET)

        elif owner in (null_address,dead_address):
            print(f"{style.GREEN}CONTRACT IS RENOUNCED OWNER {owner}", style.RESET)
        elif owner not in (null_address,dead_address) and "0x" in owner:
            print(f"{style.RED}UNKNOWN ADDRESS OWNES CONTRACT {owner}", style.RESET)


        else:
            owner = "NULL"

            print(f"{style.RED} CONTRACT OWNER IS HIDDEN AND NOT KNOWN {owner}", style.RESET)

        all_true = True


        def evaluate_property(property_name, actual_value, expected_value):
            global all_true
            all_true= False
            check_property={"Buy Tax": False,"Sell Tax": False,"Proxy Contract":True,"Mintable":True,"Can Take Back Ownership":True,"Owner Change Balance":True,"Hidden Owner":True,"Has External Calls":True,"Transfer Pausable":True,"Cannot Sell All":True,"Tax Modifiable":True,"Personal Slippage Modifiable":True,"Slippage Modifiable":True,"Is Honeypot":True,"Has Blacklist":True,"Has Whitelist":True,"Trading Cooldown":True,"Creator Balance Percent":False,"Owner Balance Percent":False,"Open Source":False,"Contract Balance Percent":False}
            if actual_value <= expected_value:
               print(style.GREEN + f"{property_name}: {actual_value} <= {expected_value}" + style.RESET)
               all_true = True
               return True
         
            elif actual_value > expected_value and check_property[property_name]==False:
                all_true = False
                return False
            elif actual_value > expected_value and (owner == null_address or owner == dead_address) and check_property[property_name]==True:


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
                r=evaluate_property(check_name, actual_value, expected_value)
                res.append(r)


        smartContract_check=False

 
        if owner!= "NULL":
            if any(val is False for val in res) :
                print(f"{style.RED}SMART CONTRACT DOES NOT MATCH OUR CRITERIA", style.RESET)


            else:
                print(f"{style.GREEN}SMART CONTRACT MATCHES OUR CRITERIA", style.RESET)
                smartContract_check = True
        else:
            print(f"{style.RED}SMART CONTRACT DOES NOT MATCH OUR CRITERIA", style.RESET)

        print("============================================")

        print(style.YELLOW + "ANALYZING LIQUIDITY POOL TOKENS", style.RESET)
        print("============================================")
        days_locked = 0
        lpABI = '[{"inputs":[],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"spender","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"sender","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount0","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount1","type":"uint256"},{"indexed":true,"internalType":"address","name":"to","type":"address"}],"name":"Burn","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"sender","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount0","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount1","type":"uint256"}],"name":"Mint","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"sender","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount0In","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount1In","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount0Out","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount1Out","type":"uint256"},{"indexed":true,"internalType":"address","name":"to","type":"address"}],"name":"Swap","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint112","name":"reserve0","type":"uint112"},{"indexed":false,"internalType":"uint112","name":"reserve1","type":"uint112"}],"name":"Sync","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"constant":true,"inputs":[],"name":"DOMAIN_SEPARATOR","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"MINIMUM_LIQUIDITY","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"PERMIT_TYPEHASH","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"address","name":"","type":"address"}],"name":"allowance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"}],"name":"approve","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"to","type":"address"}],"name":"burn","outputs":[{"internalType":"uint256","name":"amount0","type":"uint256"},{"internalType":"uint256","name":"amount1","type":"uint256"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"factory","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"getReserves","outputs":[{"internalType":"uint112","name":"_reserve0","type":"uint112"},{"internalType":"uint112","name":"_reserve1","type":"uint112"},{"internalType":"uint32","name":"_blockTimestampLast","type":"uint32"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"_token0","type":"address"},{"internalType":"address","name":"_token1","type":"address"}],"name":"initialize","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"kLast","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"to","type":"address"}],"name":"mint","outputs":[{"internalType":"uint256","name":"liquidity","type":"uint256"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"nonces","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"},{"internalType":"uint256","name":"deadline","type":"uint256"},{"internalType":"uint8","name":"v","type":"uint8"},{"internalType":"bytes32","name":"r","type":"bytes32"},{"internalType":"bytes32","name":"s","type":"bytes32"}],"name":"permit","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"price0CumulativeLast","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"price1CumulativeLast","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"to","type":"address"}],"name":"skim","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"uint256","name":"amount0Out","type":"uint256"},{"internalType":"uint256","name":"amount1Out","type":"uint256"},{"internalType":"address","name":"to","type":"address"},{"internalType":"bytes","name":"data","type":"bytes"}],"name":"swap","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[],"name":"sync","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"token0","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"token1","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"}],"name":"transfer","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"}],"name":"transferFrom","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"}]'

        lpContract = web3.eth.contract(address=pair_address, abi=lpABI)
        lpdecimals = lpContract.functions.decimals().call()
        lpDECIMAL = 10 ** lpdecimals
        totalLpBalance = lpContract.functions.totalSupply().call() / lpDECIMAL
        print(style.GREEN +'Total Lp Balance: ' + str(totalLpBalance))

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
        if owner != "NULL" and owner not in (null_address,dead_address):
            owner =web3.to_checksum_address(owner)
            checkOwnerlp = lpContract.functions.balanceOf(owner).call() / lpDECIMAL
            Ownerliquidity_percentage = checkOwnerlp / totalLpBalance * 100
            percent_lp = Ownerliquidity_percentage
            checkDeployerLp = lpContract.functions.balanceOf(deployer_address).call() / lpDECIMAL
            deployerLiquidity_percentage = checkDeployerLp / totalLpBalance * 100
            percent_lp2= deployerLiquidity_percentage
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
            pinkyOwnerlp = lpContract.functions.balanceOf(pinkysale).call() / lpDECIMAL
            pinkyliquidity_percentage = pinkyOwnerlp / totalLpBalance * 100
            pinkylockinfo = contract_pinkcrypt.functions.getLocksForToken(pair_address, 0, 1).call()
            unlocked_date = pinkylockinfo[0][5]
            timestamp = unlocked_date
            value = datetime.datetime.fromtimestamp(timestamp)
            my_date = f"{value:%d-%m-%Y %H:%M:%S}"
            print(style.MAGENTA + "[PINKY V2] Locked With Percentage Locked: ", pinkyliquidity_percentage, "%")
            print("UNLOCK DATE: ", my_date)
            days ,hours,minutes= lock_time_difference(my_date)
            print(style.YELLOW + f"TOKEN LOCKED FOR: {days} days {hours} hours {minutes} minutes")
            if days>=90:
               criteria_met = True

            reserves = getReserves(pair_address)
            tokenLiquidityAmount = float(web3.from_wei(reserves[1], "ether"))
            lp_amount = tokenLiquidityAmount
            if lp_amount < 5:
                tokenLiquidityAmount = float(web3.from_wei(reserves[get_token_from_lp(pair_address)], "ETH"))

                print(style.RED + "CURRENT LP BALANCE: ", round(tokenLiquidityAmount, 2), "ETH")
            else:
                tokenLiquidityAmount = float(web3.from_wei(reserves[get_token_from_lp(pair_address)], "ether"))
                print(style.GREEN + "Current Liquidity", round(tokenLiquidityAmount, 2), "ETH")

        elif checkLocked02 >= 1:
            unicryptOwnerlp = lpContract.functions.balanceOf(unicript).call() / lpDECIMAL
            unicryptliquidity_percentage = unicryptOwnerlp / totalLpBalance * 100
            print(style.MAGENTA + "[UNICRYPT] Locked With Percentage Locked: ", unicryptliquidity_percentage, "%")
            Unicryptlockinfo = contract_unicrypt.functions.tokenLocks(pair_address, 0).call()
            unlocked_date = Unicryptlockinfo[3]
            timestamp = unlocked_date
            value = datetime.datetime.fromtimestamp(timestamp)
            my_date = f"{value:%d-%m-%Y %H:%M:%S}"
            print("UNLOCK DATE: ", my_date)
            days ,hours,minutes= lock_time_difference(my_date)
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
            TrustSwaplockinfo = contract_trustswapsecure.functions.getDepositsByWithdrawalAddress(
                deployer_address).call()
            print(trustswapliquidity_percentage)

            TrustSwaplockinfo_ = contract_trustswapsecure.functions.lockedToken(TrustSwaplockinfo[0]).call()

            print(style.YELLOW + "[TRUSTWAP] Locked With Percentage Locked: ", trustswapliquidity_percentage, "%")
            unlocked_date = TrustSwaplockinfo_[3]
            timestamp = unlocked_date
            value = datetime.datetime.fromtimestamp(timestamp)
            my_date = f"{value:%d-%m-%Y %H:%M:%S}"
            print("UNLOCK DATE: ", my_date)
            days ,hours,minutes= lock_time_difference(my_date)
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
             criteria_met=True
             Ownerliquidity_percentage = BalanceDeadlp / totalLpBalance * 100
             percent_lp = Ownerliquidity_percentage
             print(style.RESET + "DEAD WALLET LP tokens", BalanceDeadlp, "Percentage", round(Ownerliquidity_percentage), "%")
          

        else:
            print(style.RED + ("Liquidity is not Locked by certfied authority proceed with extreme caution"))

        #### CHECKING BUYING CONDITION
       
        if criteria_met:
           print(style.GREEN,"Buying Criteria MET",style.RESET)
        else:
           print(style.RED,"Buying Criteria NOT MET",style.RESET)
        security_checks_dict = dict(security_checks)
        #Added extra check for proxy contracts who meet lock requirement
        if (criteria_met and smartContract_check) or (owner == "NULL" and result.is_proxy=="1" ):            #if  days_locked in range(60,10000) or owner_address in (None, null_address, dead_address):
                token_total_holders = data['token']['totalHolders']
                liquidity = data['pair']['liquidity']
               
                if (token_total_holders < 50 and round(liquidity) in range(1500,5000)) or (token_total_holders in range(60,99) and round(liquidity) in range(5000, 15001)) or (token_total_holders > 100 and liquidity > 10000):

            

                        print(style.GREEN,"============================================",style.RESET)

                        print(style.GREEN, "This token Matches buying criteria")

                        print(style.GREEN, "BUYING", style.RESET)
                        #Buy_Token(token_address,0.0113)





                else:
                        print(style.RED,"============================================",style.RESET)

                        print(style.RED, "BOT NOT BUYING ")
        else:
            print(style.RED, "============================================", style.RESET)

            print(style.RED, "BOT NOT BUYING")
        print(style.RESET,"============================================")




if __name__ == "__main__":
   token_address = input("Enter Token Address: ")
   analyze_token(token_address)
   

