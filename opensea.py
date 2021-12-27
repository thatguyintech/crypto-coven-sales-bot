import requests
import json

from dotenv import load_dotenv
load_dotenv()
import os
openseaApiKey = os.environ.get("OPENSEA_API_KEY")

url = "https://api.opensea.io/api/v1/events?asset_contract_address=0x5180db8F5c931aaE63c74266b211F580155ecac8&event_type=successful&only_opensea=false&offset=0&limit=2"

headers = {
    "Accept": "application/json",
    "X-API-KEY": openseaApiKey
}

response = requests.request("GET", url, headers=headers)

print("\n=== printing events..\n")
resp = json.loads(response.text)
for event in resp["asset_events"]:
    asset = event["asset"]
    txn = event["transaction"]


    print("Witch {}: {}, has taken flight at {}..".format(asset["token_id"], asset["name"], txn["timestamp"]))
    original_image_url = asset["image_original_url"]
    opensea_image_url = asset["image_url"]
    if original_image_url:
        print("image:", original_image_url)
    else:
        print("image:", opensea_image_url)



    # sale info
    token = event["payment_token"]["symbol"]
    decimals = event["payment_token"]["decimals"]
    price = round(float(event["total_price"]) * 10 ** (-1 * decimals), 4)
    print("transportation price", price, token)
    # print("total price", event["payment_token"]["symbol"])
    print("opensea", asset["permalink"])
    print("etherscan", txn["transaction_hash"])
    print("\n --- \n")
