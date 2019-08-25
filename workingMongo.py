import pymongo
from bson import ObjectId
from collections import defaultdict

# client = pymongo.MongoClient("mongodb://localhost:27017")
# db = client["mybase"]
# meta = db["meta"]
# work = db["0"]
#
# dicttown = defaultdict(list)
# for i in work.find({}, {"town":1, "birth_date":1, "_id":0}):
#     dicttown[i["town"]].append(i["birth_date"])
# print(dict(dicttown))
from datetime import datetime
print(datetime.now())


# test.insert_one({"id":2, "rel" : [1, 2]})

# print(test[1])

# def getImportId():
#     importid = meta.find_one({"_id":"import_id"})
#     if importid:
#         meta.update_one({"_id":"import_id"}, {"$inc":{"value":1}})
#         importid = importid["value"] + 1
#     else:
#         meta.insert_one({"_id":"import_id", "value":0})
#         importid = 0
#     return importid
#
#

# #
# # a = table.insert_one(data)
# #
# #
# # x = table.find_one({"_id": a.inserted_id})
# # d = {i["citizen_id"]:i for i in x}
# # print(d)
#
#
# a = db.collection_names()
# b = db["10"]
# print([a, b])

# id = "5d5d79621bcc4aca1ac7c1e3"
# res = table.find_one({"_id": ObjectId(id)})
# print(res)