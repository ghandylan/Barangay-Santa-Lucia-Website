from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


# how to use flask migrate?
# 1. flask db init
# 2. flask db migrate
# 3. flask db upgrade


class BarangayOfficial(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)


class Resident(db.Model, UserMixin):
    id = db.Column(db.String(255), primary_key=True)

    photo = db.Column(db.BLOB)
    full_name = db.Column(db.String(255))
    barangay_number = db.Column(db.String(255))
    sex = db.Column(db.String(50))
    username = db.Column(db.String(50))
    password = db.Column(db.String(50))

    birthdate = db.Column(db.String(50))
    relocation_year = db.Column(db.String(50))
    address = db.Column(db.String(255))
