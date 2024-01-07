"V1 Script to get newly created pairs on Raydium    "

from solana.rpc.api import Client

from solders.pubkey import Pubkey
from solders.transaction import Transaction
from solders.signature import Signature
RAYDIUM_PROGRAM_ID = Pubkey.from_string("675kPX9MHTjS2zt1qfr1NYHuzeLXfQM9H24wFSUt1Mp8")

OPENBOOK = Pubkey.from_string("srmqPvymJeFKQ4zGQed1GFppgkRHL9kaELCbyksJtPX")
METADATA_2022_PROGRAM_ID = Pubkey.from_string("META4s4fSmpkTbZoUsgC1oBnWB31vQcmnN8giPw51Zu")