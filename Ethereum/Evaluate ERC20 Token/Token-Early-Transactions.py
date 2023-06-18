"Focus on buys immediately after liquitidy is added"

import requests
import json


api_key = 'QSD4D9KG1NYTX3Y6CPAR62G9FBW16UZ81Z'

# Prompt user to input the token contract address and number of wallets
contract_address = input("Enter the token contract address: ")
num_wallets = int(input("Enter the number of wallets to display: "))

# Define the BscScan API URL
url = f"https://api.etherscan.io/api?module=account&action=tokentx&contractaddress={contract_address}&apikey={api_key}"

# Send a request to BscScan API and parse the JSON response
response = requests.get(url)
data = json.loads(response.text)


if data['status'] == "1":
    transactions = data['result']

    # Filter transactions and get the first 'num_wallets' wallet addresses
    wallets = []
    print(f"\nThe first {num_wallets} wallets that bought the token after liquidity was added:\n")
    for tx in transactions:
        #if tx['from'] != contract_address and tx['to'] != contract_address:
            if tx['from'] not in wallets:
                wallets.append(tx['from'])
                print(f"{len(wallets)}. Wallet: {tx['from']}, TxHash: https://etherscan.io/tx/{tx['hash']}")

                if len(wallets) >= num_wallets:
                    break
        # elif tx['to'] == contract_address.lower(): #and len(wallets) == 1:
        #     print(f"Liquidity added transaction: TxHash: {tx['hash']}\n")
else:
    print("Error fetching transactions. Please check the contract address and try again.")
