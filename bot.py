import os
import tweepy
from secrets import *
from time import gmtime, strftime
from random import choice
from grose import master_list


# ====== Individual bot configuration ==========================
bot_username = 'grosebot'
logfile_name = bot_username + ".log"

# ==============================================================


def create_tweet():
    """Create the text of the tweet you want to send."""
    text = choice(master_list)
    return text


def tweet(text):
    """Send out the text as a tweet."""
    # Twitter authentication
    auth = tweepy.OAuthHandler(C_KEY, C_SECRET)
    auth.set_access_token(A_TOKEN, A_TOKEN_SECRET)
    api = tweepy.API(auth)

    # Break the tweet up as necessary into 140-character chunks
    tweetset = []
    while len(text) > 140:
        tweetset.append(text[:140])
        text = text[140:]
    tweetset.append(text)

    # Send the tweet and log success or failure
    last_tweet = None
    for status in tweetset:
        try:
            if last_tweet:
                last_tweet = api.update_status(status, last_tweet.id)
            else:
                last_tweet = api.update_status(status)
        except tweepy.error.TweepError as e:
            log(e.message)
        else:
            log("Tweeted: " + status)


def log(message):
    """Log message to logfile."""
    path = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    with open(os.path.join(path, logfile_name), 'a+') as f:
        t = strftime("%d %b %Y %H:%M:%S", gmtime())
        f.write("\n" + t + " " + message)


if __name__ == "__main__":
    tweet_text = create_tweet()
    tweet(tweet_text)
