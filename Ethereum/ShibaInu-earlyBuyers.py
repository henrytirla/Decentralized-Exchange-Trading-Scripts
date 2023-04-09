import requests
import csv
import os

"Too many sold, Too Early they could have been Centi Millionaires."

# Your Etherscan API key
etherscan_api_key = 'Your Ether Scan API'

# SHIB contract address or Any other Contract You want to see early buys
token_contract_address = '0x95ad61b0a150d79219dcf64e1e6cc01f0b64c4ce'

#Number of initial Buys transactions
txn_number = 1001
# Fetch the first 30 transactions
url = f'https://api.etherscan.io/api?module=account&action=tokentx&contractaddress={token_contract_address}&page=1&offset={txn_number}&sort=asc&apikey={etherscan_api_key}'
response = requests.get(url)

csv_filename = 'early-token-transactions.csv'

# Check if the CSV file exists, if not create it and write the header
if not os.path.exists(csv_filename):
    with open(csv_filename, 'w', newline='') as csvfile:
        fieldnames = ['Enumeration', 'To', 'Value', 'Hash']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

# Check if the request was successful
if response.status_code == 200:
    data = response.json()

    if data['status'] == '1' and data['message'] == 'OK':
        transactions = data['result']

        # Open the CSV file and write the transaction data
        #transaction_count = 1
        with open(csv_filename, 'a', newline='') as csvfile:
            fieldnames = ['Enumeration', 'To', 'Value', 'Hash']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            for i,tx in enumerate(transactions):
                # Check if the transaction is a "buy" transaction
                if tx['from'] == "0x811beed0119b4afce20d2583eb608c6f7af1954f":
                    #etherscan_tx_url = 'https://etherscan.io/tx/'+tx["hash"]
                    writer.writerow({
                        'Enumeration': i+1,
                        'To': tx['to'],
                        'Value': tx['value'],
                        'Hash': tx['hash'],
                    })
                    #transaction_count+=1

    else:
        print('Error fetching transactions:', data['message'])
else:
    print('Error fetching transactions. Status code:', response.status_code)

