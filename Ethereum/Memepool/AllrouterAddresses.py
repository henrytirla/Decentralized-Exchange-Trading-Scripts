"Scan Memepool for all router addresses."

#Todo create UI for this script

import asyncio
import time
from web3 import Web3
import json
import requests
import datetime
from uniswap_universal_router_decoder import RouterCodec

#TODO Aggregation Router 0x1111111254EEB25477B68fb85Ed929f73A960582



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

txn_days=int(input("Fileter for transaction eg 1 All transaction less than 1 day ago/24Hr: "))
uniswap_router_addresses = [
    '0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D',  #Uniswap-V2 Router
    '0xE592427A0AEce92De3Edee1F18E0157C05861564',  #Uniswap-V3 Router
    '0x68b3465833fb72A70ecDF485E0e4C7bD8665Fc45',  #Uniswap-V3 02 Router
    '0xEf1c6E67703c7BD7107eed8303Fbe6EC2554BF6B', #OldUniversal-Router
    '0x3fC91A3afd70395Cd496C647d5a6CC9D4B2b7FAD', #Universal-Router
    ]

check_functions = {"swapETHForExactTokens": True, "swapExactETHForTokens": True,
                   "swapExactETHForTokensSupportingFeeOnTransferTokens": True, "addLiquidityETH": True,
                   'multicall': True, 'execute': True}

#swapExactTokensForTokens
check_functionName= {"V2_SWAP_EXACT_IN":True,"UNWRAP_WETH":True,"multicall":True}#"exactInputSingle":True,

api_key = 'QSD4D9KG1NYTX3Y6CPAR62G9FBW16UZ81Z'


def get_FunctionName(decoded_data):
    decoded_str = str(decoded_data[0])
    start_index = decoded_str.find(" ") + 1
    end_index = decoded_str.find("(")
    function_name = decoded_str[start_index:end_index]
    return function_name


def decode_execute(decode_data,function_name):
    codec = RouterCodec()
    decoded_trx_input = codec.decode.function_input(decode_data)
    check_V2 = decoded_trx_input[1]['inputs'][0]
    v2fnction = get_FunctionName(check_V2)
    #print("V2 Function",v2fnction)
    values_to_check = {"V3_SWAP_EXACT_IN", "V2_SWAP_EXACT_IN", "V3_SWAP_EXACT_OUT", "V2_SWAP_EXACT_OUT", "exactOutput"}
    if v2fnction not in values_to_check:
                In_put = decoded_trx_input[1]['inputs'][1]
                fn_name = get_FunctionName(In_put)
                if fn_name in check_functionName and check_functionName[fn_name]:
                    if fn_name == 'V2_SWAP_EXACT_IN':
                        v2_path = In_put[1]['path']
                        if v2_path[0]== "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2":
                            # print(style.CYAN + function_name)
                            # print("Function Name: ", fn_name)
                            token_address= v2_path[1] #
                            creation_time=get_contract_creation_date(token_address)
                            creation_day= get_Days(creation_time)
                            if creation_day < txn_days:
                                token_abi_json = get_contract_abi(token_address)
                                if token_abi_json:
                                   token_abi = json.loads(token_abi_json)
                                   token_name, token_symbol = get_token_name_symbol(w3, token_address, token_abi)
                                   token_name, token_symbol = get_token_name_symbol(w3, token_address, token_abi)
                                   creation_date = get_contract_creation_date(token_address)
                                   time_since_creation = format_time_difference(creation_date)
                                   return f"Token Addess {token_address},{style.MAGENTA}Token Name/Symbol {token_name, token_symbol}, {style.CYAN}Creation Time {time_since_creation}"


                    elif fn_name == 'UNWRAP_WETH':
                        v3_data = decoded_trx_input[1]['inputs'][0]
                        if get_FunctionName(v3_data) == 'V3_SWAP_EXACT_IN':
                            path = decoded_trx_input[1]['inputs'][0][1]['path']
                            decoded_path = codec.decode.v3_path('V3_SWAP_EXACT_IN', path)
                            return decoded_path
                        else:
                            #print(fn_name,decoded_trx_input)
                            data = decoded_trx_input[1]['inputs'][0][1]['path']
                            return fn_name, data
                else:
                    return None
    else:
              return None


def decode_multicall(multicall_decoded):
    Inner_func = get_FunctionName(multicall_decoded)
    values_to_check = {"swapExactTokensForTokens"}
    #print("Inner Multicall Function ------",Inner_func)
    if Inner_func not in values_to_check:
        # print(style.CYAN + function_name)
        tokens = [multicall_decoded[1]['params']['tokenOut'], multicall_decoded[1]['params']['tokenIn']]
        if tokens[0] == '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2':

            token_address = tokens[1]
            creation_time = get_contract_creation_date(token_address)
            creation_day = get_Days(creation_time)
            if creation_day < txn_days:
                token_abi_json = get_contract_abi(token_address)
                if token_abi_json:
                    token_abi = json.loads(token_abi_json)
                    token_name, token_symbol = get_token_name_symbol(w3, token_address, token_abi)
                    creation_date = get_contract_creation_date(token_address)
                    time_since_creation = format_time_difference(creation_date)
                    return f"Token Addess {token_address},{style.MAGENTA}Token Name/Symbol {token_name, token_symbol}, {style.CYAN}Creation Time {time_since_creation}"
            else:
                return None

def get_contract_abi(contract_address):
    try:
        bscscan_api_key = api_key
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


def get_contract_creation_date(contract_address):
    from datetime import datetime
    url = f'https://api.etherscan.io/api?module=account&action=txlist&address={contract_address}&startblock=0&endblock=99999999&page=1&offset=3&sort=asc&apikey=QSD4D9KG1NYTX3Y6CPAR62G9FBW16UZ81Z'
    response = requests.get(url)
    data = response.json()

    if data['status'] == '1':
        for tx in data['result']:
            if tx['to'] == contract_address.lower():
                timestamp = int(tx['timeStamp'])
                formatted_time = datetime.utcfromtimestamp(timestamp).strftime("%d-%m-%Y %H:%M:%S")
                return formatted_time
    else:
        raise Exception('Error while fetching transactions: ' + data['message'])


def get_Days(creation_time_str):
    from datetime import datetime, timedelta

    creation_time = datetime.strptime(creation_time_str, "%d-%m-%Y %H:%M:%S")
    current_time = datetime.utcnow()
    time_difference = current_time - creation_time

    # Extract days, hours, and minutes from the time difference
    days = time_difference.days
    hours, remainder = divmod(time_difference.seconds, 3600)
    minutes, _ = divmod(remainder, 60)

    return days



def format_time_difference(creation_time_str):
    from datetime import datetime, timedelta

    creation_time = datetime.strptime(creation_time_str, "%d-%m-%Y %H:%M:%S")
    current_time = datetime.utcnow()
    time_difference = current_time - creation_time

    # Extract days, hours, and minutes from the time difference
    days = time_difference.days
    hours, remainder = divmod(time_difference.seconds, 3600)
    minutes, _ = divmod(remainder, 60)

    return f"{days} days {hours} hours {minutes} minutes ago"


def get_token_name_symbol(web3, contract_address, abi):
    token_contract = web3.eth.contract(address=contract_address, abi=abi)
    token_name = token_contract.functions.name().call()
    token_symbol = token_contract.functions.symbol().call()

    return token_name, token_symbol

def decode_input_data(input_data, router,tx_hash):
    try:
        with open("router_abi.json") as f:
            routers_abi = json.load(f)
        abi = routers_abi.get(router)


        if abi is None:
            raise ValueError("ABI not found for the specified router.")
        contract = w3.eth.contract(address=router, abi=abi)
        decoded_data = contract.decode_function_input(input_data)
        function_name = get_FunctionName(decoded_data)
        if function_name in check_functions and check_functions[function_name]:
            if function_name == "execute":
                data= decode_execute(input_data,function_name)
                return data
            elif function_name == "multicall":

                byte_data = decoded_data[1]['data'][0]
                multicall_decoded = contract.decode_function_input(byte_data)
                data=decode_multicall(multicall_decoded)
                return data

            elif function_name == "addLiquidityETH":
                 print(style.CYAN+function_name)
                 print(decoded_data)
                 token_address=decoded_data[1]['token']
                 token_abi_json = get_contract_abi(token_address)
                 if token_abi_json:
                     token_abi = json.loads(token_abi_json)
                     token_name, token_symbol = get_token_name_symbol(w3, token_address, token_abi)
                     creation_date = get_contract_creation_date(token_address)
                     time_since_creation = format_time_difference(creation_date)

                 return f"Token Addess {token_address},{style.MAGENTA}Token Name/Symbol {token_name, token_symbol}, {style.CYAN}Creation Time {time_since_creation}"

            else:
                #print(style.CYAN+function_name)
                path_ =decoded_data[1]['path']
                if path_[0] == '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2':
                    token_address = path_[1]
                    creation_time = get_contract_creation_date(token_address)
                    creation_day = get_Days(creation_time)
                    if creation_day < txn_days:
                        token_abi_json = get_contract_abi(token_address)
                        if token_abi_json:
                            token_abi = json.loads(token_abi_json)
                            token_name, token_symbol = get_token_name_symbol(w3, token_address, token_abi)
                            creation_date = get_contract_creation_date(token_address)
                            time_since_creation = format_time_difference(creation_date)

                            return f"Token Addess {token_address},{style.MAGENTA}Token Name/Symbol {token_name, token_symbol}, {style.CYAN}Creation Time {time_since_creation}"
                    else:
                        pass
    except IndexError:
        print("An error occurred while decoding the input data. The list index is out of range.")
        return None
    except Exception as e:
        print("An error occurred while decoding the input data:", e,router,tx_hash)
        return None


count= 0
async def handle_new_block(block):
    global count
    for tx_hash in block['transactions']:
        try:

            tx = w3.eth.get_transaction(tx_hash)
            # creation_date = get_contract_creation_date(token_contract_address)
            # days, time_since_creation = format_time_difference(creation_date)
            #
            # if days < 50:


            for router_address in uniswap_router_addresses:

                if tx['to'] == router_address:
                    hash= tx['hash']
                    tx_hash = w3.to_hex(hash)
                    function_name = decode_input_data(tx['input'], tx['to'],tx_hash)
                    #print("Function Name?",function_name)

                    if function_name is not None:
                        count += 1
                        tx_details= w3.eth.get_transaction(tx_hash)
                        # print()tx_details['blockNumber']
                        print(style.CYAN+f"Current Txn Block Number: {block['number']}, Latest Block Number: {w3.eth.block_number}",end='\n ')
                        #print(print_block_numbers())
                        print(count,style.YELLOW + "Tx_Hash: ",
                              "https://etherscan.io/tx/"+tx_hash)

                        print(style.GREEN+f"{function_name}")
                        print(style.RED+"------------------")
                    #break
                else:
                    continue

        except Exception as e:
            print("An error occurred while processing a transaction:", e,w3.to_hex(tx_hash))

async def track_new_blocks():
    current_block_number =  w3.eth.block_number

    while True:
        latest_block = w3.eth.get_block('latest')
        latest_block_number = latest_block['number']

        if latest_block_number > current_block_number:
            for block_number in range(current_block_number + 1, latest_block_number + 1):
                block =  w3.eth.get_block(block_number)
                await handle_new_block(block)

            current_block_number = latest_block_number

        # Delay between checking for new blocks
        await asyncio.sleep(1)

# Run the event loop


# Run the event loop
async def main():

    await track_new_blocks()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())