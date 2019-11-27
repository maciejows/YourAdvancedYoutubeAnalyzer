import os
from flask_cors import CORS
from flask import Flask, request, jsonify


app = Flask(__name__)
CORS(app)

@app.route("/test",methods=["POST","PUT","GET"])
def test():
    if request.method == "GET":
        return jsonify("GET")
    elif request.method == "PUT":
        print(request.data)
        return jsonify("PUT")
    elif request.method == "POST":
        print(request.data)
        return jsonify("POST")

app.run(host='0.0.0.0')