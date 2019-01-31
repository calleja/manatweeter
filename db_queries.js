use manatwitter
db.getCollectionNames()
db.tweets.find().limit(3)

'delete the collection
db.tweets.remove({})

db.tweets.find().count()
db.tweets.find({'expanded_url':{$ne:null}}).count() '117/140

'create the articles collection
db.createCollection('articles')

db.articles.find()