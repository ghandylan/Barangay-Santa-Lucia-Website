from flask import Blueprint, render_template, request
from flask_login import login_required, current_user

from models import Resident, MaligayaCourtReservationList

resident_views_blueprint = Blueprint('resident_views', __name__)


@resident_views_blueprint.route('/resident/home')
@login_required
def resident_home():
    return render_template('resident/home.html')


@resident_views_blueprint.route('/resident/the_barangay')
@login_required
def resident_the_barangay():
    return render_template('resident/the_barangay.html')


@resident_views_blueprint.route('/resident/facilities')
@login_required
def resident_facilities():
    username = current_user.username
    return render_template('resident/facilities.html')


@resident_views_blueprint.route('/resident/facilities/court1')
@login_required
def resident_facilities_court1():
    user_id = current_user.id
    username = current_user.username
    full_name = current_user.full_name
    purpose = request.form.get('purpose')
    number_of_attendees = request.form.get('pax')
    reservation_day = request.form.get('date')
    reservation_time = request.form.get('time')

    if request.method == 'POST':
        maligaya_court_reservation_list = MaligayaCourtReservationList(full_name=full_name,
                                                                       purpose=purpose,
                                                                       number_of_attendees=int(number_of_attendees),
                                                                       reservation_date=reservation_day,
                                                                       reservation_time=reservation_time,
                                                                       resident_id=user_id)

    return render_template('resident/reservation-court1.html', username=username, full_name=full_name)


@resident_views_blueprint.route('/resident/facilities/court2')
@login_required
def resident_facilities_court2():
    username = current_user.username
    return render_template('resident/reservation-court2.html', username=username)


@resident_views_blueprint.route('/resident/facilities/tennis-court')
@login_required
def resident_facilities_tennis_court():
    username = current_user.username
    return render_template('resident/reservation-tenniscourt.html', username=username)


@resident_views_blueprint.route('/resident/services')
@login_required
def resident_services():
    username = current_user.username
    return render_template('resident/itemrenting.html', username=username)


@resident_views_blueprint.route('/resident/profile/<username>')
@login_required
def resident_profile(username):
    resident_full_name = Resident.query.filter_by(username=username).first().full_name
    resident_barangay_number = Resident.query.filter_by(username=username).first().barangay_number
    resident_sex = Resident.query.filter_by(username=username).first().sex
    resident_username = Resident.query.filter_by(username=username).first().username
    resident_birthdate = Resident.query.filter_by(username=username).first().birthdate
    resident_relocation_year = Resident.query.filter_by(username=username).first().relocation_year
    resident_address = Resident.query.filter_by(username=username).first().address

    return render_template('resident/profile.html', resident_full_name=resident_full_name,
                           resident_barangay_number=resident_barangay_number, resident_sex=resident_sex,
                           resident_username=resident_username, resident_birthdate=resident_birthdate,
                           resident_relocation_year=resident_relocation_year, resident_address=resident_address)
