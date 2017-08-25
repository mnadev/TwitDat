import tweepy
from configparser import ConfigParser

#get consumer keys and access tokens from configuration file using ConfigParser
config = ConfigParser()
config.read("config.ini")

#get consumer keys and access tokens
consumer_key = config.get("ConsumerKeys", "consumer_key")
consumer_secret = config.get("ConsumerKeys", "consumer_secret")
access_token = config.get("AccessTokens", "access_token")
access_token_secret = config.get("AccessTokens", "access_token_secret")

#close ConfigParser
config.clear()

# OAuth process
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

#get access to api
api = tweepy.API(auth)

#get twitter username
usrname = input("What is the username that you wish to get info for?: ")

#get user
user = api.get_user(usrname)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)