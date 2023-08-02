from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


# how to use flask migrate?
# 1. flask db init
# 2. flask db migrate
# 3. flask db upgrade


class BarangayOfficial(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)

    photo = db.Column(db.LargeBinary)
    full_name = db.Column(db.String(255))
    barangay_number = db.Column(db.String(255))
    sex = db.Column(db.String(50))
    username = db.Column(db.String(50))
    password = db.Column(db.String(50))

    birthdate = db.Column(db.String(50))
    relocation_year = db.Column(db.String(50))
    address = db.Column(db.String(255))


class Resident(db.Model, UserMixin):
    id = db.Column(db.String(255), primary_key=True)
    photo = db.Column(db.LargeBinary)
    full_name = db.Column(db.String(255))
    barangay_number = db.Column(db.String(255))
    sex = db.Column(db.String(50))
    username = db.Column(db.String(50))
    password = db.Column(db.String(50))
    birthdate = db.Column(db.String(50))
    relocation_year = db.Column(db.String(50))
    address = db.Column(db.String(255))

    # Define a one-to-many relationship with MaligayaCourt_ReservationList
    reservations = db.relationship('MaligayaCourtReservationList', backref='resident', lazy=True)


class MaligayaCourtReservationList(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    full_name = db.Column(db.String(255))
    purpose = db.Column(db.String(255))
    number_of_attendees = db.Column(db.Integer)
    reservation_date = db.Column(db.String(255))
    reservation_time = db.Column(db.String(255))
    resident_id = db.Column(db.String(255), db.ForeignKey('resident.id'), nullable=False)


class CountrysideCourtReservationList(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    full_name = db.Column(db.String(255))
    purpose = db.Column(db.String(255))
    number_of_attendees = db.Column(db.Integer)
    reservation_date = db.Column(db.String(255))
    reservation_time = db.Column(db.String(255))
    resident_id = db.Column(db.String(255), db.ForeignKey('resident.id'), nullable=False)


class TennisCourtReservationList(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    full_name = db.Column(db.String(255))
    purpose = db.Column(db.String(255))
    number_of_attendees = db.Column(db.Integer)
    reservation_date = db.Column(db.String(255))
    reservation_time = db.Column(db.String(255))
    resident_id = db.Column(db.String(255), db.ForeignKey('resident.id'), nullable=False)
