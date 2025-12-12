from flask import Flask, jsonify
import mariadb, json
from mariadb._mariadb import cursor

connection= mariadb.connect(
    host = '127.0.0.1',
    port = 3306,
    user = 'root',
    password = '1234',
    database = 'flight_game',
    autocommit = 'True')
print("Successfully connected to MariaDB!")

airport_db = {
    "EFHK": {"Name": "Helsinki-Vantaa Airport", "Location": "Helsinki"}}

app = Flask(__name__)


@app.route('/airport/<ident>')
def get_airport_data(ident):
    ident = ident.upper()
    airport = airport_db.get(ident)
    cursor = connection.cursor()
    cursor.excecute("SELECT name, municipality FROM airport WHERE ident=?", (ident))
    result = cursor.fetchone()
    cursor.close()



    if ident:
        result = {
            "ICAO": icao,
            "Name": ident["Name"],
            "Location": ident["Location"]
        }


    else:
        response = {
            "error": "airport not found"
        }
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=False, use_reloader=True, host='127.0.0.1', port=5000)