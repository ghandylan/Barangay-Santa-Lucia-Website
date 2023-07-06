from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from app import db
from sqlalchemy import ForeignKey, Integer, String, Boolean
from sqlalchemy.orm import relationship


class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)


class BarangayOfficial(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    fullname = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)
