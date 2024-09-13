from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

def db_connection():
    connection = mysql.connector.connect(
        host='mysql',
        user='root',
        password='root', 
        database='sample'
    )
    return connection


@app.route('/', methods=['GET'])
def hello():
    return 'Hello, World!'

@app.route('/data', methods=['GET'])
def get_data():
    connection = db_connection()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM num_data') 
    results = cursor.fetchall()
    return jsonify(results)


@app.route('/data', methods=['POST'])
def add_data():
    connection = db_connection()
    cursor = connection.cursor()
    insert_query = 'INSERT INTO num_data (value) VALUES (%s)'
    value = request.json['value']  
    cursor.execute(insert_query, (value,))
    connection.commit()
    return jsonify({'message': 'Data added successfully!'})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)