# tuto flask : https://www.digitalocean.com/community/tutorials/processing-incoming-request-data-in-flask-fr
import json
import logging
import os
from json import dumps

from flask import Flask, Response, request

from src.telecomapp.model import Model
from src.telecomapp.netServices import NetServices

app = Flask(__name__, static_url_path="/static/")

url = os.getenv("NEO4J_URI", "bolt://localhost:7687")

port = os.getenv("PORT", 8080)

model = Model("azeaze")  # think if its a global var or not

netServices = NetServices(model)  # think if its a global var or not


@app.route("/")
def get_index():
    return app.send_static_file("index.html")


@app.route('/region')
def region():
    # if key doesn't exist, returns None
    region = request.args.get('region')
    n_region = model.get_net_node(region)
    results = netServices.get_subtree(n_region,{},0,10)
    j_results = json.dumps(results)
    return j_results

if __name__ == "__main__":
    logging.root.setLevel(logging.INFO)
    logging.info("Starting on port %d, database is at %s", port, url)
    app.run(port=port)