import csv
import tweepy

# Oauth keys
consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""
bearer_token = ""

# Authentication with Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)
client = tweepy.Client(bearer_token)

# 'name' = the account username
name = 'LuckyCryptoC'
# 'tweet_id' = you can find the tweet id within the tweet URL
tweet_id = '1528617951985025024'

replies = []

for tweet in tweepy.Cursor(api.search_tweets, q='to:' + name, result_type='recent').items(10000):
    print(tweet.id)
    if hasattr(tweet, 'in_reply_to_status_id_str'):
        if tweet.in_reply_to_status_id_str == tweet_id:
            replies.append(tweet)

with open('replies.csv', 'w', encoding="utf-8") as f:
    csv_writer = csv.DictWriter(f, fieldnames=('user', 'text'))
    csv_writer.writeheader()
    for tweet in replies:
        row = {'user': tweet.user.screen_name, 'text': tweet.text.replace('\n', ' ')}
        csv_writer.writerow(row)
