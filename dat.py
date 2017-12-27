import tweepy
from configparser import ConfigParser
import nltk

def sentAnalys(tweet):
    print(tweet)

    #tokenize word
    token = nltk.word_tokenize(tweet)

    #run analysis on tokens
    #nltk.

    print(token)


#get consumer keys and access tokens from configuration file using ConfigParser
config = ConfigParser()
config.read("config.ini")

#get consumer keys and access tokens
consumerKey = config.get("ConsumerKeys", "consumerKey")
consumerSecret = config.get("ConsumerKeys", "consumerSecret")
accessToken = config.get("AccessTokens", "accessToken")
accessTokenSecret = config.get("AccessTokens", "accessTokenSecret")

#close ConfigParser
config.clear()

# OAuth process
auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(accessToken, accessTokenSecret)

#get access to api
api = tweepy.API(auth)

#get twitter username

def user_data(username):
    #get user
    user = api.get_user(username)

    #get user tweets
    tweets = api.user_timeline(username)

    for tweet in tweets:
        sentAnalys(tweet.text)

    return tweets
