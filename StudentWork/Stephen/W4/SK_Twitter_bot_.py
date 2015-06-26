__author__ = 'stephen'

import tweepy


consumer_key = "U8cqX60tkVaElYwi2tSF6juU3"
consumer_secret = "5PvyrWArTnLRnEwvnrMXLAZW8MWlsnrXEOWy1lJEqNi7IGBM7A"
access_token  = "3253921376-59a5Q52Qm6FMDorvvHDSttQtp6vRYennGGhIPga"
access_token_secret =  "NSprt2x9paoXQWpccbTU6bbyLJ7nnY7vBIlsfTItDSVO6"


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print tweet.text

user = api.get_user('classexamplebot')

status = api.update_status(status = "This is Stephen, again!!")