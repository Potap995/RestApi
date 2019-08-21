import pymongo
client = pymongo.MongoClient("mongodb:27017")
db = client["mybase"]
table = db["mytable"]
table.delete_many({})