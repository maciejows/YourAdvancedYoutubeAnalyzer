import os
from flask import Flask, send_file, jsonify, request
from flask_cors import CORS
from Backend.mozaika import histogram
from Backend.data import Data
from Backend.dbServices import ytDB

app = Flask(__name__)
CORS(app)

@app.route('/hist',methods=["GET"])
def output():
    if request.method == "GET":
        #TODO Check if hist is present in database
        url = request.args.get('url',type=str)
        data = Data('https://www.youtube.com/watch?v=' + url,True)
        if url != '':
            histogram(data)
            name = data.vidID + ".mp4"
            os.remove(name)
            return send_file("hist.png", mimetype='image/png')
        else:
            return jsonify("EMPTY URL")
    else:
        return jsonify("ERROR ONLY GET ACCEPTABLE")

@app.route('/vid',methods=["GET"])
def json():
    if request.method == "GET":
        yt = ytDB()
        url = request.args.get('url', type=str)
        data = Data('https://www.youtube.com/watch?v=' + url,False)
        if url != '':
            yt.addData(data)
            heh = yt.getData(data.vidID)
            yt.closeConnection()
            return jsonify(heh)
        else:
            return jsonify("EMPTY URL")
    else:
        return jsonify("ERROR ONLY GET ACCEPTABLE")


if __name__ == '__main__':
    app.run("127.0.0.1","5034")
