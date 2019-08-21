import pymongo
from bson import ObjectId

client = pymongo.MongoClient("mongodb://localhost:27017")
db = client["mybase"]
table = db["mytable"]
print("I alive)")

id = "5d5d79621bcc4aca1ac7c1e3"
res = table.find_one({"_id": ObjectId(id)})
print(res)