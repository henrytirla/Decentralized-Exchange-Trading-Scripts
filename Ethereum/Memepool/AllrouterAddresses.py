"Scan Memepool for all router addresses."

#DoingNOW


import asyncio
from web3 import Web3
from eth_abi import decode_abi

w3 = Web3(Web3.HTTPProvider("Enter your node"))

uniswap_router_addresses = [
    '0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D',  # Uniswap V2 Router
    '0x1b02dA8Cb0d097eB8D57A175b88c7D8b47997506',  # Uniswap V3 Router
    '0x68b3465833fb72A70ecDF485E0e4C7bD8665Fc45',  # Uniswap V3 02 Router
    '0xEf1c6E67703c7BD7107eed8303Fbe6EC2554BF6B', # Old Universal Router
    '0x3fC91A3afd70395Cd496C647d5a6CC9D4B2b7FAD', #Universal Router

]

def decode_input_data(input_data):
    # Perform decoding of input data here
    #Todo
    decoded_data = decode_abi(['...'], input_data)
    return decoded_data

async def handle_new_block(block):
    for tx_hash in block['transactions']:
        try:
            tx = w3.eth.getTransaction(tx_hash)

            for router_address in uniswap_router_addresses:
                if tx['to'].lower() == router_address.lower():
                    # Process the transaction
                    #decoded_input_data = decode_input_data(tx['input'])
                    print("Transaction interacting with Uniswap Router:", tx)
                    #print("Decoded Input Data:", decoded_input_data)
                    print("---")
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