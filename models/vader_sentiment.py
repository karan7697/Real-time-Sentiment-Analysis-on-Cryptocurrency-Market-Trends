from nltk.sentiment.vader import SentimentIntensityAnalyzer
import json

vader = SentimentIntensityAnalyzer()

def analyze_tweet(tweet):
    text = tweet['text']
    sentiment = vader.polarity_scores(text)
    tweet['sentiment'] = sentiment
    return tweet
