#!/usr/bin/env python
import yaml
from flask import jsonify
from flask import Flask, jsonify, request, redirect
import pymongo
import random
from datetime import datetime
from bson.json_util import dumps, loads
import uuid
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

    device_name = data['device_name']
    device_brand = data['device_brand']
    device_storage = data['device_storage']
    device_connectivity = data['device_connectivity']
    price = data['price']
    color = data['color']
    img = data['img']
    id_hp = data['id_hp']
    qty_order = data['qty_order']

    currentCollection.insert_one({
        'device_name': device_name,
        'device_brand': device_brand,
        'device_storage': device_storage,
        'device_connectivity': device_connectivity,
        'price': price,
        'color': color,
        'img': img,
        'id_hp': id_hp,
        'qty_order': qty_order,
    })
    return jsonify({"msg": "Checkout Berhasil"}), 200


def delete_checkout_by_id(id_hp):
    mongo = open_conn()
    currentCollection = mongo.tbd.receipt
    currentCollection.delete_many({'id_order': id_hp})
    return jsonify({"msg": "Checkout Berhasil Dihapus"}), 200


def get_all_order():
    mongo = open_conn()
    currentCollection = mongo.tbd.order
    cursor = currentCollection.find({})
    json_data = dumps(cursor, indent=2)
    return json_data


def get_order_by_id(id_order):
    mongo = open_conn()
    currentCollection = mongo.tbd.order
    data = currentCollection.find_one({"id_order": id_order})
    json_data = dumps(data, indent=2)
    return json_data


def insert_order(data):
    mongo = open_conn()
    currentCollection = mongo.tbd.order

    # product
    device_name = data['device_name']
    device_brand = data['device_brand']
    device_storage = data['device_storage']
    device_connectivity = data['device_connectivity']
    device_price = data['device_price']
    color = ['color']
    img = data['img']
    id_hp = data['id_hp']
    qty_order = data['qty_order']
    total_price = data['total_price']

    # detail_user
    address = data['address']
    email = data['email']
    id_user = data['id_user']
    name = data['name']
    phone_number = data['phone_number']

    # order
    # order_id = data['order_id']
    # order_time = data['order_time']
    order_id = uuid.uuid4()
    order_time = datetime.now()

    currentCollection.insert_one({
        'device_name': device_name,
        'device_brand': device_brand,
        'device_storage': device_storage,
        'device_connectivity': device_connectivity,
        'device_price': device_price,
        'color': color,
        'img': img,
        'id_hp': id_hp,
        'qty_order': qty_order,
        'total_price': total_price,
        'address': address,
        'email': email,
        'id_user': id_user,
        'name': name,
        'phone_number': phone_number,
        'order_id': order_id,
        'order_time': order_time
    })
    return jsonify({"msg": "Order Berhasil"}), 200


def delete_order_by_id(id_order):
    mongo = open_conn()
    currentCollection = mongo.tbd.receipt
    currentCollection.delete_many({'id_order': id_order})
    return jsonify({"msg": "Order Berhasil Dihapus"}), 200
