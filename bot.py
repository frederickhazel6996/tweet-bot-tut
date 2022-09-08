import tweepy
from dotenv import dotenv_values

config = dotenv_values(".env")


client = tweepy.Client(
    bearer_token=config["bearer_token"],
    consumer_key=config["api_key"],
    consumer_secret=config["api_key_secret"],
    access_token=config["access_token"],
    access_token_secret=config["access_token_secret"],
)

response = client.create_tweet(text="Bot Test 1")
print(response)
