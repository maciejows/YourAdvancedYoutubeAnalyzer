import os
from flask import Flask, send_file, jsonify, request
from YourAdvancedYoutubeAnalyzer.Backend.mozaika import histogram
from YourAdvancedYoutubeAnalyzer.Backend.data import Data

app = Flask(__name__)

@app.route('/hist',methods=["GET"])
def output():
    if request.method == "GET":
        url = request.args.get('url',type=str)
        data = Data(url,True)
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
        url = request.args.get('url', type=str)
        data = Data(url,False)
        if url != '':
            heh = data.getContent()
            return jsonify(heh)
        else:
            return jsonify("EMPTY URL")
    else:
        return jsonify("ERROR ONLY GET ACCEPTABLE")


if __name__ == '__main__':
    app.run("127.0.0.1","5034")