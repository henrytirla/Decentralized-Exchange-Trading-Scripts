from web3 import Web3
#https://testnet.bscscan.com/address/0x32f4b44286be50e905cfc5ab16b0a4747f477276
# Node Connection
w3 = Web3(Web3.HTTPProvider('https://data-seed-prebsc-1-s1.binance.org:8545/'))

# Replace these with the sender's private key and the recipient's address
sender_private_key = 'Enter Your Private Key'
recipient_address = w3.toChecksumAddress('Enter Recipient Address')

# Your message
message = 'Enter Your Message'

# Convert the message to hexadecimal data
message_hex = message.encode('utf-8').hex()

# Sender's address
sender_address = w3.toChecksumAddress("Sender's Address")


# Set up the transaction
transaction = {
    'to': recipient_address,
    'value': w3.toWei(0, 'ether'),  # Set the amount of Ether to send
    'gas': 100000,
    'gasPrice': w3.toWei('50', 'gwei'),
    'nonce': w3.eth.getTransactionCount(sender_address),
    'data': '0x' + message_hex,  # Include the message as hexadecimal data
}

# Sign the transaction
signed_transaction = w3.eth.account.signTransaction(transaction, sender_private_key)

# Send the transaction
transaction_hash = w3.eth.sendRawTransaction(signed_transaction.rawTransaction)

print(f'Transaction hash: {transaction_hash.hex()}')

#https://testnet.bscscan.com/tx/0x2803ab01415414661a1ab5bb235d591748affd369fd2a30048c9f76a6f8b028f