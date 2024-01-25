import base58
from base58  import b58decode, b58encode
from solana.rpc.api import  Keypair

#Wallet Address:  FTvNm4CQPkqcUB6AL9SE5TS8KswCfr9xGj47dzTT24CU
#Private Key:  21T8iLRJpWterSN1ozw4sEoaZ1aYVAQWcWmESisiyjQuEitXNF3PcDJqNxdbx7bTqL9wGQKhAhaMB7JFekmKK2Lk


encoded_pair= "21T8iLRJpWterSN1ozw4sEoaZ1aYVAQWcWmESisiyjQuEitXNF3PcDJqNxdbx7bTqL9wGQKhAhaMB7JFekmKK2Lk"
key_pair= b58decode(encoded_pair)

private_key_bytes = base58.b58decode(encoded_pair)
# Create a Keypair object from the secret key bytes
keypair = Keypair.from_bytes(private_key_bytes)
print(keypair.pubkey())

# private_key= key_pair[:32]
# public_key= key_pair[32:]
#
# print("Wallet Address: ",b58encode(public_key).decode())
#
# # To get the private key from the keypair,
# _keypair= private_key+public_key
# _encoded_keypair= b58encode(_keypair).decode()
# print("Private Key: ",_encoded_keypair)