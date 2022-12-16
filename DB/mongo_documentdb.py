#!/usr/bin/env python
import yaml
from flask import jsonify
from flask import Flask, jsonify, request, redirect
import pymongo
import random
from datetime import datetime
from bson.json_util import dumps, loads
with open("./app.yaml", "r") as stream:
    try:
        env = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)


HOST_URI = str(env["env_variables"]["CLOUD_MONGO_URI"])

def open_conn():
    return pymongo.MongoClient(HOST_URI)


def get_all_checkout():
    mongo = open_conn()
    currentCollection = mongo.tbd.receipt
    cursor = currentCollection.find({})
    json_data = dumps(cursor, indent=2)
    return json_data


def get_checkout_by_id(id_checkout):
    mongo = open_conn()
    currentCollection = mongo.tbd.receipt
    data = currentCollection.find_one({"id_order": id_checkout})
    json_data = dumps(data, indent=2)
    return json_data


def insert_checkout(data):
    mongo = open_conn()
    currentCollection = mongo.tbd.receipt

    color = data['color']
    device_brand = data['device_brand']
    device_name = data['device_name']
    device_storage = data['device_storage']
    id_hp = data['id_hp']
    img = data['img']
    price = data['price']
    stock = data['stock']
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
    return jsonify({"msg": "Checkout Berhasil"}), 200


def delete_checkout_by_id(id_checkout):
    mongo = open_conn()
    currentCollection = mongo.tbd.receipt
    currentCollection.delete_many({'id_order': id_checkout})
    return jsonify({"msg": "Checkout Berhasil Dihapus"}), 200
