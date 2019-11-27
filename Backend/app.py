import os
from flask import Flask, send_file, jsonify, request
from YourAdvancedYoutubeAnalyzer.Backend.mozaika import histogram
from YourAdvancedYoutubeAnalyzer.Backend.url import api

app = Flask(__name__)
a = api()

@app.route('/hist',methods=["GET"])
def output():
    if request.method == "GET":
        if a.url != '':
            histogram(a.data)
            name = a.data.vidID + ".mp4"
            os.remove(name)
            return send_file("hist.png", mimetype='image/png')
        else:
            return jsonify("EMPTY URL")
    else:
        return jsonify("ERROR ONLY GET ACCEPTABLE")

@app.route('/JSON',methods=["GET"])
def json():
    if request.method == "GET":
        if a.url != '':
            heh = a.data.getContent()
            return jsonify(heh)
        else:
            return jsonify("EMPTY URL")
    else:
        return jsonify("ERROR ONLY GET ACCEPTABLE")

@app.route('/url',methods=["POST"])
def url():
    if request.method == "POST":
        url = request.get_data().decode("utf-8")
        a.setter(url)
        return jsonify("POST")
    else:
        return jsonify("ERROR ONLY PUT ACCEPTABLE")

if __name__ == '__main__':
    app.run("127.0.0.1","5034")
