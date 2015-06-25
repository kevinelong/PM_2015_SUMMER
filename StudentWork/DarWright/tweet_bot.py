import tweepy
from get_weather import Weather

# setting up tweedy api with keys and fun things.
consumer_key = 'U8cqX60tkVaElYwi2tSF6juU3'
consumer_secret = '5PvyrWArTnLRnEwvnrMXLAZW8MWlsnrXEOWy1lJEqNi7IGBM7A'
access_token = '3253921376-59a5Q52Qm6FMDorvvHDSttQtp6vRYennGGhIPga'
access_token_secret = 'NSprt2x9paoXQWpccbTU6bbyLJ7nnY7vBIlsfTItDSVO6'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print tweet.text

user = api.get_user('classexamplebot')

# print user.screen_name
# print user.followers_count
# for friend in user.friends():
#     print friend.screen_name
#
# api.update_status("Holy cow its a #tweet!")

#  word search via twitter
# interest = raw_input("What are you interested in?> ")
# results = api.search(interest)
# for x in results:
#     print x


# get a name, find the weather at the twitter location of the name of the famous person
name = raw_input("Gimmie a name or @Handle: ")
results = api.search_users(name)
print "I found\033[0;34m", results[0].name, "\033[0min\033[0;36m", results[0].location, "\033[0m"
weather = Weather()
print weather.get_weather(weather.get_id_by_location(results[0].location))


