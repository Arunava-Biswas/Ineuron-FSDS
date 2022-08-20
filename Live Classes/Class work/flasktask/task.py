from flask import Flask, request, jsonify

from mysql_conn import create_db_connection, execute_query, read_query
from mongodb_conn import connect, rec_insert, rec_find, rec_upd, rec_del


app = Flask(__name__)


@app.route('/sql_db', methods=['GET', 'POST'])
def db_conn():
    if request.method == "POST":
        host = request.json["host"]
        user = request.json["user"]
        pwd = request.json["passwd"]
        db_name = request.json['db']
        conn_db = create_db_connection(host, user, pwd, db_name)
        return jsonify(str(conn_db))


@app.route('/sql_db/tb', methods=['GET', 'POST'])
def sql_tb():
    if request.method == "POST":
        host = request.json["host"]
        user = request.json["user"]
        pwd = request.json["passwd"]
        db_name = request.json['db']
        conn = create_db_connection(host, user, pwd, db_name)
        q = "CREATE TABLE IF NOT EXISTS students(stu_name VARCHAR(80), stu_email VARCHAR(100), stu_sub VARCHAR(100));"
        result = execute_query(conn, q)
        return jsonify(str(result))


@app.route('/sql_db/insert', methods=['GET', 'POST'])
def sql_ins():
    if request.method == "POST":
        host = request.json["host"]
        user = request.json["user"]
        pwd = request.json["passwd"]
        db_name = request.json['db']
        conn = create_db_connection(host, user, pwd, db_name)
        q = "INSERT INTO students VALUES('Arunava Biswas', 'arunavabiswas44@gmail.com', 'Data Science');"
        result = execute_query(conn, q)
        return jsonify(str(result))


@app.route('/sql_db/update', methods=['GET', 'POST'])
def sql_upd():
    if request.method == "POST":
        host = request.json["host"]
        user = request.json["user"]
        pwd = request.json["passwd"]
        db_name = request.json['db']
        conn = create_db_connection(host, user, pwd, db_name)
        q = "UPDATE students SET stu_sub = 'Statistics' WHERE stu_name = 'Arunava Biswas';"
        result = execute_query(conn, q)
        return jsonify(str(result))


@app.route('/sql_db/fetch', methods=['GET', 'POST'])
def sql_fet():
    if request.method == "POST":
        host = request.json["host"]
        user = request.json["user"]
        pwd = request.json["passwd"]
        db_name = request.json['db']
        conn = create_db_connection(host, user, pwd, db_name)
        q = "SELECT * FROM students"
        result = read_query(conn, q)
        return jsonify(str(result))


@app.route('/sql_db/delete', methods=['GET', 'POST'])
def sql_del():
    if request.method == "POST":
        host = request.json["host"]
        user = request.json["user"]
        pwd = request.json["passwd"]
        db_name = request.json['db']
        conn = create_db_connection(host, user, pwd, db_name)
        q = "DELETE FROM students WHERE stu_name = 'Arunava Biswas';"
        result = execute_query(conn, q)
        return jsonify(str(result))


@app.route('/Mg_db', methods=['GET', 'POST'])
def mg_db_conn():
    if request.method == "POST":
        res = connect()
        return jsonify(str(res))


@app.route('/Mg_db/insert', methods=['GET', 'POST'])
def mg_db_insert():
    if request.method == "POST":
        coll = connect()
        # creating one record
        record = {
            "name": "Arunava",
            "email_id": "arunava@email.com",
            "subject": ["Data Science", "Big Data", "Data Analytics"]
        }
        res = rec_insert(coll, record)
        return jsonify(str(res))


@app.route('/Mg_db/fetch', methods=['GET', 'POST'])
def mg_db_fetch():
    if request.method == "POST":
        coll = connect()
        results = rec_find(coll)
        for result in results:
            return jsonify(str(result))


@app.route('/Mg_db/update', methods=['GET', 'POST'])
def mg_db_upd():
    if request.method == "POST":
        coll = connect()
        present_data = {'subject': 'Data Analytics'}
        new_data = {"$set": {'subject': 'Machine Learning'}}
        results = rec_upd(coll, present_data, new_data)
        return jsonify(str(results))


@app.route('/Mg_db/delete', methods=['GET', 'POST'])
def mg_db_del():
    if request.method == "POST":
        delete_query = {'name': 'Arunava'}
        coll = connect()
        results = rec_del(coll, delete_query)
        return jsonify(str(results))


if __name__ == "__main__":
    app.run(debug=True)