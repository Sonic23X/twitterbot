import tweepy, time
from access import *
from random import randint

# Setup API:
def twitter_setup():
    # Authenticate and access using keys:
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

    # Return API access:
    api = tweepy.API(auth)
    return api

if __name__ == '__main__':
    # Setup Twitter API:
    bot = twitter_setup()

    # Set waiting time:
    secs = 3

    # Set tweet list:
    tweetlist = ["Test tweet using #Python \n@_MedioLimon",
                "Look, I'm using #Python \n#Muajaja",
                " \n#PythonDayMX17"]

    # Tweet posting:
    for tweet in tweetlist:
        # Print tweet:
        print(tweet)

        # Try to post tweet:
        try:
            bot.update_status(tweet)
            print("Successfully posted.")
        except tweepy.TweepError as e:
            print(e.reason)

        # Wait till next sentence extraction:
        time.sleep(secs)
