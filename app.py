from flask import Flask, jsonify, request
from flask_restful import Api, Resource
import pymongo
import logging
import json
from bson import ObjectId


client = pymongo.MongoClient("mongodb:27017")
db = client["mybase"]
table = db["mytable"]

app = Flask(__name__)
api = Api(app)

class Imports(Resource):

    def post(self):
        data = request.get_json(force=True)
        if not data:
            return {'error': 'bad request'}, 400
        logging.warning(data)
        # TODO make checkers for fields
        try:
            a = table.insert_one(data)
        except Exception as e:
            logging.warning(e)
        logging.warning(dir(a.inserted_id))
        logging.warning(str(a.inserted_id))
        res = {
            "data": {
                "import_id": str(a.inserted_id)
            }
        }
        return jsonify(res)

class Citizens(Resource):

    def get(self, id):
        # TODO add check for existance
        res = table.find_one({"_id": ObjectId(id)})
        del res["_id"]
        a = {"data": res}
        return jsonify(a)


api.add_resource(Imports, "/imports")
api.add_resource(Citizens, "/imports/<id>/citizens")

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)