import pymongo
from bson import ObjectId

client = pymongo.MongoClient("mongodb://localhost:27017")
db = client["mybase"]
meta = db["meta"]
test = db["test"]

# test.insert_one({"id":2, "rel" : [1, 2]})

a = test.find_one({"id": 1})["rel"]
print(a, type(a))
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
data = {
    "citizens": [
        {
            "citizen_id": 1,
            "town": "Москва",
            "street": "Льва Толстого",
            "building": "16к7стр5",
            "apartment": 7,
            "name": "Иванов Иван Иванович",
            "birth_date": "26.12.1986",
            "gender": "male",
            "relatives": [2]
        },
        {
            "citizen_id": 2,
            "town": "Москва",
            "street": "Льва Толстого",
            "building": "16к7стр5",
            "apartment": 7,
            "name": "Иванов Сергей Иванович",
            "birth_date": "01.04.1997",
            "gender": "male",
            "relatives": [1]
        },
        {
            "citizen_id": 3,
            "town": "Керчь",
            "street": "Иосифа Бродского",
            "building": "2",
            "apartment": 11,
            "name": "Романова Мария Леонидовна",
            "birth_date": "23.11.1986",
            "gender": "female",
            "relatives": []
        }
    ]
}
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