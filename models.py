from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


# how to use flask migrate?
# 1. flask db init
# 2. flask db migrate
# 3. flask db upgrade

# class Photo(db.Model):
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     file_name = db.Column(db.String(255))
#     data = db.Column(db.LargeBinary)
#     owner_id = db.Column(db.String(255), db.ForeignKey('resident.id'), nullable=False)


class Resident(db.Model, UserMixin):
    id = db.Column(db.String(255), primary_key=True)
    role = db.Column(db.String(255))
    # photo = db.Column(db.Integer, db.ForeignKey('photo.id'))

    full_name = db.Column(db.String(255))
    sex = db.Column(db.String(50))
    username = db.Column(db.String(50))
    password = db.Column(db.LargeBinary)
    birthdate = db.Column(db.String(50))
    relocation_year = db.Column(db.String(50))
    address = db.Column(db.String(255))

    reservations = db.relationship('MaligayaCourtReservationList', backref='resident', lazy=True)
    countryside_reservations = db.relationship('CountrysideCourtReservationList', backref='resident', lazy=True)
    tennis_reservations = db.relationship('TennisCourtReservationList', backref='resident', lazy=True)


class BarangayOfficial(db.Model, UserMixin):
    id = db.Column(db.String(255), primary_key=True)
    role = db.Column(db.String(255))
    # photo = db.Column(db.Integer, db.ForeignKey('photo.id'))

    full_name = db.Column(db.String(255))
    sex = db.Column(db.String(50))
    username = db.Column(db.String(50))
    password = db.Column(db.LargeBinary)
    birthdate = db.Column(db.String(50))
    relocation_year = db.Column(db.String(50))
    address = db.Column(db.String(255))


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


class Items(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    item_name = db.Column(db.String(255))
    item_quantity = db.Column(db.Integer)


class ItemRentals(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    resident_id = db.Column(db.String(255), db.ForeignKey('resident.id'), nullable=False)

    chairs_borrowed = db.Column(db.Integer)
    tables_borrowed = db.Column(db.Integer)
    tents_borrowed = db.Column(db.Integer)

    borrow_date = db.Column(db.String(255))

    resident = db.relationship('Resident', backref='item_rentals', lazy=True)
