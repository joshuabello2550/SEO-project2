import tweepy
import os
import pandas as pd
from collections import Counter

def authenticate_twitter_api(consumer_key, consumer_secret, access_token, access_token_secret):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    return api

def get_user_timeline(api, screen_name):
    tweets = api.user_timeline(screen_name=screen_name, count=200, tweet_mod='extended')
    data=[]
    for tweet in tweets:
        hashtags = [h['text']] for h in tweeet.entities['hashtags']
        data.append({
            'id': tweet.id_str
            'created_at': tweet.created_at,
            'text': tweet.full_text,
            'hashtags': hashtags,
        })
    return pd.DataFrame(data)

def get_trending_hashtags(df):
    all_hashtags = [h for row in df['hashtags'] for h in row]
    counter = Counter(all_hashtags)
    return counter.most_common(10)

def main():

    consumer_key = os.getenv('TWITTER_CONSUMER_KEY')
    consumer_secret = os.getenv('TWITTER_CONSUMER_SECRET')
    access_token = os.getenv('TWITTER_ACCESS_TOKEN')
    access_token_secret = os.getenv('TWITTER_ACCESS_TOKEN')
    api = authenticate_twitter_api(consumer_key, consumer_secret, access_token, access_token_secret)
    user_tweets =  get_trending_hashtags(api, 'jack')

    trends = get_trending_hashtags(user_tweets)
    print("Top Trending hashtags")
    for hashtag, count in trends:
        print(f"{hashtag}: {count}")


