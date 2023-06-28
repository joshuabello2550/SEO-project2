import tweepy
from collections import Counter
import sqlite3

auth =  tweepy.oAuthHandler('TWITTER_CONSUMER_KEY', 'TWITTER_CONSUMER_SECRET')
auth.set_access_token("ACCESS_TOKEN", "ACCESS_TOKEN_SECRET")

api =  tweepy.API(auth, wait _on_rate_limit=True)
conn = sqlite3.connect('trends.db')
c = conn.cursor()

c.execute('CREATE TABLE IF NOT EXISTS Hashtags (hashtag TEXT, count INTEGER)')
c.execute('CREATE TABLE IF NOT EXISTS Topics (topic TEXT, count INTEGER)')
# conn = sqlite3.connect('')

following = api.friends_ids("username")
hashtags = []
topics = []

for user in following:
    try:
        for status in tweepy.Cursor(api.user_timeline, id = user ).items():
            if hasattr(status, "entities"):
                entities = status.entities

                if "hashtags" in entities:
                    for ent in entities["hashtags"]:
                        if ent is not None:
                            if "text" in ent:
                                hashtag = ent["text"]
                                