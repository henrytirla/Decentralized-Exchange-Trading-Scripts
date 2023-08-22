"""Get number of times a wallet bought a token """



from alchemy import Alchemy, Network

ALCHEMY_API_KEY = "Enter your API KEY"
network = Network.ETH_MAINNET

contract_ADDRESS = ["Enter Contract Address"]

wallet_Address="Enter your wallet Address"
alchemy = Alchemy(ALCHEMY_API_KEY, network)


def main():
    alchemy = Alchemy(ALCHEMY_API_KEY, network)

    transfers = alchemy.core.get_asset_transfers(category=["erc20"],contract_addresses=contract_ADDRESS,to_address=wallet_Address)
    print(transfers)




if __name__ == "__main__":
    main()
