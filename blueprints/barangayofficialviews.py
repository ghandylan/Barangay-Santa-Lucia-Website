import uuid

import bcrypt
from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user

from models import Resident, db, MaligayaCourtReservationList, CountrysideCourtReservationList, Items, ItemRentals, \
    BarangayOfficial
from rbac import barangay_official_required

brngyofficial_views_blueprint = Blueprint('brngyofficial_views', __name__)


@brngyofficial_views_blueprint.route('/barangay_official/home')
@login_required
@barangay_official_required('barangay_official')
def barangay_official_home():
    return render_template('barangayofficial/home.html')


@brngyofficial_views_blueprint.route('/barangay_official/the_barangay')
@login_required
@barangay_official_required('barangay_official')
def barangay_official_the_barangay():
    return render_template('barangayofficial/the_barangay.html')


@brngyofficial_views_blueprint.route('/barangay_official/residents')
@login_required
@barangay_official_required('barangay_official')
def barangay_official_residents():
    residents = Resident.query.all()
    return render_template('barangayofficial/residents.html', residents=residents)


@brngyofficial_views_blueprint.route('/barangay_official/residents/add', methods=['POST', 'GET'])
@login_required
@barangay_official_required('barangay_official')
def barangay_official_add_residents():
    if request.method == 'POST':
        resident_id = uuid.uuid4()

        full_name = request.form.get('fullname')
        sex = request.form.get('sex')
        username = request.form.get('username')

        birth_date = request.form.get('birthdate')
        relocation_year = request.form.get('relocationyear')
        address = request.form.get('address')

        new_resident = Resident(id=resident_id, role="resident", full_name=full_name, sex=sex, username=username,
                                password=None, birthdate=birth_date, relocation_year=relocation_year, address=address)

        db.session.add(new_resident)
        db.session.commit()

        # upload picture
        # profile_picture = request.files['changeprofileimage']
        # upload = Photo(file_name=profile_picture.filename, data=profile_picture.read(), owner_id=resident_id)
        #
        # db.session.add(upload)
        # db.session.commit()

        return redirect(url_for('brngyofficial_views.barangay_official_residents'))

    return render_template('barangayofficial/adduser.html')


@brngyofficial_views_blueprint.route('/barangay_official/residents/add_password', methods=['POST', 'GET'])
@login_required
@barangay_official_required('barangay_official')
def barangay_official_add_residents_password():
    if request.method == 'POST':
        resident_id = request.form.get('resident_id')
        password = request.form.get('password')

        resident = Resident.query.filter_by(id=resident_id).first()
        resident.password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        db.session.commit()

        return render_template('barangayofficial/residents.html')

    return render_template('barangayofficial/adduser.html')


@brngyofficial_views_blueprint.route('/barangay_official/residents/edit/<string:id>', methods=['POST', 'GET'])
@login_required
@barangay_official_required('barangay_official')
def barangay_official_edit_residents(id):
    # photo = Photo.query.filter_by(owner_id=id).first()
    username = Resident.query.filter_by(id=id).first().username
    resident = Resident.query.filter_by(id=id).first()
    sex = Resident.query.filter_by(id=id).first().sex
    full_name = Resident.query.filter_by(id=id).first().full_name
    birth_date = Resident.query.filter_by(id=id).first().birthdate
    relocation_year = Resident.query.filter_by(id=id).first().relocation_year
    address = Resident.query.filter_by(id=id).first().address
    if request.method == 'POST':
        # new_photo = request.form.get('changeprofileimage')
        new_full_name = request.form.get('fullname')
        new_sex = request.form.get('sex')
        new_username = request.form.get('username')
        new_birth_date = request.form.get('birthdate')
        new_relocation_year = request.form.get('relocationyear')
        new_address = request.form.get('address')

        resident = Resident.query.filter_by(id=id).first()

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

    return render_template('barangayofficial/edituser.html', id=id, username=username, resident=resident,
                           sex=sex,
                           full_name=full_name, birth_date=birth_date, relocation_year=relocation_year, address=address)


@brngyofficial_views_blueprint.route('/barangay_official/residents/edit/<string:id>/delete', methods=['POST', 'GET'])
@login_required
@barangay_official_required('barangay_official')
def barangay_official_delete_resident(id):
    if request.method == 'POST':
        resident = Resident.query.filter_by(id=id).first()
        db.session.delete(resident)
        db.session.commit()

    return redirect(url_for('brngyofficial_views.barangay_official_residents'))


@brngyofficial_views_blueprint.route('/barangay_official/residents/search', methods=['POST', 'GET'])
@login_required
@barangay_official_required('barangay_official')
def barangay_official_search_residents():
    if request.method == 'POST':
        search = request.form.get('search')
        residents = Resident.query.filter(Resident.full_name.contains(search)).all()
        return render_template('barangayofficial/residents.html', residents=residents)
    return render_template('barangayofficial/residents.html')


@brngyofficial_views_blueprint.route('/barangay_official/services/item-renting-tracker')
@login_required
@barangay_official_required('barangay_official')
def barangay_official_item_tracking():
    chairs = Items.query.filter_by(item_name='Chairs').first().item_quantity
    tables = Items.query.filter_by(item_name='Tables').first().item_quantity
    tents = Items.query.filter_by(item_name='Tents').first().item_quantity

    item_rentals = ItemRentals.query.all()

    return render_template('barangayofficial/itemrenting-admin.html', chairs=chairs, tables=tables, tents=tents,
                           item_rentals=item_rentals)


@brngyofficial_views_blueprint.route('/barangay_official/services/maligaya-court-reservations')
@login_required
@barangay_official_required('barangay_official')
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
@barangay_official_required('barangay_official')
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
@barangay_official_required('barangay_official')
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
@barangay_official_required('barangay_official')
def barangay_official_profile(username):
    username = current_user.username
    full_name = BarangayOfficial.query.filter_by(username=username).first().full_name
    barangay_number = BarangayOfficial.query.filter_by(username=username).first().id
    sex = BarangayOfficial.query.filter_by(username=username).first().sex
    birth_date = BarangayOfficial.query.filter_by(username=username).first().birthdate
    relocation_year = BarangayOfficial.query.filter_by(username=username).first().relocation_year
    address = BarangayOfficial.query.filter_by(username=username).first().address

    return render_template('barangayofficial/profile.html', username=username, full_name=full_name,
                           barangay_number=barangay_number, sex=sex, birth_date=birth_date,
                           relocation_year=relocation_year, address=address)


@brngyofficial_views_blueprint.route('/barangay_official/profile/change-password', methods=['POST', 'GET'])
@login_required
@barangay_official_required('barangay_official')
def barangay_official_change_password():
    id = current_user.id

    current_password = request.form.get('current_password')
    new_password = request.form.get('new_password')
    confirm_password = request.form.get('confirm_password')

    if request.method == 'POST':
        if current_password != current_user.password:
            flash('Incorrect Password', 'danger')
            return redirect(url_for('brngyofficial_views.barangay_official_change_password'))
        elif new_password != confirm_password:
            flash('Passwords do not match', 'danger')
            return redirect(url_for('brngyofficial_views.barangay_official_change_password'))
        else:
            # update password
            BarangayOfficial.query.filter_by(id=id).update(dict(password=new_password))
            db.session.commit()
            flash('Password Updated', 'success')
            return redirect(url_for('brngyofficial_views.barangay_official_profile', username=current_user.username))

    return render_template('barangayofficial/changepassword.html')


@brngyofficial_views_blueprint.route('/barangay_official/residents/edit/<string:id>/changepw', methods=['POST', 'GET'])
@login_required
@barangay_official_required('barangay_official')
def barangay_official_change_password_resident(id):
    new_password = request.form.get('new_password')
    confirm_password = request.form.get('confirm_password')
    if request.method == 'POST':
        if new_password != confirm_password:
            flash('Passwords do not match', 'danger')
            return redirect(url_for('brngyofficial_views.barangay_official_change_password_resident', id=id))
        else:
            # update password
            Resident.query.filter_by(id=id).update(dict(password=new_password))
            db.session.commit()
            flash('Password Updated', 'success')
            return redirect(url_for('brngyofficial_views.barangay_official_residents'))
    return render_template('barangayofficial/changepassword-resident.html', id=id)
