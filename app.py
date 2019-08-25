from flask import Flask, jsonify, request, abort
from flask_restful import Api, Resource
import pymongo
import logging
import re
from datetime import datetime
import numpy as np


client = pymongo.MongoClient("mongodb:27017")
# client = pymongo.MongoClient("mongodb://localhost:27017")
db = client["mybase"]
meta = db["meta"]
FIELDS = ("citizen_id", "town", "street", "building", "apartment", "name", "birth_date", "gender", "relatives")
GENDERS = ("male", "female")

def getImportId(change=True):
    importid = meta.find_one({"_id":"import_id"})
    if not change:
        return importid["value"] if importid else -1
    if importid:
        meta.update_one({"_id":"import_id"}, {"$inc":{"value":1}})
        importid = importid["value"] + 1
    else:
        meta.insert_one({"_id":"import_id", "value":0})
        importid = 0
    return importid


def isValidString(value):
    return isinstance(value, str) and len(value) >= 0 and len(value) <= 256


def isValidNumber(value):
    return  isinstance(value, int) and value >= 0


def isValid(citizen, citizens, patch=False):
    if patch and len(citizen) < 9:
        return False

    for field in citizen:

        value = citizen[field]

        if field not in FIELDS:
            return False

        if field == "citizen_id":
            if patch:
                return False
            if not isValidNumber(value):
                return False

        if field == "name":
            if not isValidString(value):
                return False

        if field in ("town", "street", "building"):
            if not isValidString(value):
                return False
            if not re.search("[\d\w]", value):
                return False

        if field in ("citizen_id", "apartment"):
            if not isValidNumber(value):
                return False

        if field == "gender":
            if value not in GENDERS:
                return False

        if field == "birth_date":
            try:
                datetime.strptime(value, "%d.%m.%Y")
            except:
                return False

        if field == "relatives" and not patch:
            if not isinstance(value, list):
                return False
            for citizen_id in value:
                if not citizens.get(citizen_id):
                    return False
                if citizen["citizen_id"] not in citizens[citizen_id]["relatives"]:
                    return False

    return True


app = Flask(__name__)
api = Api(app)


class Imports(Resource):

    def post(self):
        data = request.json #check data
        logging.warning(data)
        if not data:
            abort(400)
        # data = json.loads(data)
        # logging.warning(data)
        real_data = {citizen["citizen_id"]:citizen for citizen in data.get("citizens", [])}

        if not real_data:
            abort(400)

        logging.warning(real_data)
        for key in real_data:
            if not isValid(real_data[key], real_data):
                abort(400)

        cur_id = getImportId()
        collection = db[str(cur_id)]
        try:
            collection.insert_many(data["citizens"])
        except Exception as e:
            logging.warning(e)
            abort(400)
        res = {
            "data": {
                "import_id": cur_id
            }
        }
        return res, 201


class Citizens(Resource):

    def get(self, import_id):
        if getImportId(change=False) < int(import_id) or int(import_id) < 0:
            abort(400)
        res = db[import_id].find({}, {"_id":False})
        ret = {"data": [i for i in res]}
        return ret, 200


class Citizen(Resource):

    def patch(self, import_id, citizen_id):
        if getImportId(change=False) < int(import_id) or int(import_id) < 0:
            abort(400)

        data = request.json
        print(data)
        if not data:
            abort(400)

        if isValid(data, [], True):
            abort(400)

        res = db[import_id].find_and_modify({"citizen_id":citizen_id}, {"$set": data})
        del res["_id"]
        if "relatives" in data:
            to_unlink = set(res["relatives"]) - set(data["relatives"])
            to_link = set(data["relatives"]) - set(res["relatives"])
            #TODO check for nonexistent citizens
            for relative_id in to_unlink:
                cur = db[import_id].find_one({"citizen_id": relative_id})["relatives"]
                cur.remove(citizen_id)
                db[import_id].update_one({"citizen_id": relative_id}, {"$set": {"relatives":cur}})

            for relative_id in to_link:
                cur = db[import_id].find_one({"citizen_id": relative_id})["relatives"]
                cur.append(citizen_id)
                db[import_id].update_one({"citizen_id": relative_id}, {"$set": {"relatives":cur}})
        res.update(data)
        ret = {"data": res}
        return ret, 200


class Birthdays(Resource):

    def get(self, import_id):
        if getImportId(change=False) < int(import_id) or int(import_id) < 0:
            abort(400)

        res = db[import_id].find({}, {"_id": False})
        real_data = {citizen["citizen_id"]:citizen for citizen in res}
        print(real_data)
        months = {i:[] for i in range(1, 13)}
        for citizen_id in real_data:
            cur_months = [0]*12
            for relative_id in real_data[citizen_id]["relatives"]:
                month = datetime.strptime(real_data[relative_id]["birth_date"], "%d.%m.%Y").month #may be uncorrect
                cur_months[month-1] += 1
            for month in range(12):
                if cur_months[month] > 0:
                    months[month + 1].append({"citizen_id":citizen_id, "presents": cur_months[month]})

        ret = {"data": months}

        return ret, 200


class Percentile(Resource):

    def get(self, import_id):
        #TODO impolement percentile
        abort(400)




api.add_resource(Imports, "/imports")
api.add_resource(Citizens, "/imports/<import_id>/citizens")
api.add_resource(Citizen, "/imports/<import_id>/citizens/<citizen_id>")
api.add_resource(Birthdays, "/imports/<import_id>/citizens/birthdays")
api.add_resource(Percentile, "/imports/<import_id>/towns/stat/percentile/age")

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8081, debug=True)