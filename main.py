# main.py
from flask import Flask, request
from DB.sql_rdbms import *
from DB.redis_keyvalue import *

app = Flask(__name__)

#  =================== SQL ===================  #
@app.route('/', methods=['GET'])
def home():
    return 'welcome to navisatya consign store'


@app.route('/hp', methods=['GET'])
def get_hp():
    return get_all_hp()


@app.route('/hp/add', methods=['POST'])
def add_hp():
    if not request.is_json:
        return jsonify({"msg": "Missing JSON in request"}), 400
    return insert_hp(request.get_json())


@app.route('/hp/stock', methods=['POST'])
def update_stock():
    if not request.is_json:
        return jsonify({"msg": "Missing JSON in request"}), 400
    return update_hp_stock(request.get_json())


@app.route('/hp/<int:id_hp>', methods=['GET'])
def detail_hp(id_hp):
    return get_hp_by_id(id_hp)


@app.route('/hp/<int:id_hp>/delete', methods=['DELETE'])
def delete_hp(id_hp):
    return delete_hp_by_id(id_hp)


@app.route('/user', methods=['GET'])
def get_user():
    return get_all_user()


@app.route('/user/add', methods=['POST'])
def add_user():
    if not request.is_json:
        return jsonify({"msg": "Missing JSON in request"}), 400
    return insert_user(request.get_json())


@app.route('/user/<int:id_user>', methods=['GET'])
def detail_user(id_user):
    return get_user_by_id(id_user)


# =========== REDIS ===========  #

@app.route('/cart', methods=['GET'])
def get_cart():
    return get_all_cart()


@app.route('/cart/add', methods=['POST'])
def add_cart():
    if not request.is_json:
        return jsonify({"msg": "Missing JSON in request"}), 400
    return insert_cart(request.get_json())

@app.route('/cart/<int:id_cart>/checkout', methods=['GET'])
def checkout_cart(id_cart):
    return checkout_cart_by_id(id_cart)


@app.route('/cart/<int:id_cart>/delete', methods=['DELETE'])
def delete_cart(id_cart):
    return delete_cart_by_id(id_cart)


if __name__ == '__main__':
    app.run()
