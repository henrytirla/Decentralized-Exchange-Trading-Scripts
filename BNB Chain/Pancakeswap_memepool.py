
# Import the web3.py library
from web3 import Web3
import webbrowser
import json
from web3.middleware import geth_poa_middleware
import requests
import config
import datetime




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
web3 = Web3(Web3.HTTPProvider("https://bsc-dataseed2.binance.org/"))
web3.middleware_onion.inject(geth_poa_middleware, layer=0)

# Define the Uniswap Router and Factory addresses
pcsRouter = web3.toChecksumAddress('0x10ED43C718714eb63d5aA57B78B54704E256024E')
v3pcsRouter= web3.toChecksumAddress('0x13f4EA83D0bd40E75C8222255bc855a974568Dd4')
WBNB ="0xbb4CdB9CBd36B01bD1cBaEBF2De08d9173bc095c"

pcsAbi = json.loads('[{"inputs":[{"internalType":"address","name":"_factory","type":"address"},{"internalType":"address","name":"_WETH","type":"address"}],"stateMutability":"nonpayable","type":"constructor"},{"inputs":[],"name":"WETH","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"tokenA","type":"address"},{"internalType":"address","name":"tokenB","type":"address"},{"internalType":"uint256","name":"amountADesired","type":"uint256"},{"internalType":"uint256","name":"amountBDesired","type":"uint256"},{"internalType":"uint256","name":"amountAMin","type":"uint256"},{"internalType":"uint256","name":"amountBMin","type":"uint256"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"addLiquidity","outputs":[{"internalType":"uint256","name":"amountA","type":"uint256"},{"internalType":"uint256","name":"amountB","type":"uint256"},{"internalType":"uint256","name":"liquidity","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"token","type":"address"},{"internalType":"uint256","name":"amountTokenDesired","type":"uint256"},{"internalType":"uint256","name":"amountTokenMin","type":"uint256"},{"internalType":"uint256","name":"amountETHMin","type":"uint256"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"addLiquidityETH","outputs":[{"internalType":"uint256","name":"amountToken","type":"uint256"},{"internalType":"uint256","name":"amountETH","type":"uint256"},{"internalType":"uint256","name":"liquidity","type":"uint256"}],"stateMutability":"payable","type":"function"},{"inputs":[],"name":"factory","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountOut","type":"uint256"},{"internalType":"uint256","name":"reserveIn","type":"uint256"},{"internalType":"uint256","name":"reserveOut","type":"uint256"}],"name":"getAmountIn","outputs":[{"internalType":"uint256","name":"amountIn","type":"uint256"}],"stateMutability":"pure","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountIn","type":"uint256"},{"internalType":"uint256","name":"reserveIn","type":"uint256"},{"internalType":"uint256","name":"reserveOut","type":"uint256"}],"name":"getAmountOut","outputs":[{"internalType":"uint256","name":"amountOut","type":"uint256"}],"stateMutability":"pure","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountOut","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"}],"name":"getAmountsIn","outputs":[{"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountIn","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"}],"name":"getAmountsOut","outputs":[{"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountA","type":"uint256"},{"internalType":"uint256","name":"reserveA","type":"uint256"},{"internalType":"uint256","name":"reserveB","type":"uint256"}],"name":"quote","outputs":[{"internalType":"uint256","name":"amountB","type":"uint256"}],"stateMutability":"pure","type":"function"},{"inputs":[{"internalType":"address","name":"tokenA","type":"address"},{"internalType":"address","name":"tokenB","type":"address"},{"internalType":"uint256","name":"liquidity","type":"uint256"},{"internalType":"uint256","name":"amountAMin","type":"uint256"},{"internalType":"uint256","name":"amountBMin","type":"uint256"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"removeLiquidity","outputs":[{"internalType":"uint256","name":"amountA","type":"uint256"},{"internalType":"uint256","name":"amountB","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"token","type":"address"},{"internalType":"uint256","name":"liquidity","type":"uint256"},{"internalType":"uint256","name":"amountTokenMin","type":"uint256"},{"internalType":"uint256","name":"amountETHMin","type":"uint256"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"removeLiquidityETH","outputs":[{"internalType":"uint256","name":"amountToken","type":"uint256"},{"internalType":"uint256","name":"amountETH","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"token","type":"address"},{"internalType":"uint256","name":"liquidity","type":"uint256"},{"internalType":"uint256","name":"amountTokenMin","type":"uint256"},{"internalType":"uint256","name":"amountETHMin","type":"uint256"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"removeLiquidityETHSupportingFeeOnTransferTokens","outputs":[{"internalType":"uint256","name":"amountETH","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"token","type":"address"},{"internalType":"uint256","name":"liquidity","type":"uint256"},{"internalType":"uint256","name":"amountTokenMin","type":"uint256"},{"internalType":"uint256","name":"amountETHMin","type":"uint256"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"},{"internalType":"bool","name":"approveMax","type":"bool"},{"internalType":"uint8","name":"v","type":"uint8"},{"internalType":"bytes32","name":"r","type":"bytes32"},{"internalType":"bytes32","name":"s","type":"bytes32"}],"name":"removeLiquidityETHWithPermit","outputs":[{"internalType":"uint256","name":"amountToken","type":"uint256"},{"internalType":"uint256","name":"amountETH","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"token","type":"address"},{"internalType":"uint256","name":"liquidity","type":"uint256"},{"internalType":"uint256","name":"amountTokenMin","type":"uint256"},{"internalType":"uint256","name":"amountETHMin","type":"uint256"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"},{"internalType":"bool","name":"approveMax","type":"bool"},{"internalType":"uint8","name":"v","type":"uint8"},{"internalType":"bytes32","name":"r","type":"bytes32"},{"internalType":"bytes32","name":"s","type":"bytes32"}],"name":"removeLiquidityETHWithPermitSupportingFeeOnTransferTokens","outputs":[{"internalType":"uint256","name":"amountETH","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"tokenA","type":"address"},{"internalType":"address","name":"tokenB","type":"address"},{"internalType":"uint256","name":"liquidity","type":"uint256"},{"internalType":"uint256","name":"amountAMin","type":"uint256"},{"internalType":"uint256","name":"amountBMin","type":"uint256"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"},{"internalType":"bool","name":"approveMax","type":"bool"},{"internalType":"uint8","name":"v","type":"uint8"},{"internalType":"bytes32","name":"r","type":"bytes32"},{"internalType":"bytes32","name":"s","type":"bytes32"}],"name":"removeLiquidityWithPermit","outputs":[{"internalType":"uint256","name":"amountA","type":"uint256"},{"internalType":"uint256","name":"amountB","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountOut","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"swapETHForExactTokens","outputs":[{"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountOutMin","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"swapExactETHForTokens","outputs":[{"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountOutMin","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"swapExactETHForTokensSupportingFeeOnTransferTokens","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountIn","type":"uint256"},{"internalType":"uint256","name":"amountOutMin","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"swapExactTokensForETH","outputs":[{"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountIn","type":"uint256"},{"internalType":"uint256","name":"amountOutMin","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"swapExactTokensForETHSupportingFeeOnTransferTokens","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountIn","type":"uint256"},{"internalType":"uint256","name":"amountOutMin","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"swapExactTokensForTokens","outputs":[{"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountIn","type":"uint256"},{"internalType":"uint256","name":"amountOutMin","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"swapExactTokensForTokensSupportingFeeOnTransferTokens","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountOut","type":"uint256"},{"internalType":"uint256","name":"amountInMax","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"swapTokensForExactETH","outputs":[{"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountOut","type":"uint256"},{"internalType":"uint256","name":"amountInMax","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"swapTokensForExactTokens","outputs":[{"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],"stateMutability":"nonpayable","type":"function"},{"stateMutability":"payable","type":"receive"}]')

pcsContract = web3.eth.contract(address=pcsRouter, abi=pcsAbi)



#swap_functions =["swapETHForExactTokens","swapExactETHForTokens","swapExactETHForTokensSupportingFeeOnTransferTokens","swapExactTokensForETH","swapExactTokensForETHSupportingFeeOnTransferTokens","swapExactTokensForTokens","swapExactTokensForTokensSupportingFeeOnTransferTokens","swapTokensForExactETH","swapTokensForExactTokens","addLiquidityETH"]

swap_functions =["swapETHForExactTokens","swapExactETHForTokens","swapExactETHForTokensSupportingFeeOnTransferTokens","addLiquidityETH"]
check_functions ={"swapETHForExactTokens":True, "swapExactETHForTokens":True,"swapExactETHForTokensSupportingFeeOnTransferTokens":True,"addLiquidityETH":True,'multicall':True}

arr =[]

# Loop forever to scan the mempool



x= True
count=0
while x == True:
    try:
        while True:
            # Get the pending transactions in the mempool
            transactions = web3.eth.getBlock("pending")['transactions']
            ##print(transactions)
            for tx in transactions:
                tx_hash = web3.toHex(tx)
                trans = web3.eth.get_transaction(tx_hash)
                from_wallet = trans['from']
                #print("FROM", from_wallet)
                data = trans['input']
                to = trans['to']
                #print(to, tx_hash)
                def get_token_name_symbol(web3, contract_address, abi):
                    token_contract = web3.eth.contract(address=contract_address, abi=abi)
                    token_name = token_contract.functions.name().call()
                    token_symbol = token_contract.functions.symbol().call()

                    return token_name, token_symbol


                def get_contract_abi(contract_address):
                    bscscan_api_key = config.bsc_api
                    url = f'https://api.bscscan.com/api?module=contract&action=getsourcecode&address={contract_address}&apikey={bscscan_api_key}'
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
                    bscscan_api_key = config.bsc_api
                    url = f"https://api.bscscan.com/api?module=account&action=txlist&address={contract_address}&startblock=1&endblock=99999999&sort=asc&apikey={bscscan_api_key}"

                    response = requests.get(url)
                    data = response.json()

                    if data['status'] == '1':
                        creation_transaction = data['result'][0]
                        timestamp = int(creation_transaction['timeStamp'])
                        creation_date = datetime.datetime.fromtimestamp(timestamp)
                        return creation_date
                    else:
                        raise Exception(f"Error: {data['message']}")


                def format_time_difference(creation_date):
                    now = datetime.datetime.utcnow()
                    time_diff = now - creation_date
                    #time_diff += datetime.timedelta(minutes=1)
                    days = time_diff.days
                    seconds = time_diff.seconds
                    hours, remainder = divmod(seconds, 3600)
                    minutes = remainder // 60
                    return style.CYAN+f" {days} days {hours} hours {minutes} minutes ago"





                if  to == pcsRouter:
                    #print(style.YELLOW + "PANCAKESWAP-------MEMEPOOL")
                    decoded = pcsContract.decode_function_input(data)
                    #print("Decoded", decoded)
                    #count += 1
                    #print('https://bscscan.com/tx/' + tx_hash, ": Count", count)
                    #print(decoded)

                    # Extract function name
                    decoded_str = str(decoded[0])
                    start_index = decoded_str.find(" ") + 1
                    end_index = decoded_str.find("(")
                    function_name = decoded_str[start_index:end_index]
                    path = decoded[1].get('path', [])

                    if path and path[0] == '0xbb4CdB9CBd36B01bD1cBaEBF2De08d9173bc095c'and path[1] != '0xbb4CdB9CBd36B01bD1cBaEBF2De08d9173bc095c' and check_functions[function_name] == True  :
                        print(style.YELLOW + "PANCAKESWAP-------MEMEPOOL")
                        count+=1
                        #print(decoded)
                        print('https://bscscan.com/tx/' + tx_hash, ": Count", count)

                        for swapFunc in range(len(swap_functions)):
                            if swap_functions[swapFunc] == function_name:
                                arr.append(swap_functions[swapFunc])

                        #print(style.GREEN + "METHOD-----", arr[-1])

                        token_contract_address = path[1]
                        token_abi_json = get_contract_abi(token_contract_address)
                        if token_abi_json:
                            token_abi = json.loads(token_abi_json)
                            token_name, token_symbol = get_token_name_symbol(web3, token_contract_address, token_abi)
                            creation_date = get_contract_creation_date(token_contract_address)
                            time_since_creation = format_time_difference(creation_date)
                            print(style.GREEN + f"METHOD----- {arr[-1]} (Name: {token_name}, Symbol: {token_symbol}), Creation: {time_since_creation}")
                            #print(style.GREEN + f"METHOD----- {arr[-1]} (Name: {token_name}, Symbol: {token_symbol})")

                        else:
                            print(style.GREEN + "METHOD-----", arr[-1])

                        # print(style.BLUE+"Address",token_contract_address)
                        # bscscan_api_key = config.bsc_api  # Replace with your BSCScan API key
                        # token_info = get_token_info(token_contract_address, bscscan_api_key)
                        #
                        # if token_info:
                        #     token_name = token_info.get('name', '')
                        #     token_symbol = token_info.get('symbol', '')
                        #     print(style.GREEN + f"METHOD----- {arr[-1]} (Name: {token_name}, Symbol: {token_symbol})")
                        # else:
                        #     print(style.GREEN + "METHOD-----", arr[-1])
                        if arr[-1] == "addLiquidityETH":
                            webbrowser.open('https://bscscan.com/tx/' + tx_hash)

                    # if to == pcsRouter:
                    #     #current_block = web3.eth.blockNumber
                    #
                    #     print(style.YELLOW+"PANCAKESWAP-------MEMEPOOL")
                    #     decoded = pcsContract.decode_function_input(data)
                    #     print("Decoded",decoded)
                    #     count+=1
                    #     print('https://bscscan.com/tx/' + tx_hash, ": Count",count)
                    #     print(decoded)
                    #     for swapFunc in range(len(swap_functions)):
                    #         if swap_functions[swapFunc] in str(decoded[0]):
                    #             arr.append(swap_functions[swapFunc])
                    #
                    #
                    #     print(style.GREEN+"METHOD-----",arr[-1] )
                    #     if arr[-1] =="addLiquidityETH":
                    #         webbrowser.open('https://bscscan.com/tx/' + tx_hash  )




                    else:
                        #print(style.RED+"NO Router match")
                        pass
                else:
                     pass




    except Exception as e:
        print(f'Error occurred: {e}')
        x = True








