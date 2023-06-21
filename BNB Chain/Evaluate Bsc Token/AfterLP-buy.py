
"""
You actually see early transactions of a project and it's a high determinant of it's success
You just have to know what to fine
This script can help you spot good wallets to follow.

"""
import requests
import json


api_key = 'KFEM9CQIBQVGZWTDGW5VDZGSM5ZYVGJ6KR'

# Prompt user to input the token contract address and number of wallets
contract_address = input("Enter the token contract address: ")
num_wallets = int(input("Enter the number of wallets to display: "))

# Define the BscScan API URL
url = f"https://api.bscscan.com/api?module=account&action=tokentx&contractaddress={contract_address}&apikey={api_key}"

# Send a request to BscScan API and parse the JSON response
response = requests.get(url)
data = json.loads(response.text)

if data['status'] == "1":
    transactions = data['result']

    # Filter transactions and get the first 'num_wallets' wallet addresses
    wallets = []
    print(f"\nThe first {num_wallets} wallets that bought the token after liquidity was added:\n")
    for tx in transactions:
        if tx['from'] != contract_address and tx['to'] != contract_address:
            if tx['from'] not in wallets:
                wallets.append(tx['from'])
                print(f"{len(wallets)}. Wallet: {tx['from']}, TxHash: https://bscscan.com/tx/{tx['hash']}")

                if len(wallets) >= num_wallets:
                    break
        elif tx['to'] == contract_address.lower(): #and len(wallets) == 1:
            print(f"Liquidity added transaction: TxHash: {tx['hash']}\n")
else:
    print("Error fetching transactions. Please check the contract address and try again.")
