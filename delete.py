import pymongo
client = pymongo.MongoClient("mongodb://localhost:27017")
db = client["mybase"]
meta = db["meta"]
meta.delete_many({})
print(db.collection_names())
for i in db.collection_names():
    db.drop_collection(i)