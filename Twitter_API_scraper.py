# Imports
import time
import tweepy
import csv

##############################################

# Twitter access keys
APIKey = '6CL0lMe9G3GC7boEimXLKtLDn'
SecretKey = 'URWEMWcZxjLsewbI59arKlknmMEWCM3kVh7cfqctK6id1Ahddv'
BearerToken = 'AAAAAAAAAAAAAAAAAAAAADzpTgEAAAAAUmp%2FGwBkZP0827MlG87dxzvZNOk%3\
    DvTVmzAzWMBSNvetrPQ0MZQVB7XAJzTKvM3B5mFHxdrMtFNA09O'
AccessToken = '707599412541808640-v0jEToY3FbzKnz2hzfyoTpHiIoNaozF'
AccessTokenSecret = 'kAYB8FY5UFtNMz0MUYccPqmZT1F8YH5O1NrYy5wcjIJ9I'

##############################################

# Renaming imports from above
consumer_key = APIKey
consumer_secret = SecretKey
access_token = AccessToken
access_token_secret = AccessTokenSecret

# Providing bearer and access tokens 
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# Querying Twitter API for tweets related to key words in our query
query = '"build back better" OR "BBB" OR "spending bill" OR "reconciliation" \
    -filter:retweets'

n=1
tweet_list = []
cursor = tweepy.Cursor(api.search_tweets, count=100, q=query, lang="en",
    result_type="recent", tweet_mode="extended")
for status in cursor.items(1000): # Look into cursor.next too
    tweet_list.append([n, status.full_text, status.id, status.created_at,
        status.favorite_count, status.user.screen_name, status.user.location])
    n+=1

# Downloading tweets to a csv file
with open('tweets.csv', mode='w', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(["N", "text", "created_at", "likes_count",
        "username", "user_loc"])
    writer.writerows(tweet_list)