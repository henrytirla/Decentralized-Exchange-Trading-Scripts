import web3
import time
import requests
import datetime

from alchemy import Alchemy, Network
from decimal import Decimal

network = Network.ETH_MAINNET

api_key = "BLHi-AZvCt6LjvO8W7nFtloBJFZa393M"

alchemy_ws_url="wss://eth-mainnet.g.alchemy.com/v2/WoUWFd2SYi7sNbmTTaT_fWMPCOUZ8yDI"
alchemy= Alchemy(api_key,network)

url = "https://eth-mainnet.g.alchemy.com/v2/lTlatSTYDZmCv6wVLRIDff7S3kZhL2dq"
headers = {
        "accept": "application/json",
        "content-type": "application/json"
    }

printed_values = []
topic_filter = [
    "0x4c209b5fc8ad50758f13e2e1088ba56a560dff690a1c6fef26394f4c03821c4f",
    "0x0000000000000000000000007a250d5630b4cf539739df2c5dacb4c659f2488d"
]




def getTimestamp():
    while True:
        timeStampData = datetime.datetime.now()
        currentTimeStamp = "[" + timeStampData.strftime("%H:%M:%S.%f")[:-3] + "]"
        return currentTimeStamp
try:
    while True:
            payload = {
                "id": 1,
                "jsonrpc": "2.0",
                "method": "eth_getLogs",
                "params": [

                    {
                        "topics":[topic_filter]

                    }

                ]
            }


            response = requests.post(url, json=payload, headers=headers)
            response_data = response.json()
     

            if 'result' in response_data:

                for res in response_data['result']:

                    if res not in printed_values:
                        try:

                            transaction_hash= res['transactionHash']
                            txn_receipt = alchemy.core.get_transaction_receipt(transaction_hash)
                            c = alchemy.core.get_transaction(transaction_hash)
                            ether_value=alchemy.from_wei(c['value'], 'ether')


                            token_address= txn_receipt['logs'][0]['address']
                          
                            input_signature = alchemy.to_hex(c['input'][:10])
                         

                            if input_signature.startswith("0xf305d719"):
                                print(getTimestamp(),"ADD LP")
                                print("Token Address: ", token_address)
                                print("Block Number:", res['blockNumber'])
                                print("Transaction Hash:", res['transactionHash'])
                                print("Log Index:", res['logIndex'])
                                print("Topics:", res['topics'])
                                print("Data:", ether_value)
                                print("=======================")
                            elif input_signature.startswith("0xc9567bf9"):
                                 hex_data = res['data']
                                 second_number = hex_data[66:]
                                 decimal_value = int(second_number, 16)
                                 wei_value = alchemy.to_wei(decimal_value, 'wei')
                                 eth_value = alchemy.from_wei(wei_value, 'ether')
                                 print(getTimestamp(),"OPEN TRADING")
                                 print("Token Address: ", token_address)
                                 print("Block Number:", res['blockNumber'])
                                 print("Transaction Hash:", res['transactionHash'])
                                 print("Log Index:", res['logIndex'])
                                 print("Topics:", res['topics'])
                                 print("Data:", eth_value)
                             


                                 print("=======================")
                              
                            elif input_signature.startswith("0x6e3fa5d1"):
                                 print(getTimestamp(),"CREATE ERC20")
                                 print("Token Address: ", token_address)
                                 print("Block Number:", res['blockNumber'])
                                 print("Transaction Hash:", res['transactionHash'])
                                 print("Log Index:", res['logIndex'])
                                 print("Topics:", res['topics'])
                                 print("Data:", ether_value)

                                 print("=======================")
                            elif input_signature.startswith("0x4bb278f3"):
                                hex_data = txn_receipt['logs'][12]['data']
                                second_number = hex_data[66:]
                                decimal_value = int(second_number, 16)
                                wei_value = alchemy.to_wei(decimal_value, 'wei')
                                eth_value = alchemy.from_wei(wei_value, 'ether')
                                print(getTimestamp(), "Finalize")
                                print("Token Address: ", txn_receipt['logs'][2]['address'])
                                print("Block Number:", txn_receipt['blockNumber'])
                                print("Transaction Hash:", txn_receipt['transactionHash'])

                                print("Data:", ether_value)

                                print("=======================")
                            else:
                                
                                pass
                        

                        except Exception as e:
                            print(f"Error {e} {alchemy.to_hex(c['input'][:10])} {transaction_hash}")
                            pass

                    printed_values.append(res) 
            else:
                print(f"No result in response_data {response_data}")
except Exception as e:
    print(f"Error {e} {alchemy.to_hex(c['input'][:10])} {transaction_hash}")
    print(response_data)

    time.sleep(1)
