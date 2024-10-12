#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route("/")
def Home():
    return "<h1>Home Page</h1>"

@app.route("/<urs>")
def User(urs):
    return f"<h1>Hello {urs}</h1>"

if __name__ == '__main__':
    app.run(port=5555, debug=True)
