#!/usr/bin/env python3

import tweepy
from dotenv import load_dotenv
import os
import random

load_dotenv()

def tweet():
    lines = open('tweets.txt').read().splitlines()
    new_tweet = random.choice(lines)
    if find_dup(new_tweet):
        tweet()
    else:
        return new_tweet


def find_dup(tweet):
    with open('tweets.log', 'rt') as f:
        tweets = f.readlines()
        for line in tweets:
            if line.__contains__(tweet):
                return True
            else:
                return False

# Authenticate to Twitter
auth = tweepy.OAuthHandler(os.getenv("APIKEY"), os.getenv("APISECRET"))
auth.set_access_token(os.getenv("TOKEN"), os.getenv("TOKENSECRET"))

# Create API object
api = tweepy.API(auth)

# Create a tweet
new_tweet = tweet()
if find_dup(new_tweet):
    new_tweet = tweet()

api.update_status(new_tweet)

# log to file
file = open('tweets.log', 'a')
file.write(new_tweet + "\n")
