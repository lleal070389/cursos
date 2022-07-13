# -*- coding: utf-8 -*-

from flask import Flask


app = Flask(__name__)

if __name__ == "__main__":
    app.config["ENV"] = "development"
    app.run(port=8000, debug=True)