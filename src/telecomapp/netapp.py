import logging
import os
from json import dumps

from flask import Flask

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


if __name__ == "__main__":
    logging.root.setLevel(logging.INFO)
    logging.info("Starting on port %d, database is at %s", port, url)
    app.run(port=port)
