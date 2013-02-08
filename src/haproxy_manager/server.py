from flask import Flask
app = Flask(__name__)


@app.route("/")
def info():
    return "Haproxy manager working"


def run():
    app.run()
