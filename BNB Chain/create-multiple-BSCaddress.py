
from web3 import Web3

# Connect to the BNB Chain blockchain using your node

web3 = Web3(Web3.HTTPProvider("Enter BSC Node here"))
# Define the number of addresses to generate
num_addresses = 10

# Generate the addresses and private keys
for i in range(num_addresses):
    # Generate a new Ethereum address and private key
    address = web3.eth.account.create()

    # Print the address and private key
    print(f"Address: {address.address}")
    print(f"Private key: {address.privateKey.hex()}")