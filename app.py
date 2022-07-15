# -*- coding: utf-8 -*-

from flask import Flask, render_template


app = Flask(__name__)


@app.get('/')
def index():
    return render_template("index_t1.html")


if __name__ == "__main__":
    app.run(port=8000, debug=True)