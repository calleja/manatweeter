import tweepy
import json

#consumer keys
#there are two classes of API keys and secrets: application/consumer level, which is associated with the application and access level, which verifies the user account associated with the app and also provides user verification tokens for API endpoint activity

#API Key: XJbGIYzWOShWm9stiRR2LvsGW 
#API secret key: op0bmrAZaR2BClP3xWsM52DzG42GhYmB4D2irFmZn5C1eIV5uJ

#access tokens acquired from the twitter interface, but this can also be retrieved from tweepy as methods from the consumer object:
#4852117881-VMeABtN5c0TI4yWthVyFzwLlOlq3Spl7uCCFdNa (Access token)
#6EeYQ9YWRQBwRMk2EckvDYZcJYCheHT4D6OmiDn0d0Vyw (Access token secret)

consumer_key = "XJbGIYzWOShWm9stiRR2LvsGW"
consumer_secret = "op0bmrAZaR2BClP3xWsM52DzG42GhYmB4D2irFmZn5C1eIV5uJ" 

secret = "6EeYQ9YWRQBwRMk2EckvDYZcJYCheHT4D6OmiDn0d0Vyw"
access_token = "4852117881-VMeABtN5c0TI4yWthVyFzwLlOlq3Spl7uCCFdNa"



def test(hashtag,noItems=10,lsExtraKeywords = None):
	#requires a consumer token and consumer secret
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

	#Api Access
	api = tweepy.API(auth)
	
	#Select tweets based on hashtag
	tweets = tweepy.Cursor(api.search, q=hashtag).items(noItems)
	
	#Search for relevant tweets to respond to
	countTweet = 0
	countPrint = 0
	for tweet in tweets:
		countTweet += 1
		if (not lsExtraKeywords or searchForText(tweet.text,lsExtraKeywords)) and not searchForClimateText(tweet.text) and tweet.lang == 'en':
			countPrint += 1
			print(countPrint)
			#print(tweet.__dict__.keys())
			print(tweet.id)
			print(tweet.created_at)
			print(tweet.lang)
			#print(tweet.author)
			print(tweet.user.name)
			print(tweet.user.screen_name)
			print(tweet.text)
	
	print("\n\nTotal Tweets: " + str(countTweet))

def searchForClimateText(txtTweet):
	lsKeyWords = ['climate','global warming','environment']
	
	return searchForText(txtTweet,lsKeyWords)

def searchForText(txt, lsKeyWords):
	
	for keyWord in lsKeyWords:
		if keyWord in txt.lower():
			return True
	
	return False
