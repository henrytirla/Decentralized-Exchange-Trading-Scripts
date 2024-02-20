#Decoded Signature To Display Buy and Sell information crucial for copyTrading

#Fixed this for all type of transction......PREMIUM

import asyncio
import datetime
import time
import base58
import httpx
import websockets
import json
from solders.signature import Signature
import requests
from solders.pubkey import Pubkey
from solana.rpc.api import Client, Keypair
from borsh_construct import CStruct, U64
from construct import Bytes, Int8ul, Int32ul, Int64ul, Pass, Switch
PUBLIC_KEY_LAYOUT = Bytes(32)
RAYDIUM_AUTHORITY = Pubkey.from_string("5Q544fKrFoe6tsEbD7S8EmxGTJYAKtTVhAW5Q5pge4j1")
LAMPORTS = 1000000000
SPL_ACCOUNT_LAYOUT = CStruct(
    "mint" / PUBLIC_KEY_LAYOUT,
    "owner" / PUBLIC_KEY_LAYOUT,
    "amount" / U64,
    "delegateOption" / Int32ul,
    "delegate" / PUBLIC_KEY_LAYOUT,
    "state" / Int8ul,
    "isNativeOption" / Int32ul,
    "isNative" / U64,
    "delegatedAmount" / U64,
    "closeAuthorityOption" / Int32ul,
    "closeAuthority" / PUBLIC_KEY_LAYOUT
)
SPL_MINT_LAYOUT = CStruct(
  "mintAuthorityOption"/ Int32ul,
  'mintAuthority'/PUBLIC_KEY_LAYOUT,
  'supply'/U64,
  'decimals'/Int8ul,
  'isInitialized'/Int8ul,
  'freezeAuthorityOption'/Int32ul,
  'freezeAuthority'/PUBLIC_KEY_LAYOUT
)
#sparx78qzrJU1sC2ZnTdWHa3mjZkd4LgaiFgCMavbbH EbNrhZAMjov2jt8tbKqo9KCnUT7iiAaKTDfQ32GAKvsz
#GpDb1yX3o4Zch82qLF7DzvHECQU92SpQ31zESe5QDcHC   EbNrhZAMjov2jt8tbKqo9KCnUT7iiAaKTDfQ32GAKvsz

class style():
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'
#DCAK8tuwzsNowVA6eSojLHhHSDQMyECuSbu7KovyvYbm
wallet_address = "DCAK8tuwzsNowVA6eSojLHhHSDQMyECuSbu7KovyvYbm" #
seen_signatures = set()
WRAPPED_SOL_MINT = "So11111111111111111111111111111111111111112"
Pool_raydium="675kPX9MHTjS2zt1qfr1NYHuzeLXfQM9H24wFSUt1Mp8"
raydium_V4="5Q544fKrFoe6tsEbD7S8EmxGTJYAKtTVhAW5Q5pge4j1"
solana_client= Client("https://api.mainnet-beta.solana.com")


def transactionType(Account: str):
    data = solana_client.get_account_info(Pubkey.from_string(Account)).value.data
    parsed_data = SPL_ACCOUNT_LAYOUT.parse(data)
    mint = Pubkey.from_bytes(parsed_data.mint)
    if mint == Pubkey.from_string(WRAPPED_SOL_MINT):
        return mint
    return mint
def getMintInfo(mint: Pubkey):
    data = solana_client.get_account_info(mint).value.data
    parsed_data = SPL_MINT_LAYOUT.parse(data)
    return parsed_data.decimals
def getTimestamp():
    while True:
        timeStampData = datetime.datetime.now()
        currentTimeStamp = "[" + timeStampData.strftime("%H:%M:%S.%f")[:-3] + "]"
        return currentTimeStamp



class TransactionProcessor:
    def __init__(self):
        self.queue = asyncio.Queue()

    async def process_transactions(self):
        while True:
            await asyncio.sleep(5)

            signature = await self.queue.get()
            try:
                transaction = solana_client.get_transaction(signature, encoding="jsonParsed",
                                                            max_supported_transaction_version=0).value
                if transaction is None:
                    print(f"{getTimestamp()} -Transaction not found: {signature}")

                instruction_list = transaction.transaction.meta.inner_instructions
                account_signer = transaction.transaction.transaction.message.account_keys[0].pubkey
                if account_signer == Pubkey.from_string(wallet_address):
                    print(f"{getTimestamp()} -New update received: , https://solscan.io/tx/{signature}")
                    for ui_inner_instructions in instruction_list:
                        if ui_inner_instructions.instructions[0].program_id == Pubkey.from_string(Pool_raydium):
                            first_info = ui_inner_instructions.instructions[1].parsed["info"]
                            second_info = ui_inner_instructions.instructions[2].parsed["info"]
                            first_token = transactionType(first_info["source"])
                            first_amount = int(first_info['amount']) / 10 ** getMintInfo(first_token)

                            if first_token == Pubkey.from_string(WRAPPED_SOL_MINT):
                                print(f"{style.GREEN}BUY {first_amount} SOL {style.RESET} -FOR  {int(second_info['amount']) / 10 ** getMintInfo(transactionType(second_info['destination']))} TokenBought= {transactionType(second_info['destination'])}  ")

                            if transactionType(second_info["destination"]) == Pubkey.from_string(raydium_V4):
                                print(
                                    f"Buy {int(first_info['amount']) / LAMPORTS} SOL for  {int(second_info['amount']) / 10 ** getMintInfo(transactionType(second_info['destination']))}  TokenBought= {transactionType(second_info['destination'])}")

                            if transactionType(second_info["destination"]) == Pubkey.from_string(WRAPPED_SOL_MINT):
                                print(
                                    f"{style.RED}SELL{style.RESET} {first_amount} -{first_token}--FOR  {style.GREEN}{int(second_info['amount']) / 10 ** getMintInfo(transactionType(second_info['destination']))} {style.RESET}SOL")

                        if ui_inner_instructions.instructions[0].program_id != Pubkey.from_string(Pool_raydium):
                            if ui_inner_instructions.index == 2 and "mint" not in \
                                    ui_inner_instructions.instructions[0].parsed["info"]:
                                info = ui_inner_instructions.instructions[0].parsed["info"]
                                # print(info)
                                sell_token = transactionType(info["destination"])
                                decimal_sell_token = getMintInfo(sell_token)
                                amount_sold = int(info['amount']) / 10 ** decimal_sell_token
                                second_info = ui_inner_instructions.instructions[1].parsed["info"]
                                sol_tokenAccount = second_info['destination']
                                sol_decimal = getMintInfo(transactionType(sol_tokenAccount))
                                sol_amount = int(second_info['amount']) / LAMPORTS
                                print(f"Sell {amount_sold} Token= {sell_token}  For {sol_amount} SOL ")

                            if ui_inner_instructions.index == 3:
                                info = ui_inner_instructions.instructions[0].parsed["info"]
                                second_info = ui_inner_instructions.instructions[1].parsed["info"]
                                tokenBought = transactionType(second_info["source"])
                                decimal_tokenBought = getMintInfo(tokenBought)

                                # print(info)
                                if transactionType(info['source']) == Pubkey.from_string(WRAPPED_SOL_MINT):

                                    print(
                                        f"Buy {int(info['amount']) / LAMPORTS} SOL for  {int(second_info['amount']) / 10 ** decimal_tokenBought}  TokenBought= {tokenBought} ")
                            print("=========================================")

                else:
                   pass
            except Exception as e:
                # print(e)
                print(f"Failed to process transaction {signature}: {e}")
            finally:
                self.queue.task_done()

    async def enqueue_transaction(self, signature):
        await self.queue.put(signature)


async def run():
   processor = TransactionProcessor()
   asyncio.create_task(processor.process_transactions())

   uri = "wss://api.mainnet-beta.solana.com"
   async with websockets.connect(uri) as websocket:
       # Send subscription request
       await websocket.send(json.dumps({
           "jsonrpc": "2.0",
           "id": 1,
           "method": "logsSubscribe",
           "params": [
               {"mentions": [wallet_address]},
               {"commitment": "finalized"} #confirmed , finalized, processed
           ]
       }))

       # Receive the first response
       first_resp = await websocket.recv()
       print(first_resp)
       response_dict = json.loads(first_resp)
       if 'result' in response_dict:
          print("Subscription successful. Subscription ID: ", response_dict['result'])

          # Continuously read from the WebSocket
          async for response in websocket:

              response_dict = json.loads(response)

              if response_dict['params']['result']['value']['err'] == None:

                  signature = response_dict['params']['result']['value']['signature']
                  if signature not in seen_signatures:
                      seen_signatures.add(signature)


                      hash_signature = signature
                      signature = Signature.from_string(hash_signature)
                      await processor.enqueue_transaction(signature)



              else:
                  pass

asyncio.run(run())
