
from web3 import Web3
import secrets
import csv
import os

# Connect to the Binance blockchain using the Infura node
web3 = Web3(Web3.HTTPProvider("https://bsc-dataseed1.binance.org/"))

# Define the number of addresses to generate
num_addresses = 10

# Define the filename
filename = "addresses_and_keys.csv"

# Check if the file exists; if not, create it and write the header row
if not os.path.exists(filename):
    with open(filename, "w", newline='') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csvwriter.writerow(['Enumeration', 'Address', 'Private Key'])

# Open the CSV file in append mode to store the new addresses and private keys
with open(filename, "a", newline='') as csvfile:
    # Create a CSV writer object
    csvwriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    # Get the current enumeration value from the file
    with open(filename, "r") as csvfile_read:
        enumeration = sum(1 for _ in csvfile_read) - 1  # Subtract 1 for the header row

    # Generate the addresses and private keys
    for i in range(num_addresses):
        extra_security = secrets.token_hex(32)
        # Generate a new Binance address and private key
        address = web3.eth.account.create(extra_security)

        # Print the address and private key
        print(f"Address: {address.address}")
        print(f"Private key: {address.privateKey.hex()}")

        # Write the enumeration, address, and private key to the CSV file
        csvwriter.writerow([enumeration + i + 1, address.address, address.privateKey.hex()])





"""Object Oriented Implementation """

# from web3 import Web3
# import secrets
# import csv
# import os
#
#
# class BinanceAddressGenerator:
#     def __init__(self, num_addresses=10, filename="addresses_and_keys.csv"):
#         self.web3 = Web3(Web3.HTTPProvider("https://bsc-dataseed1.binance.org/"))
#         self.num_addresses = num_addresses
#         self.filename = filename
#
#     def generate_address(self):
#         extra_security = secrets.token_hex(32)
#         return self.web3.eth.account.create(extra_security)
#
#     def save_addresses_to_csv(self, addresses):
#         if not os.path.exists(self.filename):
#             with open(self.filename, "w", newline='') as csvfile:
#                 csvwriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
#                 csvwriter.writerow(['Enumeration', 'Address', 'Private Key'])
#
#         with open(self.filename, "a", newline='') as csvfile:
#             csvwriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
#
#             with open(self.filename, "r") as csvfile_read:
#                 enumeration = sum(1 for _ in csvfile_read) - 1
#
#             for i, address in enumerate(addresses):
#                 csvwriter.writerow([enumeration + i + 1, address.address, address.privateKey.hex()])
#
#     def generate_and_save_addresses(self):
#         addresses = [self.generate_address() for _ in range(self.num_addresses)]
#         self.save_addresses_to_csv(addresses)
#         return addresses
#
#
# if __name__ == "__main__":
#     generator = BinanceAddressGenerator(num_addresses=10)
#     generated_addresses = generator.generate_and_save_addresses()
#
#     for address in generated_addresses:
#         print(f"Address: {address.address}")
#         print(f"Private key: {address.privateKey.hex()}")
