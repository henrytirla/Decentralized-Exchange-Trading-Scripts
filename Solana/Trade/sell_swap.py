import asyncio
import datetime
import time
from solana.rpc.types import TokenAccountOpts
from solders.keypair import Keypair
from solders.pubkey import Pubkey
from solana.rpc.commitment import Confirmed, Finalized, Commitment
from solana.rpc.api import RPCException
from solana.rpc.api import Client
from solders.compute_budget import set_compute_unit_price,set_compute_unit_limit
from solders.transaction import Transaction
from spl.token.instructions import CloseAccountParams, close_account
from create_close_account import fetch_pool_keys, get_token_account, make_swap_instruction ,sell_get_token_account
from dexscreener import getSymbol
from solana.transaction import Transaction
from spl.token.constants import WRAPPED_SOL_MINT

from dotenv import dotenv_values
config = dotenv_values(".env")
RPC_HTTPS_URL = (config["RPC_HTTPS_URL"])




solana_client = Client(RPC_HTTPS_URL) #Enter your API KEY

LAMPORTS_PER_SOL = 1000000000
MAX_RETRIES = 5
RETRY_DELAY = 3


def getTimestamp():
    while True:
        timeStampData = datetime.datetime.now()
        currentTimeStamp = "[" + timeStampData.strftime("%H:%M:%S.%f")[:-3] + "]"
        return currentTimeStamp


async def get_transaction_with_timeout(client, txid, commitment=Confirmed, timeout=10):
    # Wrap the synchronous get_transaction call in a coroutine
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(None, client.get_transaction, txid, "json")



async def sell_normal(solana_client, TOKEN_TO_SWAP_SELL, payer):
    retry_count = 0
    while retry_count < MAX_RETRIES:
        try:
            # token_symbol, SOl_Symbol = getSymbol(TOKEN_TO_SWAP_SELL)
            mint = Pubkey.from_string(TOKEN_TO_SWAP_SELL)
            sol= WRAPPED_SOL_MINT
            TOKEN_PROGRAM_ID = solana_client.get_account_info_json_parsed(mint).value.owner
            pool_keys = fetch_pool_keys(str(mint))
            accountProgramId = solana_client.get_account_info_json_parsed(mint)
            programid_of_token = accountProgramId.value.owner
            accounts = solana_client.get_token_accounts_by_owner_json_parsed(payer.pubkey(), TokenAccountOpts(
                program_id=programid_of_token)).value
            for account in accounts:
                mint_in_acc = account.account.data.parsed['info']['mint']
                if mint_in_acc == str(mint):
                    amount_in = int(account.account.data.parsed['info']['tokenAmount']['amount'])
                    print("Your Token Balance is: ", amount_in)
                    break

            swap_token_account = sell_get_token_account(solana_client, payer.pubkey(), mint)
            WSOL_token_account, WSOL_token_account_Instructions = get_token_account(solana_client, payer.pubkey(), sol)
            print(amount_in)

            print("3. Create Swap Instructions...")
            instructions_swap = make_swap_instruction(amount_in,
                                                      swap_token_account,
                                                      WSOL_token_account,
                                                      pool_keys,
                                                      mint,
                                                      solana_client,
                                                      payer
                                                      )
            params = CloseAccountParams(account=WSOL_token_account, dest=payer.pubkey(), owner=payer.pubkey(),
                                        program_id=TOKEN_PROGRAM_ID)
            closeAcc = (close_account(params))
            swap_tx = Transaction()
            if WSOL_token_account_Instructions != None:
                recent_blockhash = solana_client.get_latest_blockhash(commitment="confirmed")
                swap_tx.recent_blockhash = recent_blockhash.value.blockhash
                swap_tx.add(WSOL_token_account_Instructions)

            #Modify Compute Unit Limit and Price Accordingly  to your Gas Preferences
            swap_tx.add(instructions_swap,set_compute_unit_price(25_232),set_compute_unit_limit(200_337))
            swap_tx.add(closeAcc)
            # Execute Transaction
            txn = solana_client.send_transaction(swap_tx, payer)
            txid_string_sig = txn.value
            if txid_string_sig:
                print(f"Transaction Signature: https://solscan.io/tx/{txid_string_sig}")
                # Await transaction confirmation with a timeout
                await asyncio.wait_for(
                    get_transaction_with_timeout(solana_client, txid_string_sig, commitment="confirmed", timeout=10),
                    timeout=15
                )
                print("Transaction Confirmed")
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
            # retry_count= MAX_RETRIES
            retry_count+= 1
            time.sleep(RETRY_DELAY)

            # return False
    print("Failed to confirm transaction after maximum retries.")
    return False

async def main():

    token_toBuy="RUpbmGF6p42AAeN1QvhFReZejQry1cLkE1PUYFVVpnL"
    payer = Keypair.from_base58_string(config['PrivateKey'])
    print(payer.pubkey())
    await sell_normal(solana_client, token_toBuy, payer)

asyncio.run(main())