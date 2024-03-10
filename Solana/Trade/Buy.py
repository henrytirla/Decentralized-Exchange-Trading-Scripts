
#TODO REFACTIR CODE
from spl.token.instructions import create_associated_token_account, get_associated_token_address
from spl.token.instructions import close_account, CloseAccountParams
from spl.token.client import Token
from solders.pubkey import Pubkey
from solders.instruction import Instruction
from solana.rpc.types import TokenAccountOpts
from solana.transaction import AccountMeta
from construct import Bytes, Int8ul, Int64ul, BytesInteger
from construct import Struct as cStruct
from spl.token.core import _TokenCore

from solana.rpc.commitment import Commitment
from solana.rpc.api import RPCException
from solana.rpc.api import Client, Keypair
from solders.compute_budget import set_compute_unit_price,set_compute_unit_limit

import base58

from solders.signature import Signature
from dexscreener import getSymbol
from layouts import SWAP_LAYOUT


solana_client = Client("https://api.mainnet-beta.solana.com")

LAMPORTS_PER_SOL = 1000000000
AMM_PROGRAM_ID = Pubkey.from_string('675kPX9MHTjS2zt1qfr1NYHuzeLXfQM9H24wFSUt1Mp8')
SERUM_PROGRAM_ID = Pubkey.from_string('srmqPvymJeFKQ4zGQed1GFppgkRHL9kaELCbyksJtPX')



def get_token_account(ctx,
                      owner: Pubkey.from_string,
                      mint: Pubkey.from_string):
    try:
        account_data = ctx.get_token_accounts_by_owner(owner, TokenAccountOpts(mint))
        return account_data.value[0].pubkey, None
    except:
        swap_associated_token_address = get_associated_token_address(owner, mint)
        swap_token_account_Instructions = create_associated_token_account(owner, owner, mint)
        return swap_associated_token_address, swap_token_account_Instructions

myWallet= Pubkey.from_string("En5z1QWHbUtWdd54mdK1QVEBSpvDwejZDkroFAbccXbD")
mint_address= Pubkey.from_string("Gzwy4DrmumZAG4Mu5m6S2uSKVyZ9GQ3GMAgmTsX4a1kq") #Tyler token
accountProgramId = solana_client.get_account_info_json_parsed(Pubkey.from_string("Gzwy4DrmumZAG4Mu5m6S2uSKVyZ9GQ3GMAgmTsX4a1kq"))
# print(accountProgramId.value.owner)
# print(get_token_account(solana_client, myWallet, mint_address))

from create_close_account import get_token_account, fetch_pool_keys, get_token_account, make_swap_instruction
from dexscreener import getSymbol
# from webhook import sendWebhook

import time

LAMPORTS_PER_SOL = 1000000000


def buy(solana_client, TOKEN_TO_SWAP_BUY, payer, amount):
    token_symbol, SOl_Symbol = getSymbol(TOKEN_TO_SWAP_BUY)

    mint = Pubkey.from_string(TOKEN_TO_SWAP_BUY)

    pool_keys = fetch_pool_keys(str(mint))
    # print("Pool Keys: ", pool_keys)
    if pool_keys == "failed":
        print(f"a|BUY Pool ERROR {token_symbol} ", f"[Raydium]: Pool Key Not Found")
        return "failed"

    """
    Calculate amount
    """
    amount_in = int(amount * LAMPORTS_PER_SOL)
    # slippage = 0.1
    # lamports_amm = amount * LAMPORTS_PER_SOL
    # amount_in =  int(lamports_amm - (lamports_amm * (slippage/100)))

    txnBool = True
    while txnBool:

        """Get swap token program id"""
        print("1. Get TOKEN_PROGRAM_ID...")
        accountProgramId = solana_client.get_account_info_json_parsed(mint)
        TOKEN_PROGRAM_ID = accountProgramId.value.owner

        """
        Set Mint Token accounts addresses
        """
        print("2. Get Mint Token accounts addresses...")
        swap_associated_token_address, swap_token_account_Instructions = get_token_account(solana_client,
                                                                                           payer.pubkey(), mint)

        """
        Create Wrap Sol Instructions
        """
        print("3. Create Wrap Sol Instructions...")
        balance_needed = Token.get_min_balance_rent_for_exempt_for_account(solana_client)
        WSOL_token_account, swap_tx, payer, Wsol_account_keyPair, opts, = _TokenCore._create_wrapped_native_account_args(
            TOKEN_PROGRAM_ID, payer.pubkey(), payer, amount_in,
            False, balance_needed, Commitment("confirmed"))
        """
        Create Swap Instructions
        """
        print("4. Create Swap Instructions...")
        instructions_swap = make_swap_instruction(amount_in,
                                                  WSOL_token_account,
                                                  swap_associated_token_address,
                                                  pool_keys,
                                                  mint,
                                                  solana_client,
                                                  payer
                                                  )
        # print(instructions_swap)

        print("5. Create Close Account Instructions...")
        params = CloseAccountParams(account=WSOL_token_account, dest=payer.pubkey(), owner=payer.pubkey(),
                                    program_id=TOKEN_PROGRAM_ID)
        closeAcc = (close_account(params))

        print("6. Add instructions to transaction...")
        if swap_token_account_Instructions != None:
            swap_tx.add(swap_token_account_Instructions)
        swap_tx.add(set_compute_unit_price(1_000)) #Set your gas fees here in micro_lamports eg 1_000_000 ,20_400_000 choose amount in sol and multiply by microlamport eg 1000000000 =1 lamport 

        swap_tx.add(instructions_swap)
        swap_tx.add(closeAcc)

        try:
            print("7. Execute Transaction...")
            start_time = time.time()
            txn = solana_client.send_transaction(swap_tx, payer, Wsol_account_keyPair)
            txid_string_sig = txn.value
            print("Here is the Transaction Signature NB Confirmation is just to wat for confirmation: ", txid_string_sig)

            print("8. Confirm transaction...")
            break
            checkTxn = True
            while checkTxn:
                # status = solana_client.get_transaction(txid_string_sig, "json")
                # print( status.value.transaction.meta.err )


                try:
                    status = solana_client.get_transaction(txid_string_sig, "json")
                    FeesUsed = (status.value.transaction.meta.fee) / 1000000000
                    # print(status.value.transaction)
                    # print("STATUS", status.value.transaction.meta.err)

                    if status.value.transaction.meta.err==None:
                        print("[create_account] Transaction Success", txn.value)
                        print(f"[create_account] Transaction Fees: {FeesUsed:.10f} SOL")

                        end_time = time.time()
                        execution_time = end_time - start_time
                        print(f"Execution time: {execution_time} seconds")

                        txnBool = False
                        checkTxn = False
                        return txid_string_sig

                    else:
                        print("Transaction Failed")
                        end_time = time.time()
                        execution_time = end_time - start_time
                        print(f"Execution time: {execution_time} seconds")
                        checkTxn = False

                except Exception as e:
                    print(f"e|BUY ERROR {token_symbol}", f"[Raydium]: {e}")
                    # print("STATUS",status.value.transaction.meta.err)
                    print("Sleeping...", e)
                    time.sleep(0.500)
                    print("Retrying...")

        except RPCException as e:
            print(f"Error: [{e.args[0].message}]...\nRetrying...")

            print(f"e|BUY ERROR ", f"[Raydium]: {e.args[0].message}")
            time.sleep(1)

        except Exception as e:
            print(f"e|BUY Exception ERROR {token_symbol} ", f"[Raydium]: {e}")
            print(f"Error: [{e}]...\nEnd...")
            txnBool = False
            return "failed"

token_toBuy=input("Enter token to buy: ")
payer = Keypair.from_base58_string("Enter String Private Key")
print(payer.pubkey())
#0.004960
#0.0001
buy(solana_client, token_toBuy, payer, 0.004960)
