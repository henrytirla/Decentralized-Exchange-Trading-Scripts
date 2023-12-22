from solana.rpc.api import Client, Keypair
import base58

client = Client("Enter Your Alchemy Node API")

new_account = Keypair()
#print(new_account.pubkey(), new_account.secret())

private_key_bytes = new_account.secret()


# Convert bytes to hexadecimal string
hex_string = private_key_bytes.hex()

# Encode the hexadecimal string to base58
base58_private_key = base58.b58encode(bytes.fromhex(hex_string)).decode('utf-8')

print("Wallet Address:",new_account.pubkey())
print("Readable private key to Import on Browser Wallet:", base58_private_key)

#TODO: Fix compatibiltiy with Phantom Wallet