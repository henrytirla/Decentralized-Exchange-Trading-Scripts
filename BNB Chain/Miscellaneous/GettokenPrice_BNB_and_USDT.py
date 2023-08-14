from web3 import Web3

pancakeSwapAbi = [
    {
        "inputs": [
            {"internalType": "uint256", "name": "amountIn", "type": "uint256"},
            {"internalType": "address[]", "name": "path", "type": "address[]"},
        ],
        "name": "getAmountsOut",
        "outputs": [{"internalType": "uint256[]", "name": "amounts", "type": "uint256[]"}],
        "stateMutability": "view",
        "type": "function",
    }
]




pancakeSwapContract = "0x10ED43C718714eb63d5aA57B78B54704E256024E"
web3 = Web3(Web3.HTTPProvider("https://bsc-dataseed1.binance.org"))


def getAmountInBNB(tokenAddress, tokenAmount):
    BNBTokenAddress = "0xbb4CdB9CBd36B01bD1cBaEBF2De08d9173bc095c"
    tokenAmountWei = web3.to_wei(tokenAmount, "ether")

    try:
        router = web3.eth.contract(abi=pancakeSwapAbi, address=pancakeSwapContract)
        amounts = router.functions.getAmountsOut(tokenAmountWei, [tokenAddress, BNBTokenAddress]).call()
        if amounts and len(amounts) > 1:
            amountInBNBWei = amounts[1]
            amountInBNB = web3.from_wei(amountInBNBWei, "ether")
            return round(amountInBNB,2)
        else:
            return None
    except Exception as error:
        print("Error in getAmountInBNB:", error)
        return None

#def getAmountInUSDT(tokenAddress,tokenAmount,decimal):
def getAmountInUSDT(tokenAmount):
    BNBTokenAddress = "0xbb4CdB9CBd36B01bD1cBaEBF2De08d9173bc095c"
    USDTokenAddress = "0x55d398326f99059fF775485246999027B3197955"
    bnbToSell = web3.to_wei(tokenAmount, "ether")
    amountOut = None

    try:
        router = web3.eth.contract(abi=pancakeSwapAbi, address=pancakeSwapContract)
        amountOut = router.functions.getAmountsOut(bnbToSell, [BNBTokenAddress, USDTokenAddress]).call()
        #print("Amounts:", amountOut)  # Add this line

        amountOut = web3.from_wei(amountOut[1], "ether")
    except Exception as error:
        print("Error:", error)  # Add this line

        pass

    if not amountOut:
        return 0
    return round(amountOut)





def main():
    tokenAddress =web3.to_checksum_address("0xce186ad6430e2fe494a22c9edbd4c68794a28b35")
    tokenAmount = 102000

    amountInBNB = getAmountInBNB(tokenAddress, tokenAmount)
    amountInUSDT= getAmountInUSDT(amountInBNB)

    if amountInBNB is not None:
        print(f'Token Amount: {tokenAmount}')
        print(f'Token Amount in BNB: {amountInBNB}')
        print(f'Token Amount in USDT: ${amountInUSDT}')
    else:
        print("Failed to calculate the token amount in BNB.")


if __name__ == "__main__":
    main()
