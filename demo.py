import tweepy
from textblob import TextBlob

# Authenticate
consumer_key= 'hMh1poC9sYnLu4gl1RbRpObJI'
consumer_secret= 'pWK3lyJ0CMjCbhZYmZuyBIrWi4mhFuONSgkEfN8F67JHaqhRH1'

access_token='1942719522-YOOsbiVyUFLPN84KmZtNaOvO7Mb2AUs4eb97Wau'
access_token_secret='ZuviSp1AUTMvFLXLhRWMUfnhDA8XZCgVEAX1bjiZbT5P2'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# Retrieve Tweets
public_tweets = api.search('Bitcoin')



# Print first 10 tweets in the Query results


for tweet in public_tweets:
    print(tweet.text)
    
    # Perform Sentiment Analysis on Tweets
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    print("")
