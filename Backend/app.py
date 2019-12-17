import os
import time

from flask import Flask, send_file, jsonify, request
from flask_cors import CORS
from Backend.mozaika import histogram
from Backend.data import Data
from Backend.dbServices import ytDB
from Backend.comments import Com

app = Flask(__name__)
CORS(app)

@app.route('/hist',methods=["GET"])
def output():
    if request.method == "GET":
        #TODO Check if hist is present in database
        url = request.args.get('url',type=str)
        data = Data('https://www.youtube.com/watch?v=' + url,True)
        if url != '':
            link = histogram(data)
            os.remove(data.vidID + ".mp4")
            os.remove(data.vidID + ".png")
            return jsonify(link)
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

@app.route('/com',methods=["GET"])
def jsonc():
    if request.method == "GET":
        url = request.args.get('url', type=str)
        start = time.time()
        com = Com(url)
        com.down()
        end = time.time()
        print(end - start)
        return jsonify(len(com.komentarze))

if __name__ == '__main__':
    app.run("127.0.0.1","5034")
