#Deserialize SPL Account DATA


from borsh_construct import CStruct, U64, Bytes
from solana.rpc.api import Client
from solders.pubkey import Pubkey
from construct import Bytes, Int8ul, Int32ul, Int64ul, Pass, Switch,IfThenElse
PUBLIC_KEY_LAYOUT = Bytes(32)
solana_client=Client("https://api.mainnet-beta.solana.com")
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

def transactionType(Account: str):
    data = solana_client.get_account_info(Pubkey.from_string(Account)).value.data
    parsed_data = SPL_ACCOUNT_LAYOUT.parse(data)
    parsed_data.mint=Pubkey.from_bytes(parsed_data.mint)
    parsed_data.owner=Pubkey.from_bytes(parsed_data.owner)
    parsed_data.delegate=Pubkey.from_bytes(parsed_data.delegate)
    parsed_data.closeAuthority=Pubkey.from_bytes(parsed_data.closeAuthority)


    return parsed_data


print(transactionType("UwwaA87kG33YTTQNA3QyVQZFmNiFDioZLZrqNvcGbFr"))
