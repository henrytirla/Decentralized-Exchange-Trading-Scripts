#Using twillo api get notified of  a transaction via SMS

import json
import asyncio
import websockets

from twilio.rest import Client

# Set your Twilio credentials
account_sid = ''# Replace with your Twilio account SID
auth_token = ''# Replace with your Twilio auth token
client = Client(account_sid, auth_token)

ALCHEMY_KEY = 'BLHi-AZvCt6LjvO8W7nFtloBJFZa393M'
alchemy_ws_url = "wss://eth-mainnet.g.alchemy.com/v2/BLHi-AZvCt6LjvO8W7nFtloBJFZa393M"

async def main():
    for i in range(3):
        try:
            async with websockets.connect(alchemy_ws_url) as ws:
                print("Connection made")
                subscription_payload = {
                    "jsonrpc": "2.0",
                    "method": "eth_subscribe",
                    "params": ["alchemy_filteredNewFullPendingTransactions", {"toAddress": "0x50B8f49f4B2E80e09cE8015C4e7A9c277738Fd3d"}],
                    "id": 1
                }
                await ws.send(json.dumps(subscription_payload))
                print("JSON eth_subscribe sent")

                while True:
                    try:
                        result = await ws.recv()
                        result = json.loads(result)

                        if "params" in result and "result" in result["params"]:
                            from_address = result["params"]["result"]["from"]
                            to_address = result["params"]["result"]["to"]
                            hash = result["params"]["result"]["hash"]
                            blockHash = result["params"]["result"]["blockNumber"]

                            print("from:", from_address)
                            print("to:", to_address)
                            print("hash: ", hash)
                            print("blockHash: ", blockHash)

                            print("Send Twilio SMS for pending transaction!")
                            message = client.messages.create(
                                body="\n \n PENDING TX! \n\n From: " + from_address + " \n\n To: " + to_address + "\n\n  @tx:" + hash,
                                from_='+0000000', # Replace with your Twilio number
                                to='+000000000'# Replace with your phone number
                            )

                            print(message.sid)

                        else:
                            print("Received unexpected JSON response:", result)

                    except Exception as error:
                        print('JSON Error: ' + repr(error))
                        await asyncio.sleep(1)

        except Exception as error:
            print('Connection Error: ' + repr(error))
            await asyncio.sleep(3)

if __name__ == "__main__":
    asyncio.run(main())
