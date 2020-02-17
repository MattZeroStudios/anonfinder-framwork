from smedia.twitter import Twitter
import twitter


class KeyManager:

    twitter_keys = {"consumer_key": "", "consumer_secret": "", "access_key": "", "access_secret": ""}


class AnonFinder(Twitter):
    def __init__(self):
        self.twitter = twitter.Api(consumer_key=KeyManager.twitter_keys["consumer_key"],
                                   consumer_secret=KeyManager.twitter_keys["consumer_secret"],
                                   access_token_key=KeyManager.twitter_keys["access_key"],
                                   access_token_secret=KeyManager.twitter_keys["access_secret"])

