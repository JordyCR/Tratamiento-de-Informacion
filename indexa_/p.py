import pymongo


client = pymongo.MongoClient()
print client.database_names()
db = client['urls']


### MongoDB Links
# http://stackoverflow.com/questions/15748486/best-way-to-extract-all-id-from-mongodb-collection
# http://stackoverflow.com/questions/16889666/checking-if-record-exists-in-mongodb
# https://api.mongodb.org/python/2.8/api/pymongo/collection.html
# https://docs.mongodb.org/manual/core/cursors/#read-operations-cursors
# https://docs.mongodb.org/manual/reference/method/db.collection.find/
# https://docs.mongodb.org/manual/reference/object-id/
# http://api.mongodb.org/python/current/tutorial.html
# 