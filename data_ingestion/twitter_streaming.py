import tweepy
from kafka import KafkaProducer
import json

# Twitter API credentials
api_key = 'YOUR_TWITTER_API_KEY'
api_key_secret = 'YOUR_TWITTER_API_KEY_SECRET'
access_token = 'YOUR_TWITTER_ACCESS_TOKEN'
access_token_secret = 'YOUR_TWITTER_ACCESS_TOKEN_SECRET'

# Kafka configuration
producer = KafkaProducer(bootstrap_servers='localhost:9092')

# Twitter API authentication
auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        tweet = status._json
        producer.send('twitter_stream', json.dumps(tweet).encode('utf-8'))

    def on_error(self, status_code):
        if status_code == 420:
            return False

stream_listener = MyStreamListener()
stream = tweepy.Stream(auth=api.auth, listener=stream_listener)
stream.filter(track=['bitcoin', 'crypto', 'ethereum'])
