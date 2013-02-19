import json

from flask import Flask, request, jsonify
app = Flask(__name__)

from haproxy_manager.manager import Manager
from haproxy_manager.common.config import config


@app.route("/list", defaults={'ftype': None})
@app.route("/list/<ftype>")
def list(ftype):
    manager = Manager(config.get("haproxyfiles", "conf_files"))
    return flask.jsonify(manager.list(ftype))


@app.route("/type/<ftype>/name/<fname>", methods=["GET", "PUT", "DELETE"])
def conf(ftype, fname):
    """
    For PUT opts must be: {"arg1":1, "arg2":2}
    """
    manager = Manager(config.get("haproxyfiles", "conf_files"))
    response = {"message": ""}

    if request.method == 'GET':
        return jsonify(manager.get(ftype, fname))

    elif request.method == 'PUT':
        manager.update(ftype, fname, request.json)
        return jsonify(response)

    elif request.method == 'DELETE':
        return jsonify(manager.delete(ftype, fname))


def run():
    app.run(debug=True)
