import requests
import json
import time
from requests_oauthlib import OAuth1Session
import os
from dotenv import load_dotenv
load_dotenv()

openseaApiKey = os.environ.get("OPENSEA_API_KEY")
consumer_key = os.environ.get("TWITTER_API_KEY") 
consumer_secret = os.environ.get("TWITTER_API_KEY_SECRET") 
access_token = os.environ.get("ACCESS_TOKEN") 
token_secret = os.environ.get("ACCESS_TOKEN_SECRET") 

# check file for the last time that was queried
# request data from opensea (last time queried - now)
# dedup, parse, and clean data
# write the new response to file
# repeat

while True:

    lastEventTime = 0

    with open("lasttime.txt",'r') as f:
        lastEventTime = f.readline()
        print("last published sale event was at: ", lastEventTime)
        

    url = "https://api.opensea.io/api/v1/events?asset_contract_address=0x5180db8F5c931aaE63c74266b211F580155ecac8&event_type=successful&only_opensea=false&offset=0&limit=1"

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
        createdTime = txn["timestamp"]

        if createdTime != lastEventTime:
            print("createdTime (datetime)", createdTime)

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

            with open("lasttime.txt", "w") as f:
                f.write(createdTime)

    time.sleep(30)

# tweet the trades

# # Twitter Bot POST request
# # Be sure to add replace the text of the with the text you wish to Tweet. You can also add parameters to post polls, quote Tweets, Tweet with reply settings, and Tweet to Super Followers in addition to other features.
# payload = {"text": "Hello world!"}

# # Get request token
# request_token_url = "https://api.twitter.com/oauth/request_token"
# oauth = OAuth1Session(consumer_key, client_secret=consumer_secret)

# try:
#     fetch_response = oauth.fetch_request_token(request_token_url)
# except ValueError:
#     print(
#         "There may have been an issue with the consumer_key or consumer_secret you entered."
#     )

# resource_owner_key = fetch_response.get("oauth_token")
# resource_owner_secret = fetch_response.get("oauth_token_secret")
# print("Got OAuth token: %s" % resource_owner_key)

# # Get authorization
# base_authorization_url = "https://api.twitter.com/oauth/authorize"
# authorization_url = oauth.authorization_url(base_authorization_url)
# print("Please go here and authorize: %s" % authorization_url)
# verifier = input("Paste the PIN here: ")

# # Get the access token
# access_token_url = "https://api.twitter.com/oauth/access_token"
# oauth = OAuth1Session(
#     consumer_key,
#     client_secret=consumer_secret,
#     resource_owner_key=resource_owner_key,
#     resource_owner_secret=resource_owner_secret,
#     verifier=verifier,
# )
# oauth_tokens = oauth.fetch_access_token(access_token_url)

# access_token = oauth_tokens["oauth_token"]
# access_token_secret = oauth_tokens["oauth_token_secret"]

# # Make the request
# oauth = OAuth1Session(
#     consumer_key,
#     client_secret=consumer_secret,
#     resource_owner_key=access_token,
#     resource_owner_secret=access_token_secret,
# )

# # Making the request
# response = oauth.post(
#     "https://api.twitter.com/2/tweets",
#     json=payload,
# )

# if response.status_code != 201:
#     raise Exception(
#         "Request returned an error: {} {}".format(response.status_code, response.text)
#     )

# print("Response code: {}".format(response.status_code))

# # Saving the response as JSON
# json_response = response.json()
# print(json.dumps(json_response, indent=4, sort_keys=True))