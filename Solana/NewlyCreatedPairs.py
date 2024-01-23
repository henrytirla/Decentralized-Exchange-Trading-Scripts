"Detect  New Pools Created on Solana Raydium DEX"

#TODO Add Buys ,Sells price and liquidity pool tracking management
from pprint import pprint

import asyncio
from typing import Iterator, List, AsyncIterator, Tuple
from asyncstdlib import enumerate

from solana.rpc.websocket_api import connect
from solana.rpc.commitment import Finalized
from solana.rpc.api import Client

from solders.pubkey import Pubkey

# Type hinting imports
from solana.rpc.commitment import Commitment
from solana.rpc.websocket_api import SolanaWsClientProtocol
from solders.rpc.responses import RpcLogsResponse, SubscriptionResult, LogsNotification, GetTransactionResp
from solders.signature import Signature
from solders.transaction_status import UiPartiallyDecodedInstruction, ParsedInstruction

# Raydium Liquidity Pool V4
RaydiumLPV4 = "675kPX9MHTjS2zt1qfr1NYHuzeLXfQM9H24wFSUt1Mp8"
URI = "https://api.mainnet-beta.solana.com"  # "https://api.devnet.solana.com" | "https://api.mainnet-beta.solana.com"
WSS = "wss://api.mainnet-beta.solana.com"  # "wss://api.devnet.solana.com" | "wss://api.mainnet-beta.solana.com"
solana_client = Client(URI)
# Raydium function call name, look at raydium-amm/program/src/instruction.rs
log_instruction = "initialize2"


async def main():
    """The client as an infinite asynchronous iterator:"""
    async with connect(WSS) as websocket:
        subscription_id = await subscribe_to_logs(
            websocket,
            RpcTransactionLogsFilterMentions(RaydiumLPV4),
            Finalized
        )  # type: ignore
        async for signature in process_messages(websocket, log_instruction):  # type: ignore
            get_tokens(signature, RaydiumLPV4)
            break
        await websocket.logs_unsubscribe(subscription_id)


async def subscribe_to_logs(websocket: SolanaWsClientProtocol, 
                            mentions: RpcTransactionLogsFilterMentions,
                            commitment: Commitment) -> int:
    await websocket.logs_subscribe(
        filter_=mentions,
        commitment=commitment
    )
    first_resp = await websocket.recv()
    return get_subscription_id(first_resp)  # type: ignore


def get_subscription_id(response: SubscriptionResult) -> int:
    return response[0].result


async def process_messages(websocket: SolanaWsClientProtocol,
                           instruction: str) -> AsyncIterator[Signature]:
    """Async generator, main websocket's loop"""
    async for idx, msg in enumerate(websocket):
        value = get_msg_value(msg)
        print(idx)
        if [log for log in value.logs if instruction in log]:
            print(f"{value.signature=}")
            pprint(value.logs)
            yield value.signature


def get_msg_value(msg: List[LogsNotification]) -> RpcLogsResponse:
    return msg[0].result.value


def get_tokens(signature: Signature, RaydiumLPV4: Pubkey) -> None:
    """httpx.HTTPStatusError: Client error '429 Too Many Requests' 
    for url 'https://api.mainnet-beta.solana.com'
    For more information check: https://httpstatuses.com/429
    """
    transaction = solana_client.get_transaction(
        signature,
        encoding="jsonParsed",
        max_supported_transaction_version=0
    )
    # https://kevinheavey.github.io/solders/api_reference/instruction.html
    instructions = get_instructions(transaction)
    for instruction in instructions_with_program_id(instructions, RaydiumLPV4):
        tokens = get_tokens_info(instruction)
        print_table(tokens)


def get_instructions(
    transaction: GetTransactionResp
) -> List[UiPartiallyDecodedInstruction | ParsedInstruction]:
    instructions = transaction \
                   .value \
                   .transaction \
                   .transaction \
                   .message \
                   .instructions
    return instructions


def instructions_with_program_id(
    instructions: List[UiPartiallyDecodedInstruction | ParsedInstruction],
    program_id: str
) -> Iterator[UiPartiallyDecodedInstruction | ParsedInstruction]:
    return (instruction for instruction in instructions
            if instruction.program_id == program_id)


def get_tokens_info(
    instruction: UiPartiallyDecodedInstruction | ParsedInstruction
) -> Tuple[Pubkey, Pubkey]:
    accounts = instruction.accounts
    Token0 = accounts[8]
    Token1 = accounts[9]
    return (Token0, Token1)


def print_table(tokens: Tuple[Pubkey, Pubkey]) -> None:
    data = [
        {'Token_Index': 'Token0', 'Account Public Key': tokens[0]},  # Token0
        {'Token_Index': 'Token1', 'Account Public Key': tokens[1]}   # Token1
    ]
    print("============NEW POOL DETECTED====================")
    header = ["Token_Index", "Account Public Key"]
    print("│".join(f" {col.ljust(15)} " for col in header))
    print("|".rjust(18))
    for row in data:
        print("│".join(f" {str(row[col]).ljust(15)} " for col in header))


if __name__ == "__main__":
    RaydiumLPV4 = Pubkey.from_string(RaydiumLPV4)
    asyncio.run(main())
