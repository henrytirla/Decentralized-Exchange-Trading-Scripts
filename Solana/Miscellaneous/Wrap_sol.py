import asyncio

import base58
from solana.rpc.api import Client
from solana.rpc.api import Keypair
from solana.transaction import Transaction
from solders.compute_budget import set_compute_unit_price, set_compute_unit_limit
from solders.system_program import transfer, TransferParams
from solders.pubkey import Pubkey
from spl.token.instructions import create_associated_token_account, SyncNativeParams
from spl.token.constants import WRAPPED_SOL_MINT, TOKEN_PROGRAM_ID, ASSOCIATED_TOKEN_PROGRAM_ID
from spl.token.instructions import sync_native
from solana.rpc.commitment import Commitment, Confirmed
from solana.rpc.async_api import AsyncClient


# Initialize Solana client
solana_client = Client("https://api.mainnet-beta.solana.com") #Didn't test with this api but helius should work fine

private_key_string = "YOUR_PRIVATE_KEY HERE"
private_key_bytes = base58.b58decode(private_key_string)
payer = Keypair.from_bytes(private_key_bytes)
print(payer.pubkey())
#creates WSOL token account
sol_ass= create_associated_token_account(payer.pubkey(),owner=payer.pubkey(),mint=WRAPPED_SOL_MINT)

wsol_token_account= sol_ass.accounts[1].pubkey
# Amount of SOL to wrap (in lamports, 1 SOL = 1,000,000,000 lamports)
amount_to_wrap = int(0.08 * 10**9)

params_sync = SyncNativeParams(
    program_id=TOKEN_PROGRAM_ID,
    account=wsol_token_account
)

params = TransferParams(
    from_pubkey=payer.pubkey(),
    to_pubkey=wsol_token_account,
    lamports=amount_to_wrap
)

transaction = Transaction()

transaction.add(sol_ass,transfer(params),sync_native(params_sync),set_compute_unit_price(25_854),set_compute_unit_limit(101_337))

transaction.sign(payer)


async_solana_client = AsyncClient("https://api.mainnet-beta.solana.com")



async def send_and_confirm_transaction(client, transaction, payer, max_attempts=3):
    async with AsyncClient("ws://api.mainnet-beta.solana.com", commitment=Confirmed) as async_client:
        attempts = 0
        while attempts < max_attempts:
            txid = await async_client.send_transaction(transaction, payer)
            try:
                await asyncio.wait_for(async_client.confirm_transaction(txid.value, commitment=Confirmed), timeout=40)
                print(f"Transaction signature: https://solscan.io/tx/{txid.value}")
                print("Transaction confirmed")
                break # Exit the loop if the transaction is confirmed
            except asyncio.TimeoutError:
                attempts += 1
                print(f"Attempt {attempts}: Transaction not confirmed within 20 seconds. Attempting to resend.")
                print(f"Transaction signature: https://solscan.io/tx/{txid.value}")
        if attempts == max_attempts:
            print("Maximum attempts reached. Transaction could not be confirmed.")


asyncio.run(send_and_confirm_transaction(async_solana_client, transaction, payer))
