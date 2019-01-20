#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 20 14:06:20 2019

@author: lechuza
"""

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

#requires a consumer token and consumer secret
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

#achieve access at the consumer level... this call requests the access token and retrieves the authorization url for the user to authorize our consumer

try:
    redirect_url = auth.get_authorization_url()
except tweepy.TweepError:
    print('Error! Failed to get request token.')

#although I set the arguments in earlier code, these access variables can also be retrieved via the auth object
auth.set_access_token(access_token, secret)
api = tweepy.API(auth)
#make the rest of the code obey the rate limits
api = tweepy.API(auth, wait_on_rate_limit = True)
api.update_status('tweepy + oauth!')


#object or attribute of interest when parsing or scraping tweets using cursor on a manual (non-streaming) basis - ultimately we are interested in the text of posts and possibly the titles of posted articles
    
#explore the API object methods... optimal form to call/retrieve is via the cursor   
#returns a list of status objects
lista = []
for status in tweepy.Cursor(api.home_timeline).items():
    lista.append(status)
    
lista[0]    
type(lista[0])
first = lista[0]
first_json = json.dumps(first._json)
#the above returns a string
type(first_json)
json_obj = json.loads(first_json)
json_obj.keys()

#keys of interest
json_obj['text']
json_obj['user']['name']
json_obj['entities'] # "urls" and "media"

#attempt to direct queries at only the following "friends"
#@brooklynpaper, @citylab

#user_id = "brooklynpaper",
target_status = []
for status in tweepy.Cursor(api.user_timeline, id = "brooklynpaper", tweet_mode = "extended").items():
    target_status.append(status)
    
first_tgt = json.loads(json.dumps(target_status[0]._json))
first_tgt
first_tgt.keys()
first_tgt['text']
first_tgt['user']['name']
first_tgt['entities']['urls'] # "urls" and "media"
first_tgt['media']

scnd_tgt = json.loads(json.dumps(target_status[1]._json))
scnd_tgt
scnd_tgt.keys()
scnd_tgt['full_text']
scnd_tgt['user']['name']
scnd_tgt['entities']['urls'] # "urls" and "media"
scnd_tgt['media']

#select elements of interest... if possible discard those having 0 probability of involing climate news... write/store those elements - include all relevant meta data... then kick off workflow to navigate to url and scrape the article
