#!/usr/bin/env python
import yaml
from flask import jsonify
from flask import Flask, jsonify, request, redirect
from flask_pymongo import PyMongo
import random
from datetime import datetime
from bson.json_util import dumps, loads
with open("./app.yaml", "r") as stream:
    try:
        env = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)


HOST_URI = str(env["env_variables"]["HOST_URI"])
app = Flask(__name__)
app.config['MONGO_URI'] = HOST_URI
mongo = PyMongo(app)


@app.route('/', methods = ['GET'])
def retrieveAll():
    # holder = list()
    currentCollection = mongo.db.receipt
    cursor = currentCollection.find({})

    json_data = dumps(cursor, indent = 2)

    # holder.append(currentCollection.find())
    # for i in currentCollection.find():
    #     holder.append({'id_hp': i['id_hp'], 'device_name': i['device_name'], 'device_brand': i['device_brand'],  'device_storage': i['device_storage'], 'device_connectivity': i['device_connectivity'],'device_battery': i['device_battery'], 'color': i['color'],'price': i['price'], 'img': i['img']})
    return json_data

@app.route('/<int:id_order>', methods = ['GET'])
def retriveFromID(id_order):
    currentCollection = mongo.db.receipt
    data = currentCollection.find_one({"id_order": id_order})
    json_data = dumps(data, indent=2)
    return json_data
    # return jsonify({'id_hp': data['id_hp'], 'device_name': data['device_name'], 'device_brand': data['device_brand'],  'device_storage': data['device_storage'], 'device_connectivity': data['device_connectivity'],'device_battery': data['device_battery'], 'color': data['color'],'price': data['price'], 'img': data['img']})


@app.route('/postData', methods = ['POST'])
def postData():
    currentCollection = mongo.db.receipt

    color = request.json['color']
    # description = request.json['description']
    # device_battery = request.json['device_battery']
    device_brand = request.json['device_brand']
    # device_connectivity = request.json['device_connectivity']
    device_name = request.json['device_name']
    device_storage = request.json['device_storage']
    id_hp = request.json['id_hp']
    img = request.json['img']
    price = request.json['price']
    stock = request.json['stock']
    time = datetime.now()
    id_order = random.randrange(5000, 1000000, 1254)
    currentCollection.insert_one({
                              'color': color,
                              'device_brand': device_brand,
                              'device_name': device_name,
                              'device_storage': device_storage,
                              'id_hp': id_hp,
                              'img': img,
                              'price': price,
                              'stock': stock,
                            'time': time,
                            'id_order': id_order})
    return print('Insert Succesful')

@app.route('/deleteData/<int:id_order>', methods = ['DELETE'])
def deleteData(id_order):
    currentCollection = mongo.db.receipt
    currentCollection.delete_many({'id_order': id_order})
    return print("Delete Succesful")



if __name__ == '__main__':
    app.run(debug= True)