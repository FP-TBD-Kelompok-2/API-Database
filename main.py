# main.py
from flask import Flask, request
from DB.sql_rdbms import *
from DB.redis_keyvalue import *
from DB.mongo_documentdb import *

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

# =========== END OF SQL =========== #
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
# =========== END OF REDIS ==========  #

# =========== MONGODB ===========  #
@app.route('/checkout', methods=['GET'])
def get_checkout():
    return get_all_checkout()

# get checkout by id
@app.route('/checkout/<int:id_checkout>', methods=['GET'])
def detail_checkout(id_checkout):
    return get_checkout_by_id(id_checkout)


# insert checkout
@app.route('/checkout/add', methods=['POST'])
def add_checkout():
    if not request.is_json:
        return jsonify({"msg": "Missing JSON in request"}), 400
    return insert_checkout(request.get_json())

# delete checkout
@app.route('/checkout/<int:id_checkout>/delete', methods=['DELETE'])
def delete_checkout(id_checkout):
    return delete_checkout_by_id(id_checkout)


if __name__ == '__main__':
    app.run()
