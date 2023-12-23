from solana.rpc.api import Client, Keypair
import base58
from dotenv import dotenv_values

config = dotenv_values(".env")
client = Client(config["RPC_URL"])  #You can directly use the RPC_URL here without using dotenv

new_account = Keypair()
wallet_address = new_account.pubkey()

private_key_bytes = new_account.secret()
public_key_bytes = bytes(new_account.pubkey())
encoded_keypair= private_key_bytes+public_key_bytes
private_key= base58.b58encode(encoded_keypair).decode()
print("Wallet Address: ",wallet_address)
print("Private Key : ",private_key) #import in phantom wallet

