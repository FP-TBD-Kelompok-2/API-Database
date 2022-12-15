#!/usr/bin/env python
import redis
import yaml
from flask import jsonify
import json




# def open_connection():
#     return redis.Redis(host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASSWORD)


def convert_str(x):
    return str(x, "utf-8")
# list = [{
#     "name": "samsung",
#     "price": 1000000,
#     "stock": 100,
#     "qty_order":10,
#     "total_price": 10000000,
#     "gambar": "https://www.google.com"
# }]

# r.hset("product_id:3", "name", "Samsung S22 Ultra")
# r.hset("product_id:3", "price", 1000000)
# r.hset("product_id:3", "stock", 100)
# r.hset("product_id:3", "qty_order", 10)

# buat ngambil semua key
# for key in r.scan_iter("product_id:*"):
#     # delete the key
#     print(convert_str(key))

# buat ngambil value dari setiap key
#     print(r.hgetall(key))
# print(type(dict))
# r.set('card', dict)


# Struktur Insert Data
# {
#     "id_hp": 1,
#     "nama_hp": "Samsung Galaxy S21",
#     "harga_hp": 10000000,
#     "qty_order": 10,
#     "qty_stock": 100,
#     "gambar_hp": "https://www.samsung.com/id/smartphones/galaxy-s21-5g/images/galaxy-s21-5g-1.jpg"
# }

with open("./app.yaml", "r") as stream:
    try:
        env = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)

REDIS_HOST = str(env["env_variables"]["CLOUD_REDIS_HOST"])
REDIS_PORT = int(env["env_variables"]["CLOUD_REDIS_PORT"])
REDIS_PASSWORD = str(env["env_variables"]["CLOUD_REDIS_PASSWORD"])


def open_conn():
    return redis.Redis(host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASSWORD)


def get_all_cart():
    r = open_conn()
    list = []
    for key in r.scan_iter("cart_id:*"):
        list.append(convert_str(key))
    if len(list) == 0:
        return jsonify({"msg": "Cart Kosong"}), 200

    list_dict = []
    for key in list:
        list_dict.append(convert_hgetall_to_dict(r.hgetall(key)))

    return jsonify(list_dict), 200

import ast
# byte_str = b"{'one': 1, 'two': 2}"
# dict_str = byte_str.decode("UTF-8")
# mydata = ast.literal_eval(dict_str)
# print(repr(mydata))

def convert_hgetall_to_dict(data):
    dict = {}
    for key in data:
        dict[key.decode("UTF-8")] = data[key].decode("UTF-8")
    return dict





def insert_cart(data):
    r = open_conn()
    id_hp = data["id_hp"]
    nama_hp = data["nama_hp"]
    harga_hp = data["harga_hp"]
    qty_order = data["qty_order"]
    qty_stock = data["qty_stock"]
    total_harga = data["total_harga"]
    gambar_hp = data["gambar_hp"]

    if qty_order > qty_stock:
        return jsonify({"msg": "Stock tidak cukup"}), 400

    r.hset("cart_id:" + str(id_hp), "id_hp", id_hp)
    r.hset("cart_id:" + str(id_hp), "nama_hp", nama_hp)
    r.hset("cart_id:" + str(id_hp), "harga_hp", harga_hp)
    r.hset("cart_id:" + str(id_hp), "qty_order", qty_order)
    r.hset("cart_id:" + str(id_hp), "qty_stock", qty_stock)
    r.hset("cart_id:" + str(id_hp), "total_harga", total_harga)
    r.hset("cart_id:" + str(id_hp), "gambar_hp", gambar_hp)

    return jsonify({"msg": f"Berhasil menambahkan {nama_hp} ke cart".format(nama_hp)}), 200

def checkout_cart_by_id(id):
    r = open_conn()
    list = []
    for key in r.scan_iter("cart_id:*"):
        list.append(convert_str(key))
    if len(list) == 0:
        return jsonify({"msg": "Cart Kosong"}), 200
    if "cart_id:" + str(id) not in list:
        return jsonify({"msg": "Cart tidak ditemukan"}), 404
    r.delete("cart_id:" + str(id))
    return jsonify({"msg": f"Berhasil checkout"}), 200


def delete_cart_by_id(id):
    r = open_conn()
    list = []
    for key in r.scan_iter("cart_id:*"):
        list.append(convert_str(key))
    if len(list) == 0:
        return jsonify({"msg": "Cart Kosong"}), 200
    if "cart_id:" + str(id) not in list:
        return jsonify({"msg": "Cart tidak ditemukan"}), 404
    r.delete("cart_id:" + str(id))
    return jsonify({"msg": "Berhasil menghapus cart"}), 200
