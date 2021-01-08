from flask import Flask
from flask_restful import Api
from os.path import join, dirname, abspath
from os import environ
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object("app.config.Config")
api = Api(app)
basedir = abspath(dirname(__file__))

# app.config['SQLALCHEMY_DATABASE_URI'] = environ['DATABASE_URL']
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
