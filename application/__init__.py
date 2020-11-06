from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import getenv
app = Flask(__name__)

db = SQLAlchemy(app)

app.config['SQLALCHEMY_DATABASE_URI'] = GENTENV('DB_URI')
app.config['SECRET_KEY'] = getenv('SECRET_KEY')



from application import routes




