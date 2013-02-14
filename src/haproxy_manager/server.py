import json

from flask import Flask, request
app = Flask(__name__)

from haproxy_manager.manager import Manager


@app.route("/")
def info():
    return "Haproxy manager working"


@app.route("/list")
def list():
    manager = Manager("tests/output/")
    return json.dumps(manager.list())


@app.route("/<name>", methods=["GET", "PUT", "DELETE"])
def conf(name):
    manager = Manager("tests/output/")

    if request.method == 'GET':
        return json.dumps(manager.get(name))

    elif request.method == 'PUT':
        return json.dumps(manager.update(name))

    elif request.method == 'DELETE':
        return json.dumps(manager.delete(name))


def run():
    app.run(debug=True)
