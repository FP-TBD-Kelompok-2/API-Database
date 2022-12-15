# sql_rdbms.py
import os
import pymysql
from flask import jsonify

db_user = os.environ.get('CLOUD_SQL_USERNAME')
db_password = os.environ.get('CLOUD_SQL_PASSWORD')
db_name = os.environ.get('CLOUD_SQL_DATABASE_NAME')
db_connection_name = os.environ.get('CLOUD_SQL_CONNECTION_NAME')


def open_connection():
    unix_socket = '/cloudsql/{}'.format(db_connection_name)
    try:
        if os.environ.get('GAE_ENV') == 'standard':
            conn = pymysql.connect(user=db_user,
                                   password=db_password,
                                   unix_socket=unix_socket,
                                   db=db_name,
                                   cursorclass=pymysql.cursors.DictCursor
                                   )
    except pymysql.MySQLError as e:
        return e
    return conn


def get():
    conn = open_connection()
    with conn.cursor() as cursor:
        result = cursor.execute('SELECT * FROM songs;')
        songs = cursor.fetchall()
        if result > 0:
            got_songs = jsonify(songs)
        else:
            got_songs = 'No Songs in DB'
        return got_songs


def get_all_hp():
    conn = open_connection()
    with conn.cursor() as cursor:
        result = cursor.execute('SELECT * FROM handphones;')
        handphones = cursor.fetchall()
        if result > 0:
            got_handphones = jsonify(handphones)
        else:
            got_handphones = 'No Handphone in DB'
        return got_handphones


def insert_hp(hp):
    try:
        conn = open_connection()
        with conn.cursor() as cursor:
            cursor.execute(
                'INSERT INTO handphones (device_name, device_brand, device_storage, device_connectivity, device_battery, cpu_name, cpu_cores, cpu_clock, antutu_score, description, stock, price, color, img) VALUES( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);',
                (hp["device_name"], hp["device_brand"], hp["device_storage"], hp["device_connectivity"], hp["device_battery"], hp["cpu_name"], hp["cpu_cores"], hp["cpu_clock"], hp["antutu_score"], hp["description"], hp["stock"], hp["price"], hp["color"], hp["img"]))
        conn.commit()
        conn.close()
        return jsonify({"msg": f"{hp['device_name']} added"}), 200
    except Exception as e:
        return jsonify({"msg": f"{e}"}), 400


def update_hp_stock(hp):
    try:
        conn = open_connection()
        with conn.cursor() as cursor:
            cursor.execute(
                'UPDATE handphones SET stock = %s WHERE id_hp = %s;',
                (hp["stock"], hp["id_hp"]))
        conn.commit()
        conn.close()
        return jsonify({"msg": f"stock id {hp['id_hp']} updated"}), 200
    except Exception as e:
        return jsonify({"msg": f"{e}"}), 400


def get_hp_by_id(id_hp):
    conn = open_connection()
    with conn.cursor() as cursor:
        result = cursor.execute(
            'SELECT * FROM handphones WHERE id_hp = %s;', (id_hp))
        handphone = cursor.fetchone()
        if result > 0:
            got_handphone = jsonify(handphone)
        else:
            got_handphone = 'No Handphone in DB'
        return got_handphone


def delete_hp_by_id(id_hp):
    try:
        conn = open_connection()
        with conn.cursor() as cursor:
            cursor.execute(
                'DELETE FROM handphones WHERE id_hp = %s;', (id_hp))
        conn.commit()
        conn.close()
        return jsonify({"msg": f"handphone id {id_hp} deleted"}), 200
    except Exception as e:
        return jsonify({"msg": f"{e}"}), 400


def get_all_user():
    conn = open_connection()
    with conn.cursor() as cursor:
        result = cursor.execute('SELECT * FROM users;')
        users = cursor.fetchall()
        if result > 0:
            got_users = jsonify(users)
        else:
            got_users = 'No User in DB'
        return got_users


def insert_user(user):
    try:
        conn = open_connection()
        with conn.cursor() as cursor:
            cursor.execute(
                'INSERT INTO users (name, email, password, phone_number, address) VALUES( %s, %s, %s, %s, %s);',
                (user["name"], user["email"], user["password"], user["phone_number"], user["address"]))
        conn.commit()
        conn.close()
        return jsonify({"msg": f"{user['email']} added"}), 200
    except Exception as e:
        return jsonify({"msg": f"{e}"}), 400


def get_user_by_id(id_user):
    conn = open_connection()
    with conn.cursor() as cursor:
        result = cursor.execute(
            'SELECT * FROM users WHERE id_user = %s;', (id_user))
        user = cursor.fetchone()
        if result > 0:
            got_user = jsonify(user)
        else:
            got_user = 'No User in DB'
        return got_user
