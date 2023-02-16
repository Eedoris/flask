from msilib import init_database
from flask import Flask
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///db1.db'

db= SQLAlchemy(app)

class User(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100),unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))

db.create_all()


if __name__ == "__main__":
    app.run(debug=True)




 