"V1 Script to get newly created pairs on Raydium    "

import httpx
import time
import threading

response = httpx.get("https://api.raydium.io/v2/sdk/token/raydium.mainnet.json")
previous_tokens = set()

new_tokens = set()
printtokens = set()
if response.status_code == 200:
  # print(response.json())
   response = httpx.get("https://api.raydium.io/v2/sdk/token/raydium.mainnet.json")
   #print(response.json()["unNamed"])
   current_tokens = set([j["mint"] for j in response.json()["unNamed"]])
   new_tokens = current_tokens - previous_tokens
   previous_tokens = current_tokens
   print(new_tokens)