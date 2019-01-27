# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 15:49:44 2019

@author: callejal
"""

"""
Created on Sun Jan 20 14:06:20 2019

@author: lechuza
"""

import tweepy
import json
import itertools

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
#api.update_status('tweepy + oauth!')


#object or attribute of interest when parsing or scraping tweets using cursor on a manual (non-streaming) basis - ultimately we are interested in the text of posts and possibly the titles of posted articles
    
#attempt to direct queries at only the following "friends"
#@brooklynpaper, @citylab

    
#select elements of interest... if possible discard those having 0 probability of involing climate news... write/store those elements - include all relevant meta data... then kick off workflow to navigate to url and scrape the article

#AUTO PARSING
#collect handle, date, time, tweet body, url; this requires indexing the json document and repackaging it in the document format of the database... MISSING: hashtags
   
def extraction(listOfDocs):
    lista = []
    #nested function to parse and package timestamp data of tweet
    def extractDate(dateString):
        string_list = dateString.split(" ")
        month = string_list[1]
        day_date = string_list[2]
        time_date = string_list[3]
        year_date = string_list[5]
        outputDict = {'month_date': month, 'day_date': day_date, 'time_date': time_date, 'year_date': year_date}
        return(outputDict)
    #loop through each status element of the API resultset
    for single in listOfDocs:
        first_tgt = json.loads(json.dumps(single._json))
        full_text = first_tgt['full_text']   
        user_name = first_tgt['user']['name']
        #cases there are no irls associated w/tweet
        try:
            expanded_url = first_tgt['entities']['urls'][0]['expanded_url']
        except IndexError:
            expanded_url = None
        try:
            if len(first_tgt['entities']['hashtags']) > 0:
                #list comprehension to extract only the text field of hashtags list
                hashtags = [i['text'] for i in first_tgt['entities']['hashtags']]
            else:
                hashtags = None
        except IndexError:
            hashtags = None
        creation = first_tgt['created_at']
        tweet_id = first_tgt['id']
        screenname = first_tgt['user']['screen_name']
        datedata = first_tgt['created_at']
        #parse date
        dateDict = extractDate(datedata)
        
        #compile dictionary
        final_dict = {'full_text': full_text, 'user_name': user_name, 'expanded_url': expanded_url, 'creation': creation, 'screenname': screenname, 'dateDict': dateDict, 'hashtags': hashtags, 'tweet_id': tweet_id}
        #print the compiled data as a test
        lista.append(final_dict)
    return(lista)

#old way... works! first 7 pages should return ~ 140 tweets
old_list= []
page = 1
while page < 8:
    statuses = api.user_timeline(page=page, id = "brooklynpaper", tweet_mode = "extended", count = 20, wait_on_rate_limit = True)
    if statuses:
        for status in statuses:
            # process status here
            old_list.append(status)
    else:
        # All done
        break
    page += 1  # next page

h = extraction(old_list)

old_list[9]
scnd_tgt = json.loads(json.dumps(old_list[9]._json))
scnd_tgt.keys()
scnd_tgt['entities']

[i['text'] for i in h[9]['hashtags']]
h[9]['hashtags']
