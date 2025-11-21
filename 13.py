from flask import Flask

airport_db={
    "EFHK":{"Name": "Helsinki-Vantaa Airport", "Location": "Helsinki"}}

app= Flask(__name__)
@app.route('/airport/<icao>', methods= ["GET"])
def get_airport_data(icao):
    icao= icao.upper()
    airport= airport_db.get(icao)

    if airport:
        response = {
            "ICAO" : icao,
            "Name" : airport["Name"],
            "Location": airport["Location"]
        }
        return response, 200

    else:
        response = {
            "error" : "airport not found"
        }
    return response, 404

if __name__ == '__main__':
    app.run(debug=False, use_reloader=False, host='127.0.0.1', port= 5000)

