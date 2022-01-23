# tuto flask : https://www.digitalocean.com/community/tutorials/processing-incoming-request-data-in-flask-fr
import json
import logging
import os


from flask import Flask, Response, request, render_template, jsonify

from src.telecomapp import net
from src.telecomapp.model import Model
from src.telecomapp.netServices import NetServices

app = Flask(__name__, static_url_path="/static/")

url = os.getenv("NEO4J_URI", "bolt://localhost:7687")

port = os.getenv("PORT", 8080)

model = Model("azeaze")  # think if its a global var or not

netServices = NetServices(model)  # think if its a global var or not

arr = net.csv_to_arr('H:/workspace/python/telecom-project/data/BD Routage 30 10 2021.csv')
my_net = net.Net(arr)
my_net.gen_json(my_net.get_nodes()['AGA001'])
msg = my_net.str_tree
msg2="'"+msg+"'"
@app.route("/")
def get_index():
    return app.send_static_file("testfetch.html")


@app.route('/region')
def region():
    # if key doesn't exist, returns None
    region = request.args.get('region')
    n_region = model.get_net_node("AGA001")
    results = netServices.get_subtree(n_region,{},0,1)
    res = netServices.get_subtree_city("FO", region, 0, 12)
    j_res  = json.dumps(res)
    j_results = json.dumps(results)
    user = {'id': "Mr.", 'lastname': "My Father's Son"}

    return Response(j_res,mimetype="application/json")

if __name__ == "__main__":
    logging.root.setLevel(logging.INFO)
    logging.info("Starting on port %d, database is at %s", port, url)
    app.run(port=port,debug=True)
