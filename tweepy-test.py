import os
import tweepy
from dotenv import load_dotenv
load_dotenv()

openseaApiKey = os.environ.get("OPENSEA_API_KEY")
consumer_key = os.environ.get("TWITTER_API_KEY") 
consumer_secret = os.environ.get("TWITTER_API_KEY_SECRET") 
access_token = os.environ.get("ACCESS_TOKEN") 
token_secret = os.environ.get("ACCESS_TOKEN_SECRET") 

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, token_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)