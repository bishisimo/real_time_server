import json
import os

import flask
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources=r'/*', supports_credentials=True)


@app.route('/point_cluster/<vin>')
def get_map(vin):
    return flask.render_template("point_cluster.html", vin=vin)


@app.route('/api/point_cluster/all')
def point_cluster_all():
    res_dir = './static/stop_gps'
    result = []
    for file_name in os.listdir(res_dir):
        res_path = os.path.join(res_dir, file_name)
        with open(res_path)as file:
            data = json.load(file)
            result += data
    return flask.jsonify(result)


@app.route('/api/point_cluster/<vin>')
def point_cluster(vin):
    res_dir = './static/stop_gps'
    res_path = os.path.join(res_dir, f'{vin}.json')
    with open(res_path)as file:
        data = json.load(file)
    return flask.jsonify(data)


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=2021,
        debug=False
    )
