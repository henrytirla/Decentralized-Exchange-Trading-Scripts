
#TODO REFACTOR CODE
import requests, json, os, sys
from configparser import ConfigParser

config = ConfigParser()
config.read(os.path.join(sys.path[0], 'data', 'config.ini'))
# birdeye_api = config.get("BIRDEYE", "API")

"""I modified it to dexscreener, forgot to change the filename"""


def getBaseToken(token_address):
    url = f"https://api.dexscreener.com/latest/dex/pairs/solana/{token_address}"
    response = requests.get(url).json()
    return response['pair']['baseToken']['address']


"""
USDT and USDC prices will be excluded
"""


def get_price(token_address):
    url = f"https://api.dexscreener.com/latest/dex/tokens/{token_address}"
    exclude = ['EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v', 'Es9vMFrzaCERmJfrF4H2FYD4KCoNkY11McCe8BenwNYB']
    response = requests.get(url).json()

    if token_address not in exclude:
        for pair in response['pairs']:
            if pair['quoteToken']['address'] == 'So11111111111111111111111111111111111111112':
                return float(pair['priceUsd'])
    else:
        return response['pairs'][0]['priceUsd']
    return None


"""Common addresses like usdc and usdt will be excluded as we know their symbols"""


def getSymbol(token):
    # usdc and usdt
    exclude = ['EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v', 'Es9vMFrzaCERmJfrF4H2FYD4KCoNkY11McCe8BenwNYB']

    if token not in exclude:
        url = f"https://api.dexscreener.com/latest/dex/tokens/{token}"

        Token_Symbol = ""
        Sol_symbol = ""
        try:
            response = requests.get(url)

            # Check if the request was successful (status code 200)
            if response.status_code == 200:
                resp = response.json()
                print("Response:", resp['pairs'][0]['baseToken']['symbol'])
                for pair in resp['pairs']:
                    quoteToken = pair['quoteToken']['symbol']

                    if quoteToken == 'SOL':
                        Token_Symbol = pair['baseToken']['symbol']
                        Sol_symbol = quoteToken
                        return Token_Symbol, Sol_symbol


            else:
                print(f"[getSymbol] Request failed with status code {response.status_code}")

        except requests.exceptions.RequestException as e:
            print(f"[getSymbol] error occurred: {e}")
        except:
            a = 1

        return Token_Symbol, Sol_symbol
    else:
        if token == 'EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v':
            return "USDC", "SOL"
        elif token == 'EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v':
            return "USDT", "SOL"
