#Get raydium pool info of any token much faster than downloading a whole 70MB json file.



import base58
from solana.rpc.api import Client
from solana.rpc.types import MemcmpOpts
from solders.pubkey import Pubkey
solana_client = Client("https://solana-mainnet.g.alchemy.com/v2/zWDdevLas9BnD8ZvpXyEXE-7QdkX_Kn6")
address = Pubkey.from_string("5b5aQ8J9iv9Mzvy2Xr79jpQcEtb9v2hpQch4QwUicv5W")
RAYDIUM = Pubkey.from_string("675kPX9MHTjS2zt1qfr1NYHuzeLXfQM9H24wFSUt1Mp8")
OPENBOOK = Pubkey.from_string("srmqPvymJeFKQ4zGQed1GFppgkRHL9kaELCbyksJtPX")
from borsh_construct import CStruct, U64, Bytes, U128
from construct import Bytes, Int8ul, Int32ul, Int64ul, Pass, Switch
from base58  import b58decode, b58encode
PUBLIC_KEY_LAYOUT = Bytes(32)

liquidity_state_layout_v4 = CStruct(
    "status" / U64,
    "nonce" / U64,
    "maxOrder" / U64,
    "depth" / U64,
    "baseDecimal" / U64,
    "quoteDecimal" / U64,
    "state" / U64,
    "resetFlag" / U64,
    "minSize" / U64,
    "volMaxCutRatio" / U64,
    "amountWaveRatio" / U64,
    "baseLotSize" / U64,
    "quoteLotSize" / U64,
    "minPriceMultiplier" / U64,
    "maxPriceMultiplier" / U64,
    "systemDecimalValue" / U64,
    "minSeparateNumerator" / U64,
    "minSeparateDenominator" / U64,
    "tradeFeeNumerator" / U64,
    "tradeFeeDenominator" / U64,
    "pnlNumerator" / U64,
    "pnlDenominator" / U64,
    "swapFeeNumerator" / U64,
    "swapFeeDenominator" / U64,
    "baseNeedTakePnl" / U64,
    "quoteNeedTakePnl" / U64,
    "quoteTotalPnl" / U64,
    "baseTotalPnl" / U64,
    "poolOpenTime" / U64,
    "punishPcAmount" / U64,
    "punishCoinAmount" / U64,
    "orderbookToInitTime" / U64,
    "swapBaseInAmount" / U128,
    "swapQuoteOutAmount" / U128,
    "swapBase2QuoteFee" / U64,
    "swapQuoteInAmount" / U128,
    "swapBaseOutAmount" / U128,
    "swapQuote2BaseFee" / U64,
    "baseVault" / PUBLIC_KEY_LAYOUT,
    "quoteVault" / PUBLIC_KEY_LAYOUT,
    "baseMint" / PUBLIC_KEY_LAYOUT,
    "quoteMint" / PUBLIC_KEY_LAYOUT,
    "lpMint" / PUBLIC_KEY_LAYOUT,
    "openOrders" / PUBLIC_KEY_LAYOUT,
    "marketId" / PUBLIC_KEY_LAYOUT,
    "marketProgramId" / PUBLIC_KEY_LAYOUT,
    "targetOrders" / PUBLIC_KEY_LAYOUT,
    "withdrawQueue" / PUBLIC_KEY_LAYOUT,
    "lpVault" / PUBLIC_KEY_LAYOUT,
    "owner" / PUBLIC_KEY_LAYOUT,
    "lpReserve" / U64,
    # Const(b'\x00\x00\x00') # padding
)


bytes= base58.b58decode("SEDNswjQdnSyxhNBET1LvUCJ5wGKRwNBm5vNb88nKCw")
print(bytes)

def getRaydiumMarkets(tokenMint: Pubkey):
    memcmp_filter = MemcmpOpts(offset=(30 * 8) + 64 + 32 + 64 , bytes=tokenMint)
    markets = solana_client.get_program_accounts(
        RAYDIUM,
        commitment="confirmed",
        filters=[memcmp_filter]
    )
    # return markets
    data= markets.value[0].account.data
    parsed_data=liquidity_state_layout_v4.parse(data)
    parsed_data.baseVault = Pubkey.from_bytes(parsed_data.baseVault)
    parsed_data.quoteVault = Pubkey.from_bytes(parsed_data.quoteVault)
    parsed_data.baseMint = Pubkey.from_bytes(parsed_data.baseMint)
    parsed_data.quoteMint = Pubkey.from_bytes(parsed_data.quoteMint)
    parsed_data.lpMint = Pubkey.from_bytes(parsed_data.lpMint)
    parsed_data.openOrders = Pubkey.from_bytes(parsed_data.openOrders)
    parsed_data.marketId = Pubkey.from_bytes(parsed_data.marketId)
    parsed_data.marketProgramId = Pubkey.from_bytes(parsed_data.marketProgramId)
    parsed_data.targetOrders = Pubkey.from_bytes(parsed_data.targetOrders)
    parsed_data.withdrawQueue = Pubkey.from_bytes(parsed_data.withdrawQueue)
    parsed_data.lpVault = Pubkey.from_bytes(parsed_data.lpVault)
    parsed_data.owner = Pubkey.from_bytes(parsed_data.owner)


    return parsed_data

print(getRaydiumMarkets(bytes))
print("=====================")

