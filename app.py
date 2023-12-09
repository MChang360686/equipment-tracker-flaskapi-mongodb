#!/usr/bin/python3

from flask import Flask, jsonify, request
import dotenv
from pymongo import MongoClient


app = Flask(__name__)

@app.route('/')
def helloworld():
    return("Hello World")

@app.route('/people', methods=['GET', 'POST'])
def getPeople():
    return("Returns people")

@app.route('/equipment')
def getEquipment():
    return("Returns Equipment")

@app.route('/people/')
def getPerson():
    return("Returns specific person")

if __name__ == '__main__':
    app.run()