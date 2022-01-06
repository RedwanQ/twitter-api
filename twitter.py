import tweepy
import time

auth = tweepy.OAuthHandler(APIKEY, ACCESS API KEY)
auth.set_access_token(KEY,KEY)

api = tweepy.API(auth, wait_on_rate_limit=True)

user = api.verify_credentials()

search = "Watford"
nrTweets = 100


for tweet in tweepy.Cursor(api.search_tweets, search).items(nrTweets):
    try:
        print('Tweet Liked')
        tweet.favorite()
        time.sleep(10)
    except tweepy.TweepyException as e:
        print(e.reason)
    except StopIteration:
        break
