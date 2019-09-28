import tweepy
import textblob
# from tweepy.auth import OAuthHandler


consumer_key =  'EVUzi3c2CrEWhRHuRkvzhGZiT'
consumer_secret =  'uHSfyNhrrghhbOwrL6EJVvolBPoY5lcJGTfsCs43z4kRUNWQYn'

access_token  ='414503954-43HAYArKrxmwgoBl5OhVTQ3R5kWoLjYedBEXCPBx'
access_token_secret  = 'HnlHnqsGcTw9PITR55MFk7zaULOc6s4BprvG2JnyFqk9u'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
public_tweets = api.search('Trump')
for tweet in public_tweets:
    print(tweet.text)











public_tweets = api.home_timeline()