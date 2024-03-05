from flask import Flask
from flask_sqlalchemy import SQLAlchemy
"""allows cross origin requests which is not allowed by defualt"""
from flask_cors import CORS
from dotenv import load_dotenv, dotenv_values
import os
load_dotenv()


app = Flask(__name__)
CORS(app)
db_name = 'my_contacts'
db_host = '127.0.0.1'
db_username = os.getenv('DB_USERNAME')

db_password = os.getenv('DB_PASSWORD')

"""connect to our database, we will be using a MySQL database"""

app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql://{db_username}:{db_password}@{db_host}/{db_name}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

"""create a database instance"""
db = SQLAlchemy(app)

