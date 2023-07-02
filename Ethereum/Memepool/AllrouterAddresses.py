"Scan Memepool for all router addresses."

#DoingNOW
#Get Inputs and feed it to the decode_input
#Handle each input sequentially

import asyncio
from web3 import Web3
import json
from eth_abi import decode_abi

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

w3 = Web3(Web3.HTTPProvider("https://mainnet.infura.io/v3/b28812c62af1405e90af0ee79ea42a41"))


uniswap_router_addresses = [
    '0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D',  # Uniswap V2 Router
    '0xE592427A0AEce92De3Edee1F18E0157C05861564',  # Uniswap V3 Router
    '0x68b3465833fb72A70ecDF485E0e4C7bD8665Fc45',  # Uniswap V3 02 Router
    '0xEf1c6E67703c7BD7107eed8303Fbe6EC2554BF6B', # Old Universal Router
    '0x3fC91A3afd70395Cd496C647d5a6CC9D4B2b7FAD', #Universal Router

]



def decode_input_data(input_data, router):
    with open("router_abi.json") as f:
        routers_abi = json.load(f)
    #print(routers_abi)


    abi = routers_abi.get(router)
    #print(abi)

    if abi is None:
        raise ValueError("ABI not found for the specified router.")

    contract = w3.eth.contract(address=router, abi=abi)
    decoded_data = contract.decode_function_input(input_data)
    decoded_str = str(decoded_data[0])
    start_index = decoded_str.find(" ") + 1
    end_index = decoded_str.find("(")
    function_name = decoded_str[start_index:end_index]
    print(style.CYAN+function_name)

    return decoded_data


async def handle_new_block(block):
    for tx_hash in block['transactions']:
        try:
            tx = w3.eth.getTransaction(tx_hash)

            for router_address in uniswap_router_addresses:
                if tx['to'].lower() == router_address.lower():
                    # Process the transaction
                    #decoded_input_data = decode_input_data(tx['input'])
                    #tx_hash = w3.toHex(tx)
                    hash= tx['hash']
                    tx_hash = w3.toHex(hash)
                    #print(tx_hash)
                    print(style.YELLOW+"Transaction interacting with Uniswap Router:", tx['to'], "Tx_Hash: ",w3.toHex(hash))
                    print(style.GREEN+"Decoded Input Data:", decode_input_data(tx['input'],tx['to']))
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