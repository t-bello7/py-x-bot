import os
import json
from requests_oauthlib import OAuth1Session
from dotenv import load_dotenv
import tweepy

load_dotenv()

CONSUMER_API_KEY=os.getenv('CONSUMER_API_KEY')
CONSUMER_API_SECRET=os.getenv('CONSUMER_API_SECRET')

APP_ACCESS_KEY=os.getenv('ACCESS_TOKEN')
APP_ACCESS_SECRET=os.getenv('ACCESS_TOKEN_SECRET')

client = tweepy.Client(
    consumer_key=CONSUMER_API_KEY,
    consumer_secret=CONSUMER_API_SECRET,
    access_token=APP_ACCESS_KEY,
    access_token_secret=APP_ACCESS_SECRET
)

client.create_tweet(text="Created this tweet from my py-x-bot")