#Get all token accounts of a wallet address

import asyncio
import time
from datetime import datetime, timezone
from solana.rpc.api import Client, Keypair
from solders.pubkey import Pubkey
from solana.rpc.types import MemcmpOpts
from solders.signature import Signature
from solana.rpc import types
from solana.rpc.async_api import AsyncClient


def unix_to_readable(unix_time):
    # Calculate the total seconds
    total_seconds = unix_time
    datetime_obj = datetime.utcfromtimestamp(total_seconds)
    current_time = datetime.utcnow()
    # Calculate the time difference
    time_difference = current_time - datetime_obj
    days = time_difference.days
    hours, remainder = divmod(time_difference.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    # return f"{days} days, {hours} hours, {minutes} minutes, {seconds} seconds"
    return days


async def get_token_accounts(wallet_address: str):
    solana_client = AsyncClient("Enter your API URL here")
    owner = Pubkey.from_string(wallet_address)
    opts = types.TokenAccountOpts(program_id=Pubkey.from_string("TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA"))
    response = await solana_client.get_token_accounts_by_owner(owner, opts)
    return response.value

wallet_address = "Enter Solana Wallet Address here"
token_accounts=asyncio.run(get_token_accounts(wallet_address))
print(len(token_accounts))
solana_client=Client("Enter your API URL here")
token_account_times = []
for token_account in token_accounts:
    sig = solana_client.get_signatures_for_address(token_account.pubkey, limit=500)
    if sig.value:
        block_time = solana_client.get_transaction(sig.value[-1].signature, encoding="jsonParsed",
                                                    max_supported_transaction_version=0).value.block_time
        transaction_time =  unix_to_readable(block_time)
        token_account_times.append((token_account.pubkey, transaction_time))
sorted_token_accounts = sorted(token_account_times, key=lambda x: x[1])
for pubkey, transaction_time in sorted_token_accounts:
    print(f"Token Account: {pubkey}, Last Transaction: {transaction_time}")