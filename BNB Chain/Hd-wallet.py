"Generate Wallet from Mnemonic"

from web3 import Web3
from mnemonic import Mnemonic
from web3 import Web3
import secrets
from eth_account import Account


w3 = Web3(Web3.HTTPProvider("https://bsc-dataseed1.binance.org/"))

mnemo = Mnemonic("english")
words = mnemo.generate(strength=256)

extra_security= secrets.token_hex(32)

w3.eth.account.enable_unaudited_hdwallet_features()
#Generated Acct from Mnemonic
acct = Account.from_mnemonic(words,passphrase=extra_security)
acct_privatekeys =w3.toHex(acct.privateKey)
accout = w3.eth.account.privateKeyToAccount(acct_privatekeys)

account_publickey = accout.address
account_privatekey= accout.privateKey

print("MNEMONIC PHRASE--[KEEP PRIVATE]",words)
print('Public Key', account_publickey)
print("Private_Key---[KEEP PRIVATE]",w3.toHex(account_privatekey))