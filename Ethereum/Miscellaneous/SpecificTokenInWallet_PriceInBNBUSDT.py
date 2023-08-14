
from web3 import Web3
web3 = Web3(Web3.HTTPProvider("https://eth-mainnet.g.alchemy.com/v2/lTlatSTYDZmCv6wVLRIDff7S3kZhL2dq"))


tokenAbi = [
    {"constant": True, "inputs": [], "name": "decimals", "outputs": [{"name": "", "type": "uint8"}], "payable": False, "stateMutability": "view", "type": "function"},
    {"constant": True, "inputs": [], "name": "name", "outputs": [{"name": "", "type": "string"}], "payable": False, "stateMutability": "view", "type": "function"},
    {"constant": True, "inputs": [], "name": "symbol", "outputs": [{"name": "", "type": "string"}], "payable": False, "stateMutability": "view", "type": "function"},
    {"constant": True,"inputs": [{"name": "owner", "type": "address"}],"name": "balanceOf","outputs": [{"name": "", "type": "uint256"}],"payable": False,"stateMutability": "view","type": "function"}
]


V2SwapAbi = [
    {
        "inputs": [
            {"internalType": "uint256", "name": "amountIn", "type": "uint256"},
            {"internalType": "address[]", "name": "path", "type": "address[]"},
        ],
        "name": "getAmountsOut",
        "outputs": [{"internalType": "uint256[]", "name": "amounts", "type": "uint256[]"}],
        "stateMutability": "view",
        "type": "function",
    },

]

V2SwapContract = "0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D"


tokenAddress= input("Enter Token Address ")
tokenAddress=web3.to_checksum_address(tokenAddress)
#walletAddress= input("Enter Wallet Address")
walletAddress=web3.to_checksum_address(walletAddress)

tokenContract = web3.eth.contract(address=tokenAddress, abi=tokenAbi)

decimals = tokenContract.functions.decimals().call()
tokenName = tokenContract.functions.name().call()
balance = tokenContract.functions.balanceOf(walletAddress).call()
token_balance= balance/10 **decimals
WETH="0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2"
USDT="0xdAC17F958D2ee523a2206206994597C13D831ec7"
def findMatchingDecimal(token_decimals):
    decimalsDict = {
        1: "wei",
        1000: "kwei",
        1000000: "mwei",
        1000000000: "gwei",
        1000000000000: "szabo",
        1000000000000000: "finney",
        1000000000000000000: "ether",
        1000000000000000000000: "kether",
        1000000000000000000000000: "mether",
        1000000000000000000000000000: "gether",
        1000000000000000000000000000000: "tether"
    }

    matching_entry = decimalsDict.get(10 ** token_decimals)
    return matching_entry

def getAmountInBNB(tokenAddress, tokenAmount):
    tokenAmountWei = web3.to_wei(tokenAmount, findMatchingDecimal(decimals))

    try:
        router = web3.eth.contract(abi=V2SwapAbi, address=V2SwapContract)
        amounts = router.functions.getAmountsOut(tokenAmountWei, [tokenAddress, WETH]).call()
        if amounts and len(amounts) > 1:
            amountInBNBWei = amounts[1]
            amountInBNB = web3.from_wei(amountInBNBWei, "ether")
            return round(amountInBNB,2)
        else:
            return None
    except Exception as error:
        print("Error in getAmountInBNB:", error)
        return None


def getAmountInUSDT(tokenAmount):

    EthToSell = web3.to_wei(tokenAmount, "ether")
    #EthToSell = web3.to_wei(str(tokenAmount), "ether")
    #EthToSell = int(tokenAmount * 1e18)  # Convert to wei directly

    amountOut = None

    try:
        router = web3.eth.contract(abi=V2SwapAbi, address=V2SwapContract)
        amountOut = router.functions.getAmountsOut(EthToSell, [WETH, USDT]).call()
        #print("Amounts:", amountOut)  # Add this line
        amountOut = web3.from_wei(amountOut[1], "mwei")

    except Exception as error:
        print("Error:", error)  # Add this line

        pass

    # if not amountOut:
    #     return 0
    return round(amountOut)

weth_amount= getAmountInBNB(tokenAddress,token_balance)
print(weth_amount)
if web3.is_connected() and tokenContract:
    if balance is not None and decimals is not None:
        print(f"Token Balance: {round(token_balance)}")
        print(f"Balance in ETH: {getAmountInBNB(tokenAddress,token_balance)}")
        print(f"Balance in USDT {getAmountInUSDT(weth_amount)}")
        print(f"Token Name: {tokenName}")

    else:
        print("Failed to retrieve token balance or decimals.")
else:
    print("Web3 connection error or invalid token contract.")
