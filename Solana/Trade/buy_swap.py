import asyncio
import datetime
import time
from solana.rpc.types import TokenAccountOpts
from solders.pubkey import Pubkey
from solana.rpc.commitment import Commitment, Confirmed, Finalized
from solana.rpc.api import RPCException
from solana.rpc.api import Client, Keypair
from solana.rpc.async_api import AsyncClient
from solders.compute_budget import set_compute_unit_price,set_compute_unit_limit
from spl.token.instructions import create_associated_token_account, get_associated_token_address, close_account, \
    CloseAccountParams
from create_close_account import  fetch_pool_keys,  make_swap_instruction
from spl.token.client import Token
from spl.token.core import _TokenCore

from dotenv import dotenv_values
config = dotenv_values(".env")

async_solana_client= AsyncClient(config["RPC_HTTPS_URL"]) #Enter your API KEY in .env file

solana_client = Client(config["RPC_HTTPS_URL"])

LAMPORTS_PER_SOL = 1000000000
MAX_RETRIES = 5
RETRY_DELAY = 3

#You can use getTimeStamp With Print Statments to evaluate How fast your transactions are confirmed

def getTimestamp():
    while True:
        timeStampData = datetime.datetime.now()
        currentTimeStamp = "[" + timeStampData.strftime("%H:%M:%S.%f")[:-3] + "]"
        return currentTimeStamp


async def get_transaction_with_timeout(client, txid, commitment=Confirmed, timeout=10):
    # Wrap the synchronous get_transaction call in a coroutine
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(None, client.get_transaction, txid, "json")

async def get_token_account(ctx,
                                owner: Pubkey.from_string,
                                mint: Pubkey.from_string):
        try:
            account_data = await ctx.get_token_accounts_by_owner(owner, TokenAccountOpts(mint))
            return account_data.value[0].pubkey, None
        except:
            swap_associated_token_address = get_associated_token_address(owner, mint)
            swap_token_account_Instructions = create_associated_token_account(owner, owner, mint)
            return swap_associated_token_address, swap_token_account_Instructions

async def buy(solana_client, TOKEN_TO_SWAP_BUY, payer, amount):

    retry_count = 0
    while retry_count < MAX_RETRIES:
        try:
            # token_symbol, SOl_Symbol = getSymbol(TOKEN_TO_SWAP_BUY)
            mint = Pubkey.from_string(TOKEN_TO_SWAP_BUY)
            pool_keys = fetch_pool_keys(str(mint))
            amount_in = int(amount * LAMPORTS_PER_SOL)
            accountProgramId = solana_client.get_account_info_json_parsed(mint)
            TOKEN_PROGRAM_ID = accountProgramId.value.owner

            balance_needed = Token.get_min_balance_rent_for_exempt_for_account(solana_client)
            swap_associated_token_address, swap_token_account_Instructions = await get_token_account(async_solana_client,payer.pubkey(),mint)
            WSOL_token_account, swap_tx, payer, Wsol_account_keyPair, opts, = _TokenCore._create_wrapped_native_account_args(
                TOKEN_PROGRAM_ID, payer.pubkey(), payer, amount_in,
                False, balance_needed, Commitment("confirmed"))

            instructions_swap = make_swap_instruction(amount_in,
                                                      WSOL_token_account,
                                                      swap_associated_token_address,
                                                      pool_keys,
                                                      mint,
                                                      solana_client,
                                                      payer)
            params = CloseAccountParams(account=WSOL_token_account, dest=payer.pubkey(), owner=payer.pubkey(),
                                        program_id=TOKEN_PROGRAM_ID)
            closeAcc = (close_account(params))
            if swap_token_account_Instructions != None:
                # recent_blockhash = solana_client.get_latest_blockhash(Commitment("confirmed"))
                recent_blockhash = solana_client.get_latest_blockhash(commitment="confirmed")

                swap_tx.recent_blockhash = recent_blockhash.value.blockhash
                swap_tx.add(swap_token_account_Instructions)

            #compute unit price and comute unit limit gauge your gas fees more explanations on how to calculate in a future article

            swap_tx.add(instructions_swap,set_compute_unit_price(25_232),set_compute_unit_limit(200_337),closeAcc)
            txn = solana_client.send_transaction(swap_tx, payer,Wsol_account_keyPair)
            txid_string_sig = txn.value
            if txid_string_sig:
                print("Waiting For Transaction Confirmation .......")

                print(f"Transaction Signature: https://solscan.io/tx/{txid_string_sig}")
                # Await transaction confirmation with a timeout
                await asyncio.wait_for(
                    get_transaction_with_timeout(solana_client, txid_string_sig, Commitment("confirmed"), timeout=10),
                    timeout=15
                )
                print("Transaction Confirmed")
                # return txid_string_sig
                return True
        except asyncio.TimeoutError:
            print("Transaction confirmation timed out. Retrying...")
            retry_count += 1
            time.sleep(RETRY_DELAY)
        except RPCException as e:
            print(f"RPC Error: [{e.args[0].message}]... Retrying...")
            retry_count += 1
            time.sleep(RETRY_DELAY)
        except Exception as e:
            print(f"Unhandled exception: {e}. Retrying...")
            retry_count = MAX_RETRIES
            return False

    print("Failed to confirm transaction after maximum retries.")
    return False



##
async def main():

    token_toBuy="RUpbmGF6p42AAeN1QvhFReZejQry1cLkE1PUYFVVpnL" #Enter token you wish to buy here
    payer = Keypair.from_base58_string(config["PrivateKey"])
    print(payer.pubkey())
    buy_transaction=await buy(solana_client, token_toBuy, payer, 0.01) #Enter amount of sol you wish to spend
    print(buy_transaction)

asyncio.run(main())
