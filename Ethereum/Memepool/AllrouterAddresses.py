"Scan Memepool for all router addresses."



import asyncio
from web3 import Web3
import json
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

w3 = Web3(Web3.HTTPProvider("Enter your nodes"))


uniswap_router_addresses = [
    '0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D',  # Uniswap V2 Router
    '0xE592427A0AEce92De3Edee1F18E0157C05861564',  # Uniswap V3 Router
    '0x68b3465833fb72A70ecDF485E0e4C7bD8665Fc45',  # Uniswap V3 02 Router
    '0xEf1c6E67703c7BD7107eed8303Fbe6EC2554BF6B', # Old Universal Router
    '0x3fC91A3afd70395Cd496C647d5a6CC9D4B2b7FAD', #Universal Router


]

check_functions = {"swapETHForExactTokens": True, "swapExactETHForTokens": True,
                   "swapExactETHForTokensSupportingFeeOnTransferTokens": True, "addLiquidityETH": True,
                   'multicall': True, 'execute': True}


def get_FunctionName(decoded_data):
    decoded_str = str(decoded_data[0])
    start_index = decoded_str.find(" ") + 1
    end_index = decoded_str.find("(")
    function_name = decoded_str[start_index:end_index]
    return function_name

# uniswap_v3_path = b"\xc0*\xaa9\xb2#\xfe\x8d\n\x0e ... \xd7\x89"  # bytes or str hex
# fn_name = "V3_SWAP_EXACT_IN"  # Or V3_SWAP_EXACT_OUT
# codec = RouterCodec()
# decoded_path = codec.decode.v3_path(fn_name, uniswap_v3_path)
def decode_execute(decode_data):
    codec = RouterCodec()
    decoded_trx_input = codec.decode.function_input(decode_data)
    In_put = decoded_trx_input[1]['inputs'][1]
    fn_name= get_FunctionName(In_put)
    print(fn_name)
    if fn_name == 'V3_SWAP_EXACT_IN':
       #fn_name = "V3_SWAP_EXACT_IN"
       print(decoded_trx_input)
       path = In_put[1]['path']
       decoded_path = codec.decode.v3_path(fn_name, path)
       return fn_name,decoded_path
    elif fn_name == 'V2_SWAP_EXACT_IN':
         print(decoded_trx_input)
         v2_path= In_put[1]['path']
         return v2_path
    elif fn_name == "UNWRAP_WETH":
         print(decoded_trx_input)
         data= decoded_trx_input[1]['inputs'][0][1]['path']
         return fn_name,data








def decode_input_data(input_data, router):
    with open("router_abi.json") as f:
        routers_abi = json.load(f)
    abi = routers_abi.get(router)

    if abi is None:
        raise ValueError("ABI not found for the specified router.")
    contract = w3.eth.contract(address=router, abi=abi)
    decoded_data = contract.decode_function_input(input_data)


    function_name = get_FunctionName(decoded_data)


    if function_name in check_functions and check_functions[function_name]:
        print(style.CYAN + function_name)
        if function_name == "execute":

            data= decode_execute(input_data)
            # return  SwapExact_in , In_put ,decoded_trx_input
            return data
        elif function_name == "multicall":
            byte_data = decoded_data[1]['data'][0]
            multicall_decoded = contract.decode_function_input(byte_data)
            return multicall_decoded
        else:
            path_ =decoded_data[1]['path']
            return path_
    # else:
    #     return "Pass"








async def handle_new_block(block):
    for tx_hash in block['transactions']:
        try:

            tx = w3.eth.get_transaction(tx_hash)


            for router_address in uniswap_router_addresses:
                if tx['to'] == router_address:
                    hash= tx['hash']
                    tx_hash = w3.to_hex(hash)
                    if tx['to'] == router_address:

                        function_name = decode_input_data(tx['input'], tx['to'])
                        if function_name is not None:
                            print(style.YELLOW + "Transaction interacting with Uniswap Router:", tx['to'], "Tx_Hash: ",
                                  w3.to_hex(hash))

                            print(style.GREEN+f"Decoded Input Data: {function_name}")
                            print(style.RED+"------------------")

        except Exception as e:
            print("An error occurred while processing a transaction:", e)

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
        await asyncio.sleep(5)

# Run the event loop
async def main():
    await track_new_blocks()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())