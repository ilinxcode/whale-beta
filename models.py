from flask_login import UserMixin
from server import db

class User(UserMixin, db.Model):
  id = db.Column(db.Integer, primary_key=True)
  email = db.Column(db.String(100), unique=True)
  password = db.Column(db.String(100))
  name = db.Column(db.String(200), unique=True)
  confirmed = db.Column(db.String(10))
  