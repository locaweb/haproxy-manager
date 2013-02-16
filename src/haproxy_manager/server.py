import json

from flask import Flask, request
app = Flask(__name__)

from haproxy_manager.manager import Manager


@app.route("/list/<type>")
def list(ftype): manager = Manager("tests/output/")
    return json.dumps(manager.list(ftype))


@app.route("/type/<ftype>/name/<fname>", methods=["GET", "PUT", "DELETE"])
def conf(ftype, fname):
    """
    For PUT opts must be: {"arg1":1, "arg2":2}
    """
    manager = Manager("tests/output/")

    if request.method == 'GET':
        return json.dumps(manager.get(ftype, fname))

    elif request.method == 'PUT':
        return json.dumps(manager.update(ftype, fname, request.form))

    elif request.method == 'DELETE':
        return json.dumps(manager.delete(ftype, fname))


def run():
    app.run(debug=True)
