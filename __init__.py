from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

db = SQLAlchemy(app)

app.config['SQL ALCHEMY_DATABSE_UI'] = 'sqlite///'

from application import routes
