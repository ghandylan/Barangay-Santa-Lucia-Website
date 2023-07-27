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
    # role = db.Column(db.String(50), default='barangay_official')


class Resident(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)
    # role = db.Column(db.String(50), default='resident')
