#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 17:21:39 2019

@author: lechuza
"""

import pymongo
import pandas
from bson.objectid import ObjectId

#connect to mongo instance
client = pymongo.MongoClient('localhost', 21999)
#connect to a database... there is also a collections level
db = client.manatwitter
#collections are created upon initial assertion into them at run time
db.tweets.insert_

#takes an iterable as argument... returns an instance of InsertManyResult from which I can query (as an attribute) the list of _ids inserted into the collection
db.tweets.insert_many(h)

h[67].keys()

'full_text', 'user_name', 'expanded_url', 'creation', 'screenname', 'dateDict', 'hashtags'

#iterate through every single document within the tweets collection, extract the expanded_url text (if there is one), then download that text and store the text into a different collection - the 'articles' collection

#treat the collection as an iterable and index for 'expanded_url'
db.tweets
['expanded_url']

#attempt to search by objectID ... ObjectId("5c4cf54faf41c1250e094b2f")
single = db.tweets.find_one({"_id": ObjectId("5c4cf54faf41c1250e094b2f")})
single['expanded_url']
#with the expanded_url in hand, attempt to download the text from the url

from newspaper import Article
import newspaper

text = 