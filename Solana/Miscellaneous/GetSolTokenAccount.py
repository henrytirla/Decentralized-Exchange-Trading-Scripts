#Get the Sol token account of a wallet address
import asyncio
import sys

from solders.pubkey import Pubkey
from solana.rpc.async_api import AsyncClient
from solana.rpc.types import TokenAccountOpts

wallet_address = "" #Enter Wallet Address
mint_address = "So11111111111111111111111111111111111111112"

async def get_specific_token_account(owner_pubkey: str, mint_pubkey: str):
    async with AsyncClient("https://api.mainnet-beta.solana.com") as client:
        owner_pubkey_obj = Pubkey.from_string(owner_pubkey)
        mint_pubkey_obj = Pubkey.from_string(mint_pubkey)
        # Using get_token_accounts_by_owner to fetch token accounts
        opts = TokenAccountOpts(mint=mint_pubkey_obj)
        response = await client.get_token_accounts_by_owner(owner_pubkey_obj, opts)
        if response:
            return response.value[0].pubkey  # Return the first account found
    return None

async def main():
    account = await get_specific_token_account(wallet_address, mint_address)
    if account:
        print("Found account:", account)
    else:
        print("No account found for the given mint address.")

if __name__ == "__main__":
    asyncio.run(main())
