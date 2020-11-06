from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

db = SQLAlchemy(app)

app.config['SQL ALCHEMY_DATABSE_UI'] = 'mysql+pymysql://root:root@35.246.12.217/Todo '

from application import routes
