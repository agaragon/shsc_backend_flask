from ..api import api
from flask import Flask
from ..app import app


@app.route("/")
def hello():
    return """Hello World from Flask in a uWSGI Nginx Docker container with \
    Python 3.7 (from the example template),
    try also: <a href="/users/">/users/</a>"""
