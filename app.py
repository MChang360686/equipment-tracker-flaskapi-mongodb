#!/usr/bin/python3

import os
from flask import Flask, jsonify, request
from dotenv import load_dotenv
from pymongo import MongoClient
from bson import json_util
import json


app = Flask(__name__)
app.config["MONGO_URI"] = os.environ.get("DB_URI")

url = os.environ.get("DB_URI")
port = os.environ.get("PORT_NUM")

client = MongoClient(url, port)

db = client['test']

@app.route('/')
def helloworld():
    people = list(db.get_collection("people").find())
    return(json.loads(json_util.dumps(people)))

@app.route('/people', methods=['GET'])
def getPeople():
    people = list(request.test["people"].find(limit=100))
    return people

@app.route('/equipment', methods=['GET', 'POST'])
def getEquipment():
    return("Returns Equipment")

@app.route('/people/', methods=['GET', 'POST', 'PUT'])
def getPerson():
    return("Returns specific person")

if __name__ == '__main__':
    app.run()


    """
    We can add the following to run() for https.
    May trigger a browser warning though.

    ssl_context="adhoc"
    """