#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 17:21:39 2019

Tweets are stored via inserting into a mongodb. 
Connection to the mongodb is established, a collection is either referenced or created, then all tweets are inserted via iterable batch form.

Once tweets are stored, expanded urls (twitter naming convention) are retrieved/queried in an article text downloading workflow. Article text/html is then stored in a different collection within the mongodb along with a reference ID to the original tweet.
"""

import pymongo
import pandas
from bson.objectid import ObjectId

#connect to mongo instance
client = pymongo.MongoClient('localhost', 21999)
#connect to a database... there is also a collections level
db = client.manatwitter
#collections are created upon initial insertion into them at run time

#db.collections.insert_many() takes an iterable as argument... returns an instance of InsertManyResult from which I can query (as an attribute) the list of _ids inserted into the collection
db.tweets.insert_many(h)

#test to learn the nature of all the keys
h[67].keys()

#keys of the mongo document: ['full_text', 'user_name', 'expanded_url', 'creation', 'screenname', 'dateDict', 'hashtags']

#iterate through every single document within the tweets collection, extract the expanded_url text (if there is one), then download that text and store the text into a different collection - the 'articles' collection within same db

#treat the collection as an iterable and index for 'expanded_url'

#QUERYING TWEETS in MONGO
#attempt to search by objectID ... ObjectId("5c4cf54faf41c1250e094b2f")
single = db.tweets.find_one({"_id": ObjectId("5c4cf54faf41c1250e094b2f")})
single['expanded_url']
#with the expanded_url in hand, attempt to download the text from the url

from newspaper import Article
#walk through installation of all dependencies: https://newspaper.readthedocs.io/en/latest/
import nltk

article = Article(single['expanded_url'])
article.download()
article.parse()
texty = article.text
nltk.download() # will display a dialogue box, click on download all nlp library/packages
article.nlp() #subsequent attributes this creates: summary and keywords
article.summary
#this may be a word frequency hierarchy
article.keywords
