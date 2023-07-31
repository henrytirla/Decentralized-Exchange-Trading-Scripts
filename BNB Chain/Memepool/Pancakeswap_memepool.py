
# Import the web3.py library
from web3 import Web3
import webbrowser
import json
from web3.middleware import geth_poa_middleware
import requests
import config
import datetime
import asyncio
from uniswap_universal_router_decoder import RouterCodec





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



# Connect to the Ethereum blockchain using the Infura node
filter_days= int(input("Enter Txn Filter in days eg 1 = Txn Less than 1 day Old: "))
w3 = Web3(Web3.HTTPProvider("https://bsc-dataseed2.binance.org/"))

w3.middleware_onion.inject(geth_poa_middleware, layer=0)

router_dict={"0x10ED43C718714eb63d5aA57B78B54704E256024E":True, #Pancakeswap main router
             #"0x1a1ec25DC08e98e5E93F1104B5e5cdD298707d31":True, #Metamask main router

}

router_address="0x10ED43C718714eb63d5aA57B78B54704E256024E"
router_abi= '[{"inputs":[{"internalType":"address","name":"_factory","type":"address"},{"internalType":"address","name":"_WETH","type":"address"}],"stateMutability":"nonpayable","type":"constructor"},{"inputs":[],"name":"WETH","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"tokenA","type":"address"},{"internalType":"address","name":"tokenB","type":"address"},{"internalType":"uint256","name":"amountADesired","type":"uint256"},{"internalType":"uint256","name":"amountBDesired","type":"uint256"},{"internalType":"uint256","name":"amountAMin","type":"uint256"},{"internalType":"uint256","name":"amountBMin","type":"uint256"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"addLiquidity","outputs":[{"internalType":"uint256","name":"amountA","type":"uint256"},{"internalType":"uint256","name":"amountB","type":"uint256"},{"internalType":"uint256","name":"liquidity","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"token","type":"address"},{"internalType":"uint256","name":"amountTokenDesired","type":"uint256"},{"internalType":"uint256","name":"amountTokenMin","type":"uint256"},{"internalType":"uint256","name":"amountETHMin","type":"uint256"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"addLiquidityETH","outputs":[{"internalType":"uint256","name":"amountToken","type":"uint256"},{"internalType":"uint256","name":"amountETH","type":"uint256"},{"internalType":"uint256","name":"liquidity","type":"uint256"}],"stateMutability":"payable","type":"function"},{"inputs":[],"name":"factory","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountOut","type":"uint256"},{"internalType":"uint256","name":"reserveIn","type":"uint256"},{"internalType":"uint256","name":"reserveOut","type":"uint256"}],"name":"getAmountIn","outputs":[{"internalType":"uint256","name":"amountIn","type":"uint256"}],"stateMutability":"pure","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountIn","type":"uint256"},{"internalType":"uint256","name":"reserveIn","type":"uint256"},{"internalType":"uint256","name":"reserveOut","type":"uint256"}],"name":"getAmountOut","outputs":[{"internalType":"uint256","name":"amountOut","type":"uint256"}],"stateMutability":"pure","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountOut","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"}],"name":"getAmountsIn","outputs":[{"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountIn","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"}],"name":"getAmountsOut","outputs":[{"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountA","type":"uint256"},{"internalType":"uint256","name":"reserveA","type":"uint256"},{"internalType":"uint256","name":"reserveB","type":"uint256"}],"name":"quote","outputs":[{"internalType":"uint256","name":"amountB","type":"uint256"}],"stateMutability":"pure","type":"function"},{"inputs":[{"internalType":"address","name":"tokenA","type":"address"},{"internalType":"address","name":"tokenB","type":"address"},{"internalType":"uint256","name":"liquidity","type":"uint256"},{"internalType":"uint256","name":"amountAMin","type":"uint256"},{"internalType":"uint256","name":"amountBMin","type":"uint256"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"removeLiquidity","outputs":[{"internalType":"uint256","name":"amountA","type":"uint256"},{"internalType":"uint256","name":"amountB","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"token","type":"address"},{"internalType":"uint256","name":"liquidity","type":"uint256"},{"internalType":"uint256","name":"amountTokenMin","type":"uint256"},{"internalType":"uint256","name":"amountETHMin","type":"uint256"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"removeLiquidityETH","outputs":[{"internalType":"uint256","name":"amountToken","type":"uint256"},{"internalType":"uint256","name":"amountETH","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"token","type":"address"},{"internalType":"uint256","name":"liquidity","type":"uint256"},{"internalType":"uint256","name":"amountTokenMin","type":"uint256"},{"internalType":"uint256","name":"amountETHMin","type":"uint256"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"removeLiquidityETHSupportingFeeOnTransferTokens","outputs":[{"internalType":"uint256","name":"amountETH","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"token","type":"address"},{"internalType":"uint256","name":"liquidity","type":"uint256"},{"internalType":"uint256","name":"amountTokenMin","type":"uint256"},{"internalType":"uint256","name":"amountETHMin","type":"uint256"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"},{"internalType":"bool","name":"approveMax","type":"bool"},{"internalType":"uint8","name":"v","type":"uint8"},{"internalType":"bytes32","name":"r","type":"bytes32"},{"internalType":"bytes32","name":"s","type":"bytes32"}],"name":"removeLiquidityETHWithPermit","outputs":[{"internalType":"uint256","name":"amountToken","type":"uint256"},{"internalType":"uint256","name":"amountETH","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"token","type":"address"},{"internalType":"uint256","name":"liquidity","type":"uint256"},{"internalType":"uint256","name":"amountTokenMin","type":"uint256"},{"internalType":"uint256","name":"amountETHMin","type":"uint256"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"},{"internalType":"bool","name":"approveMax","type":"bool"},{"internalType":"uint8","name":"v","type":"uint8"},{"internalType":"bytes32","name":"r","type":"bytes32"},{"internalType":"bytes32","name":"s","type":"bytes32"}],"name":"removeLiquidityETHWithPermitSupportingFeeOnTransferTokens","outputs":[{"internalType":"uint256","name":"amountETH","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"tokenA","type":"address"},{"internalType":"address","name":"tokenB","type":"address"},{"internalType":"uint256","name":"liquidity","type":"uint256"},{"internalType":"uint256","name":"amountAMin","type":"uint256"},{"internalType":"uint256","name":"amountBMin","type":"uint256"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"},{"internalType":"bool","name":"approveMax","type":"bool"},{"internalType":"uint8","name":"v","type":"uint8"},{"internalType":"bytes32","name":"r","type":"bytes32"},{"internalType":"bytes32","name":"s","type":"bytes32"}],"name":"removeLiquidityWithPermit","outputs":[{"internalType":"uint256","name":"amountA","type":"uint256"},{"internalType":"uint256","name":"amountB","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountOut","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"swapETHForExactTokens","outputs":[{"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountOutMin","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"swapExactETHForTokens","outputs":[{"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountOutMin","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"swapExactETHForTokensSupportingFeeOnTransferTokens","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountIn","type":"uint256"},{"internalType":"uint256","name":"amountOutMin","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"swapExactTokensForETH","outputs":[{"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountIn","type":"uint256"},{"internalType":"uint256","name":"amountOutMin","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"swapExactTokensForETHSupportingFeeOnTransferTokens","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountIn","type":"uint256"},{"internalType":"uint256","name":"amountOutMin","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"swapExactTokensForTokens","outputs":[{"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountIn","type":"uint256"},{"internalType":"uint256","name":"amountOutMin","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"swapExactTokensForTokensSupportingFeeOnTransferTokens","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountOut","type":"uint256"},{"internalType":"uint256","name":"amountInMax","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"swapTokensForExactETH","outputs":[{"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountOut","type":"uint256"},{"internalType":"uint256","name":"amountInMax","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"swapTokensForExactTokens","outputs":[{"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],"stateMutability":"nonpayable","type":"function"},{"stateMutability":"payable","type":"receive"}]'

WBNB ="0xbb4CdB9CBd36B01bD1cBaEBF2De08d9173bc095c"

def get_token_name_symbol(web3, contract_address, abi):
    token_contract = web3.eth.contract(address=contract_address, abi=abi)
    token_name = token_contract.functions.name().call()
    token_symbol = token_contract.functions.symbol().call()
    token_decimals = token_contract.functions.decimals().call()


    return token_name, token_symbol, token_decimals


def get_contract_abi(contract_address):
    bscscan_api_key = config.bsc_api
    url = f'https://api.bscscan.com/api?module=contract&action=getsourcecode&address={contract_address}&apikey={config.bsc_api}'
    response = requests.get(url)

    if response.status_code == 200:
        contract_info = response.json()
        if 'result' in contract_info and contract_info['result'] and 'ABI' in contract_info['result'][
            0]:
            return contract_info['result'][0]['ABI']
        else:
            return None
    else:
        return None




def get_contract_creation_date(contract_address):
    from datetime import datetime
    bscscan_api_key = config.bsc_api

    url = f"https://api.bscscan.com/api?module=account&action=txlist&address={contract_address}&startblock=1&endblock=99999999&sort=asc&apikey={bscscan_api_key}"
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

def format_time_difference(creation_time_str):
    from datetime import datetime, timedelta

    creation_time = datetime.strptime(creation_time_str, "%d-%m-%Y %H:%M:%S")
    current_time = datetime.utcnow()
    time_difference = current_time - creation_time

    # Extract days, hours, and minutes from the time difference
    days = time_difference.days
    hours, remainder = divmod(time_difference.seconds, 3600)
    minutes, _ = divmod(remainder, 60)
    formatted_time = style.CYAN + f" {days} days {hours} hours {minutes} minutes ago"


    return days,formatted_time





#swap_functions =["swapETHForExactTokens","swapExactETHForTokens","swapExactETHForTokensSupportingFeeOnTransferTokens","swapExactTokensForETH","swapExactTokensForETHSupportingFeeOnTransferTokens","swapExactTokensForTokens","swapExactTokensForTokensSupportingFeeOnTransferTokens","swapTokensForExactETH","swapTokensForExactTokens","addLiquidityETH"]

swap_functions =["swapETHForExactTokens","swapExactETHForTokens","swapExactETHForTokensSupportingFeeOnTransferTokens","addLiquidityETH"]
check_functions ={"swapETHForExactTokens":True, "swapExactETHForTokens":True,"swapExactETHForTokensSupportingFeeOnTransferTokens":True,"addLiquidityETH":True,'multicall':True}

arr =[]

# Loop forever to scan the mempool





contract = w3.eth.contract(address=router_address,abi=router_abi)
count = 0
async def handle_new_block(block):
    global count
    for tx_hash in block['transactions']:
        try:
            tx_hash =w3.to_hex(tx_hash)
            tx = w3.eth.get_transaction(tx_hash)
            data = tx['input']

            to = tx['to']
            if to == router_address:
                hash= tx['hash']
                tx_hash = w3.to_hex(hash)
                decoded = contract.decode_function_input(data)
                #print(decoded,end='\n')
                # Extract function name
                decoded_str = str(decoded[0])
                start_index = decoded_str.find(" ") + 1
                end_index = decoded_str.find("(")
                function_name = decoded_str[start_index:end_index]
                path = decoded[1].get('path', [])
                if path and path[0] == '0xbb4CdB9CBd36B01bD1cBaEBF2De08d9173bc095c' and path[
                    1] != '0xbb4CdB9CBd36B01bD1cBaEBF2De08d9173bc095c' and check_functions[function_name] == True:
                    count+=1

                    for swapFunc in range(len(swap_functions)):
                        #print(swap_functions[swapFunc])
                        if swap_functions[swapFunc] == function_name:
                            arr.append(swap_functions[swapFunc])

                        # print(style.GREEN + "METHOD-----", arr[-1])
                    token_contract_address = path[1]
                    creation_date = get_contract_creation_date(token_contract_address)
                    days, time_since_creation = format_time_difference(creation_date)

                    token_abi_json = get_contract_abi(token_contract_address)
                    if days <filter_days:
                        if token_abi_json:
                            token_abi = json.loads(token_abi_json)
                            token_name, token_symbol, token_decimals = get_token_name_symbol(w3, token_contract_address,
                                                                                             token_abi)
                            creation_date = get_contract_creation_date(token_contract_address)
                            days, time_since_creation = format_time_difference(creation_date)
                            print(style.YELLOW + "PANCAKESWAP-------MEMEPOOL")

                            # print(decoded)
                            print(style.CYAN + f"Current Txn Block Number: {block['number']}, Latest Block Number: {w3.eth.block_number}",
                                end='\n ')

                            print(count, 'https://bscscan.com/tx/' + tx_hash)
                            print(style.GREEN + f"Token Address: {token_contract_address} (Name: {token_name}, Symbol: {token_symbol}, Decimal: {token_decimals}), Creation: {time_since_creation}")
                            # print(style.GREEN + f"METHOD----- {arr[-1]} (Name: {token_name}, Symbol: {token_symbol})")


                    else:
                        #print(style.GREEN + "METHOD-----", arr[-1])
                        pass

                    if arr[-1] == "addLiquidityETH":
                        webbrowser.open('https://bscscan.com/tx/' + tx_hash)
                else:
                    pass




            else:
                    continue

        except Exception as e:
            print("Error",e)

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
async def main():

    await track_new_blocks()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())












