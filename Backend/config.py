from flask import Flask
from flask_sqlalchemy import SQLAlchemy
"""allows cross origin requests which is not allowed by defualt"""
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

"""connect to our database, we will be using a MySQL database"""
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mydatabase2.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

"""create a database instance"""
db = SQLAlchemy(app)

