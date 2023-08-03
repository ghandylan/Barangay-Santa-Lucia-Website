import uuid

from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required

from models import Resident, db, MaligayaCourtReservationList, CountrysideCourtReservationList

brngyofficial_views_blueprint = Blueprint('brngyofficial_views', __name__)


@brngyofficial_views_blueprint.route('/barangay_official/home')
@login_required
def barangay_official_home():
    return render_template('barangayofficial/home.html')


@brngyofficial_views_blueprint.route('/barangay_official/the_barangay')
@login_required
def barangay_official_the_barangay():
    return render_template('barangayofficial/the_barangay.html')


@brngyofficial_views_blueprint.route('/barangay_official/facilities')
@login_required
def barangay_official_facilities():
    return render_template('barangayofficial/facilities.html')


@brngyofficial_views_blueprint.route('/barangay_official/residents')
@login_required
def barangay_official_residents():
    residents = Resident.query.all()
    return render_template('barangayofficial/residents.html', residents=residents)


@brngyofficial_views_blueprint.route('/barangay_official/residents/add', methods=['POST', 'GET'])
@login_required
def barangay_official_add_residents():
    if request.method == 'POST':
        resident_id = str(uuid.uuid4())[:8]

        # profile_picture = request.form.get('profile_picture')
        full_name = request.form.get('fullname')
        barangay_number = uuid.uuid4()
        sex = request.form.get('sex')
        username = request.form.get('username')

        birth_date = request.form.get('birthdate')
        relocation_year = request.form.get('relocationyear')
        address = request.form.get('address')
        new_resident = Resident(id=resident_id, photo=None, full_name=full_name, barangay_number=barangay_number,
                                sex=sex, username=username, password=None, birthdate=birth_date,
                                relocation_year=relocation_year, address=address)

        db.session.add(new_resident)
        db.session.commit()

        return redirect(url_for('brngyofficial_views.barangay_official_residents'))

    return render_template('barangayofficial/adduser.html')


@brngyofficial_views_blueprint.route('/barangay_official/residents/add_password', methods=['POST', 'GET'])
@login_required
def barangay_official_add_residents_password():
    if request.method == 'POST':
        resident_id = request.form.get('resident_id')
        password = request.form.get('password')

        resident = Resident.query.filter_by(id=resident_id).first()
        resident.password = password
        db.session.commit()

        return render_template('barangayofficial/residents.html')

    return render_template('barangayofficial/adduser.html')


@brngyofficial_views_blueprint.route('/barangay_official/residents/edit/<string:barangay_number>',
                                     methods=['POST', 'GET'])
@login_required
def barangay_official_edit_residents(barangay_number):
    # photo = Resident.query.filter_by(barangay_number=barangay_number).first().photo
    username = Resident.query.filter_by(barangay_number=barangay_number).first().username
    resident = Resident.query.filter_by(barangay_number=barangay_number).first()
    sex = Resident.query.filter_by(barangay_number=barangay_number).first().sex
    full_name = Resident.query.filter_by(barangay_number=barangay_number).first().full_name
    birth_date = Resident.query.filter_by(barangay_number=barangay_number).first().birthdate
    relocation_year = Resident.query.filter_by(barangay_number=barangay_number).first().relocation_year
    address = Resident.query.filter_by(barangay_number=barangay_number).first().address
    if request.method == 'POST':
        # new_photo = request.form.get('changeprofileimage')
        new_full_name = request.form.get('fullname')
        new_sex = request.form.get('sex')
        new_username = request.form.get('username')
        new_birth_date = request.form.get('birthdate')
        new_relocation_year = request.form.get('relocationyear')
        new_address = request.form.get('address')

        resident = Resident.query.filter_by(barangay_number=barangay_number).first()

        # resident.photo = new_photo
        resident.full_name = new_full_name
        resident.sex = new_sex
        resident.username = new_username
        resident.birthdate = new_birth_date
        resident.relocation_year = new_relocation_year
        resident.address = new_address

        db.session.add(resident)
        db.session.commit()

        return redirect(url_for('brngyofficial_views.barangay_official_residents'))

    return render_template('barangayofficial/edituser.html', barangay_number=barangay_number, username=username,
                           resident=resident, sex=sex, full_name=full_name, birth_date=birth_date,
                           relocation_year=relocation_year, address=address)


@brngyofficial_views_blueprint.route('/barangay_official/residents/delete/<string:barangay_number>',
                                     methods=['POST', 'GET'])
@login_required
def barangay_official_delete_resident(barangay_number):
    if request.method == 'POST':
        resident = Resident.query.filter_by(barangay_number=barangay_number).first()
        db.session.delete(resident)
        db.session.commit()

    return redirect(url_for('brngyofficial_views.barangay_official_residents'))


@brngyofficial_views_blueprint.route('/barangay_official/residents/search', methods=['POST', 'GET'])
@login_required
def barangay_official_search_residents():
    if request.method == 'POST':
        search = request.form.get('search')
        residents = Resident.query.filter(Resident.full_name.contains(search)).all()
        return render_template('barangayofficial/residents.html', residents=residents)
    return render_template('barangayofficial/residents.html')


@brngyofficial_views_blueprint.route('/barangay_official/services')
@login_required
def barangay_official_item_tracking():
    return render_template('barangayofficial/itemrenting-admin.html')


@brngyofficial_views_blueprint.route('/barangay_official/services/maligaya-court-reservations')
@login_required
def barangay_official_maligaya_court_reservations():
    tuesday = MaligayaCourtReservationList.query.filter_by(reservation_date='Tuesday').all()
    wednesday = MaligayaCourtReservationList.query.filter_by(reservation_date='Wednesday').all()
    thursday = MaligayaCourtReservationList.query.filter_by(reservation_date='Thursday').all()
    friday = MaligayaCourtReservationList.query.filter_by(reservation_date='Friday').all()
    saturday = MaligayaCourtReservationList.query.filter_by(reservation_date='Saturday').all()
    sunday = MaligayaCourtReservationList.query.filter_by(reservation_date='Sunday').all()

    return render_template('barangayofficial/reservation-admin-court1.html', tuesday=tuesday, wednesday=wednesday,
                           thursday=thursday, friday=friday, saturday=saturday, sunday=sunday)


@brngyofficial_views_blueprint.route('/barangay_official/services/countryside-court-reservations')
@login_required
def barangay_official_countryside_court_reservations():
    tuesday = CountrysideCourtReservationList.query.filter_by(reservation_date='Tuesday').all()
    wednesday = CountrysideCourtReservationList.query.filter_by(reservation_date='Wednesday').all()
    thursday = CountrysideCourtReservationList.query.filter_by(reservation_date='Thursday').all()
    friday = CountrysideCourtReservationList.query.filter_by(reservation_date='Friday').all()
    saturday = CountrysideCourtReservationList.query.filter_by(reservation_date='Saturday').all()
    sunday = CountrysideCourtReservationList.query.filter_by(reservation_date='Sunday').all()

    return render_template('barangayofficial/reservation-admin-court2.html', tuesday=tuesday, wednesday=wednesday,
                           thursday=thursday, friday=friday, saturday=saturday, sunday=sunday)


@brngyofficial_views_blueprint.route('/barangay_official/services/tennis-court-reservations')
@login_required
def barangay_official_tennis_court_reservations():
    tuesday = CountrysideCourtReservationList.query.filter_by(reservation_date='Tuesday').all()
    wednesday = CountrysideCourtReservationList.query.filter_by(reservation_date='Wednesday').all()
    thursday = CountrysideCourtReservationList.query.filter_by(reservation_date='Thursday').all()
    friday = CountrysideCourtReservationList.query.filter_by(reservation_date='Friday').all()
    saturday = CountrysideCourtReservationList.query.filter_by(reservation_date='Saturday').all()
    sunday = CountrysideCourtReservationList.query.filter_by(reservation_date='Sunday').all()

    return render_template('barangayofficial/reservation-admin-tenniscourt.html', tuesday=tuesday, wednesday=wednesday,
                           thursday=thursday, friday=friday, saturday=saturday, sunday=sunday)


@brngyofficial_views_blueprint.route('/barangay_official/profile/<username>')
@login_required
def barangay_official_profile(username):
    return render_template('barangayofficial/profile.html', username=username)
