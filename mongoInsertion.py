#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 17:21:39 2019

Tweets are stored via inserting into a mongodb. 
Connection to the mongodb is established, a collection is either referenced or created, then all tweets are inserted via iterable batch form.

Once tweets are stored, expanded urls (twitter naming convention) are retrieved/queried in an article text downloading workflow. Article text/html is then stored in a different collection within the mongodb along with a reference ID to the original tweet.
"""

import pymongo
import pandas as pd
from bson.objectid import ObjectId
from newspaper import Article
#walk through installation of all dependencies: https://newspaper.readthedocs.io/en/latest/
import nltk

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
single
single['expanded_url']
#with the expanded_url in hand, attempt to download the text from the url


article = Article(single['expanded_url'])
article.download()
article.parse()
texty = article.text
nltk.download() # will display a dialogue box, click on download all nlp library/packages
article.nlp() #subsequent attributes this creates: summary and keywords
article.summary
#this may be a word frequency hierarchy
article.keywords

#STRATEGY: ideally each of the attributes and results of the nlp is also stored in the database, aside from author, date, source... can also manually build a tldf rank
#variables to mine from each article:
#word frequency/histogram

#Often a simple bigram approach is better than a 1-gram bag-of-words model for tasks like documentation classification.

#ARTICLE COLLECTION CREATION
#iterate through each document in the 'tweet' collection and if there is an expanded url, use the newspaper.Article library to extract the text... will also need to store the tweet document ID in the article document to facilitate "joins"

#only retrieve documents where expanded_url != None
tweet_cursor = db.tweets.find({'expanded_url': {'$ne': None}})[1:20]

#extract text from this article    
def extract_article_tgt_data(urlInput):
    article = Article(urlInput)
    article.download()
    article.parse()
    return(article.text)
    
test_lista = []    
for doc in tweet_cursor:
    #iterate through the urls of each reference article from the tweets, build a document that includes the full text of the article (acquired via an auto scraping library)
    article_url = doc['expanded_url']
    if article_url is not None:
        #create a new document, this will be stored in the 'Article' collection 
        art_doc = {}
        #previously defined function
        art_doc['article_text'] = extract_article_tgt_data(article_url)
        art_doc['_id'] = doc['_id']
        art_doc['tweet_id'] = doc['tweet_id']
        art_doc['user_name'] = doc['user_name']
        #insert_news_doc(doc)
        test_lista.append(art_doc)
    else:
        next
    
db.collection_names()
test_lista[9]['tweet_id']

#returns a cursor object
db.articles.find({'tweet_id': test_lista[9]['tweet_id']}).count()

#insert the "article" document into the 'articles' collection of the database; first ensure there is no pre-existing record
def insert_news_doc(document):
    #ensure there is no pre-existing record in the collection
    if db.articles.find({'tweet_id': document['tweet_id']}).count() == 0:
        print('inserting article document')
        db.articles.insert_one(document)
    else: 
        print(db.articles.find({'tweet_id': document['tweet_id']}).count())
        
for i in test_lista:
    insert_news_doc(i)     
    
    