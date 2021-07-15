from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:data@34.89.107.2/fundamentalproject'
app.config['SECRET_KEY']=str(os.urandom(16))


db = SQLAlchemy(app)

from application import routes