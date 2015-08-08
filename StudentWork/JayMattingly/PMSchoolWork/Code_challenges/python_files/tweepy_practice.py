import tweepy

auth = tweepy.OAuthHandler('U8cqX60tkVaElYwi2tSF6juU3', '5PvyrWArTnLRnEwvnrMXLAZW8MWlsnrXEOWy1lJEqNi7IGBM7A')
auth.set_access_token('3253921376-59a5Q52Qm6FMDorvvHDSttQtp6vRYennGGhIPga', 'NSprt2x9paoXQWpccbTU6bbyLJ7nnY7vBIlsfTItDSVO6')

api = tweepy.API(auth)
me = api.get_user('classexamplebot')
#public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print tweet.text

search = raw_input("What tweets are you interested in looking for?")
tweet_search = api.search(search)
print tweet_search


# api.update_status(status=' ')
