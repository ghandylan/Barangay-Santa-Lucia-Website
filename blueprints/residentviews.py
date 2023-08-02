from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from check_reservation import check_reservation_maligaya

from models import Resident, MaligayaCourtReservationList, CountrysideCourtReservationList, db

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


@resident_views_blueprint.route('/resident/facilities/court1', methods=['GET', 'POST'])
@login_required
def resident_facilities_court1():
    user_id = current_user.id
    username = current_user.username
    full_name = current_user.full_name
    purpose = request.form.get('purpose')
    number_of_attendees = request.form.get('pax')
    reservation_day = request.form.get('date')
    reservation_time = request.form.get('time')
    tuesday_7am = check_reservation_maligaya('Tuesday', '7amslot')
    tuesday_8am = check_reservation_maligaya('Tuesday', '8amslot')
    tuesday_9am = check_reservation_maligaya('Tuesday', '9amslot')
    tuesday_10am = check_reservation_maligaya('Tuesday', '10amslot')
    tuesday_11am = check_reservation_maligaya('Tuesday', '11amslot')
    tuesday_12pm = check_reservation_maligaya('Tuesday', '12pmslot')
    tuesday_1pm = check_reservation_maligaya('Tuesday', '1pmslot')
    tuesday_2pm = check_reservation_maligaya('Tuesday', '2pmslot')
    tuesday_3pm = check_reservation_maligaya('Tuesday', '3pmslot')
    tuesday_4pm = check_reservation_maligaya('Tuesday', '4pmslot')
    tuesday_5pm = check_reservation_maligaya('Tuesday', '5pmslot')
    tuesday_6pm = check_reservation_maligaya('Tuesday', '6pmslot')

    wednesday_7am = check_reservation_maligaya('Wednesday', '7amslot')
    wednesday_8am = check_reservation_maligaya('Wednesday', '8amslot')
    wednesday_9am = check_reservation_maligaya('Wednesday', '9amslot')
    wednesday_10am = check_reservation_maligaya('Wednesday', '10amslot')
    wednesday_11am = check_reservation_maligaya('Wednesday', '11amslot')
    wednesday_12pm = check_reservation_maligaya('Wednesday', '12pmslot')
    wednesday_1pm = check_reservation_maligaya('Wednesday', '1pmslot')
    wednesday_2pm = check_reservation_maligaya('Wednesday', '2pmslot')
    wednesday_3pm = check_reservation_maligaya('Wednesday', '3pmslot')
    wednesday_4pm = check_reservation_maligaya('Wednesday', '4pmslot')
    wednesday_5pm = check_reservation_maligaya('Wednesday', '5pmslot')
    wednesday_6pm = check_reservation_maligaya('Wednesday', '6pmslot')

    thursday_7am = check_reservation_maligaya('Thursday', '7amslot')
    thursday_8am = check_reservation_maligaya('Thursday', '8amslot')
    thursday_9am = check_reservation_maligaya('Thursday', '9amslot')
    thursday_10am = check_reservation_maligaya('Thursday', '10amslot')
    thursday_11am = check_reservation_maligaya('Thursday', '11amslot')
    thursday_12pm = check_reservation_maligaya('Thursday', '12pmslot')
    thursday_1pm = check_reservation_maligaya('Thursday', '1pmslot')
    thursday_2pm = check_reservation_maligaya('Thursday', '2pmslot')
    thursday_3pm = check_reservation_maligaya('Thursday', '3pmslot')
    thursday_4pm = check_reservation_maligaya('Thursday', '4pmslot')
    thursday_5pm = check_reservation_maligaya('Thursday', '5pmslot')
    thursday_6pm = check_reservation_maligaya('Thursday', '6pmslot')

    friday_7am = check_reservation_maligaya('Friday', '7amslot')
    friday_8am = check_reservation_maligaya('Friday', '8amslot')
    friday_9am = check_reservation_maligaya('Friday', '9amslot')
    friday_10am = check_reservation_maligaya('Friday', '10amslot')
    friday_11am = check_reservation_maligaya('Friday', '11amslot')
    friday_12pm = check_reservation_maligaya('Friday', '12pmslot')
    friday_1pm = check_reservation_maligaya('Friday', '1pmslot')
    friday_2pm = check_reservation_maligaya('Friday', '2pmslot')
    friday_3pm = check_reservation_maligaya('Friday', '3pmslot')
    friday_4pm = check_reservation_maligaya('Friday', '4pmslot')
    friday_5pm = check_reservation_maligaya('Friday', '5pmslot')
    friday_6pm = check_reservation_maligaya('Friday', '6pmslot')

    saturday_7am = check_reservation_maligaya('Saturday', '7amslot')
    saturday_8am = check_reservation_maligaya('Saturday', '8amslot')
    saturday_9am = check_reservation_maligaya('Saturday', '9amslot')
    saturday_10am = check_reservation_maligaya('Saturday', '10amslot')
    saturday_11am = check_reservation_maligaya('Saturday', '11amslot')
    saturday_12pm = check_reservation_maligaya('Saturday', '12pmslot')
    saturday_1pm = check_reservation_maligaya('Saturday', '1pmslot')
    saturday_2pm = check_reservation_maligaya('Saturday', '2pmslot')
    saturday_3pm = check_reservation_maligaya('Saturday', '3pmslot')
    saturday_4pm = check_reservation_maligaya('Saturday', '4pmslot')
    saturday_5pm = check_reservation_maligaya('Saturday', '5pmslot')
    saturday_6pm = check_reservation_maligaya('Saturday', '6pmslot')

    sunday_7am = check_reservation_maligaya('Sunday', '7amslot')
    sunday_8am = check_reservation_maligaya('Sunday', '8amslot')
    sunday_9am = check_reservation_maligaya('Sunday', '9amslot')
    sunday_10am = check_reservation_maligaya('Sunday', '10amslot')
    sunday_11am = check_reservation_maligaya('Sunday', '11amslot')
    sunday_12pm = check_reservation_maligaya('Sunday', '12pmslot')
    sunday_1pm = check_reservation_maligaya('Sunday', '1pmslot')
    sunday_2pm = check_reservation_maligaya('Sunday', '2pmslot')
    sunday_3pm = check_reservation_maligaya('Sunday', '3pmslot')
    sunday_4pm = check_reservation_maligaya('Sunday', '4pmslot')
    sunday_5pm = check_reservation_maligaya('Sunday', '5pmslot')
    sunday_6pm = check_reservation_maligaya('Sunday', '6pmslot')

    if request.method == 'POST':
        maligaya_court_reservation_list = MaligayaCourtReservationList(full_name=full_name, purpose=purpose,
                                                                       number_of_attendees=int(number_of_attendees),
                                                                       reservation_date=reservation_day,
                                                                       reservation_time=reservation_time,
                                                                       resident_id=user_id)
        db.session.add(maligaya_court_reservation_list)
        db.session.commit()

        return render_template('resident/reservation-court1.html', username=username, full_name=full_name,
                               tuesday_7am=tuesday_7am, tuesday_8am=tuesday_8am, tuesday_9am=tuesday_9am,
                               tuesday_10am=tuesday_10am, tuesday_11am=tuesday_11am, tuesday_12pm=tuesday_12pm,
                               tuesday_1pm=tuesday_1pm, tuesday_2pm=tuesday_2pm, tuesday_3pm=tuesday_3pm,
                               tuesday_4pm=tuesday_4pm, tuesday_5pm=tuesday_5pm, tuesday_6pm=tuesday_6pm,

                               wednesday_7am=wednesday_7am, wednesday_8am=wednesday_8am, wednesday_9am=wednesday_9am,
                               wednesday_10am=wednesday_10am, wednesday_11am=wednesday_11am,
                               wednesday_12pm=wednesday_12pm, wednesday_1pm=wednesday_1pm, wednesday_2pm=wednesday_2pm,
                               wednesday_3pm=wednesday_3pm, wednesday_4pm=wednesday_4pm, wednesday_5pm=wednesday_5pm,
                               wednesday_6pm=wednesday_6pm,

                               thursday_7am=thursday_7am, thursday_8am=thursday_8am, thursday_9am=thursday_9am,
                               thursday_10am=thursday_10am, thursday_11am=thursday_11am, thursday_12pm=thursday_12pm,
                               thursday_1pm=thursday_1pm, thursday_2pm=thursday_2pm, thursday_3pm=thursday_3pm,
                               thursday_4pm=thursday_4pm, thursday_5pm=thursday_5pm, thursday_6pm=thursday_6pm,

                               friday_7am=friday_7am, friday_8am=friday_8am, friday_9am=friday_9am,
                               friday_10am=friday_10am, friday_11am=friday_11am, friday_12pm=friday_12pm,
                               friday_1pm=friday_1pm, friday_2pm=friday_2pm, friday_3pm=friday_3pm,
                               friday_4pm=friday_4pm, friday_5pm=friday_5pm, friday_6pm=friday_6pm,

                               saturday_7am=saturday_7am, saturday_8am=saturday_8am, saturday_9am=saturday_9am,
                               saturday_10am=saturday_10am, saturday_11am=saturday_11am, saturday_12pm=saturday_12pm,
                               saturday_1pm=saturday_1pm, saturday_2pm=saturday_2pm, saturday_3pm=saturday_3pm,
                               saturday_4pm=saturday_4pm, saturday_5pm=saturday_5pm, saturday_6pm=saturday_6pm,

                               sunday_7am=sunday_7am, sunday_8am=sunday_8am, sunday_9am=sunday_9am,
                               sunday_10am=sunday_10am, sunday_11am=sunday_11am, sunday_12pm=sunday_12pm,
                               sunday_1pm=sunday_1pm, sunday_2pm=sunday_2pm, sunday_3pm=sunday_3pm,
                               sunday_4pm=sunday_4pm, sunday_5pm=sunday_5pm, sunday_6pm=sunday_6pm)

    return render_template('resident/reservation-court1.html', username=username, full_name=full_name,
                           tuesday_7am=tuesday_7am, tuesday_8am=tuesday_8am, tuesday_9am=tuesday_9am,
                           tuesday_10am=tuesday_10am, tuesday_11am=tuesday_11am, tuesday_12pm=tuesday_12pm,
                           tuesday_1pm=tuesday_1pm, tuesday_2pm=tuesday_2pm, tuesday_3pm=tuesday_3pm,
                           tuesday_4pm=tuesday_4pm, tuesday_5pm=tuesday_5pm, tuesday_6pm=tuesday_6pm,

                           wednesday_7am=wednesday_7am, wednesday_8am=wednesday_8am, wednesday_9am=wednesday_9am,
                           wednesday_10am=wednesday_10am, wednesday_11am=wednesday_11am, wednesday_12pm=wednesday_12pm,
                           wednesday_1pm=wednesday_1pm, wednesday_2pm=wednesday_2pm, wednesday_3pm=wednesday_3pm,
                           wednesday_4pm=wednesday_4pm, wednesday_5pm=wednesday_5pm, wednesday_6pm=wednesday_6pm,

                           thursday_7am=thursday_7am, thursday_8am=thursday_8am, thursday_9am=thursday_9am,
                           thursday_10am=thursday_10am, thursday_11am=thursday_11am, thursday_12pm=thursday_12pm,
                           thursday_1pm=thursday_1pm, thursday_2pm=thursday_2pm, thursday_3pm=thursday_3pm,
                           thursday_4pm=thursday_4pm, thursday_5pm=thursday_5pm, thursday_6pm=thursday_6pm,

                           friday_7am=friday_7am, friday_8am=friday_8am, friday_9am=friday_9am, friday_10am=friday_10am,
                           friday_11am=friday_11am, friday_12pm=friday_12pm, friday_1pm=friday_1pm,
                           friday_2pm=friday_2pm, friday_3pm=friday_3pm, friday_4pm=friday_4pm, friday_5pm=friday_5pm,
                           friday_6pm=friday_6pm,

                           saturday_7am=saturday_7am, saturday_8am=saturday_8am, saturday_9am=saturday_9am,
                           saturday_10am=saturday_10am, saturday_11am=saturday_11am, saturday_12pm=saturday_12pm,
                           saturday_1pm=saturday_1pm, saturday_2pm=saturday_2pm, saturday_3pm=saturday_3pm,
                           saturday_4pm=saturday_4pm, saturday_5pm=saturday_5pm, saturday_6pm=saturday_6pm,

                           sunday_7am=sunday_7am, sunday_8am=sunday_8am, sunday_9am=sunday_9am, sunday_10am=sunday_10am,
                           sunday_11am=sunday_11am, sunday_12pm=sunday_12pm, sunday_1pm=sunday_1pm,
                           sunday_2pm=sunday_2pm, sunday_3pm=sunday_3pm, sunday_4pm=sunday_4pm, sunday_5pm=sunday_5pm,
                           sunday_6pm=sunday_6pm)


@resident_views_blueprint.route('/resident/facilities/court2')
@login_required
def resident_facilities_court2():
    user_id = current_user.id
    username = current_user.username
    full_name = current_user.full_name
    purpose = request.form.get('purpose')
    number_of_attendees = request.form.get('pax')
    reservation_day = request.form.get('date')
    reservation_time = request.form.get('time')

    tuesday_7am = check_reservation_maligaya('Tuesday', '7amslot')
    tuesday_8am = check_reservation_maligaya('Tuesday', '8amslot')
    tuesday_9am = check_reservation_maligaya('Tuesday', '9amslot')
    tuesday_10am = check_reservation_maligaya('Tuesday', '10amslot')
    tuesday_11am = check_reservation_maligaya('Tuesday', '11amslot')
    tuesday_12pm = check_reservation_maligaya('Tuesday', '12pmslot')
    tuesday_1pm = check_reservation_maligaya('Tuesday', '1pmslot')
    tuesday_2pm = check_reservation_maligaya('Tuesday', '2pmslot')
    tuesday_3pm = check_reservation_maligaya('Tuesday', '3pmslot')
    tuesday_4pm = check_reservation_maligaya('Tuesday', '4pmslot')
    tuesday_5pm = check_reservation_maligaya('Tuesday', '5pmslot')
    tuesday_6pm = check_reservation_maligaya('Tuesday', '6pmslot')

    wednesday_7am = check_reservation_maligaya('Wednesday', '7amslot')
    wednesday_8am = check_reservation_maligaya('Wednesday', '8amslot')
    wednesday_9am = check_reservation_maligaya('Wednesday', '9amslot')
    wednesday_10am = check_reservation_maligaya('Wednesday', '10amslot')
    wednesday_11am = check_reservation_maligaya('Wednesday', '11amslot')
    wednesday_12pm = check_reservation_maligaya('Wednesday', '12pmslot')
    wednesday_1pm = check_reservation_maligaya('Wednesday', '1pmslot')
    wednesday_2pm = check_reservation_maligaya('Wednesday', '2pmslot')
    wednesday_3pm = check_reservation_maligaya('Wednesday', '3pmslot')
    wednesday_4pm = check_reservation_maligaya('Wednesday', '4pmslot')
    wednesday_5pm = check_reservation_maligaya('Wednesday', '5pmslot')
    wednesday_6pm = check_reservation_maligaya('Wednesday', '6pmslot')

    thursday_7am = check_reservation_maligaya('Thursday', '7amslot')
    thursday_8am = check_reservation_maligaya('Thursday', '8amslot')
    thursday_9am = check_reservation_maligaya('Thursday', '9amslot')
    thursday_10am = check_reservation_maligaya('Thursday', '10amslot')
    thursday_11am = check_reservation_maligaya('Thursday', '11amslot')
    thursday_12pm = check_reservation_maligaya('Thursday', '12pmslot')
    thursday_1pm = check_reservation_maligaya('Thursday', '1pmslot')
    thursday_2pm = check_reservation_maligaya('Thursday', '2pmslot')
    thursday_3pm = check_reservation_maligaya('Thursday', '3pmslot')
    thursday_4pm = check_reservation_maligaya('Thursday', '4pmslot')
    thursday_5pm = check_reservation_maligaya('Thursday', '5pmslot')
    thursday_6pm = check_reservation_maligaya('Thursday', '6pmslot')

    friday_7am = check_reservation_maligaya('Friday', '7amslot')
    friday_8am = check_reservation_maligaya('Friday', '8amslot')
    friday_9am = check_reservation_maligaya('Friday', '9amslot')
    friday_10am = check_reservation_maligaya('Friday', '10amslot')
    friday_11am = check_reservation_maligaya('Friday', '11amslot')
    friday_12pm = check_reservation_maligaya('Friday', '12pmslot')
    friday_1pm = check_reservation_maligaya('Friday', '1pmslot')
    friday_2pm = check_reservation_maligaya('Friday', '2pmslot')
    friday_3pm = check_reservation_maligaya('Friday', '3pmslot')
    friday_4pm = check_reservation_maligaya('Friday', '4pmslot')
    friday_5pm = check_reservation_maligaya('Friday', '5pmslot')
    friday_6pm = check_reservation_maligaya('Friday', '6pmslot')

    saturday_7am = check_reservation_maligaya('Saturday', '7amslot')
    saturday_8am = check_reservation_maligaya('Saturday', '8amslot')
    saturday_9am = check_reservation_maligaya('Saturday', '9amslot')
    saturday_10am = check_reservation_maligaya('Saturday', '10amslot')
    saturday_11am = check_reservation_maligaya('Saturday', '11amslot')
    saturday_12pm = check_reservation_maligaya('Saturday', '12pmslot')
    saturday_1pm = check_reservation_maligaya('Saturday', '1pmslot')
    saturday_2pm = check_reservation_maligaya('Saturday', '2pmslot')
    saturday_3pm = check_reservation_maligaya('Saturday', '3pmslot')
    saturday_4pm = check_reservation_maligaya('Saturday', '4pmslot')
    saturday_5pm = check_reservation_maligaya('Saturday', '5pmslot')
    saturday_6pm = check_reservation_maligaya('Saturday', '6pmslot')

    sunday_7am = check_reservation_maligaya('Sunday', '7amslot')
    sunday_8am = check_reservation_maligaya('Sunday', '8amslot')
    sunday_9am = check_reservation_maligaya('Sunday', '9amslot')
    sunday_10am = check_reservation_maligaya('Sunday', '10amslot')
    sunday_11am = check_reservation_maligaya('Sunday', '11amslot')
    sunday_12pm = check_reservation_maligaya('Sunday', '12pmslot')
    sunday_1pm = check_reservation_maligaya('Sunday', '1pmslot')
    sunday_2pm = check_reservation_maligaya('Sunday', '2pmslot')
    sunday_3pm = check_reservation_maligaya('Sunday', '3pmslot')
    sunday_4pm = check_reservation_maligaya('Sunday', '4pmslot')
    sunday_5pm = check_reservation_maligaya('Sunday', '5pmslot')
    sunday_6pm = check_reservation_maligaya('Sunday', '6pmslot')

    if request.method == 'POST':
        countryside_court_reservation_list = CountrysideCourtReservationList(full_name=full_name, purpose=purpose,
                                                                             number_of_attendees=int(
                                                                                 number_of_attendees),
                                                                             reservation_date=reservation_day,
                                                                             reservation_time=reservation_time,
                                                                             resident_id=user_id)
        db.session.add(countryside_court_reservation_list)
        db.session.commit()
        return render_template('resident/reservation-court2.html', username=username, full_name=full_name,
                               tuesday_7am=tuesday_7am, tuesday_8am=tuesday_8am, tuesday_9am=tuesday_9am,
                               tuesday_10am=tuesday_10am, tuesday_11am=tuesday_11am, tuesday_12pm=tuesday_12pm,
                               tuesday_1pm=tuesday_1pm, tuesday_2pm=tuesday_2pm, tuesday_3pm=tuesday_3pm,
                               tuesday_4pm=tuesday_4pm, tuesday_5pm=tuesday_5pm, tuesday_6pm=tuesday_6pm,

                               wednesday_7am=wednesday_7am, wednesday_8am=wednesday_8am, wednesday_9am=wednesday_9am,
                               wednesday_10am=wednesday_10am, wednesday_11am=wednesday_11am,
                               wednesday_12pm=wednesday_12pm, wednesday_1pm=wednesday_1pm, wednesday_2pm=wednesday_2pm,
                               wednesday_3pm=wednesday_3pm, wednesday_4pm=wednesday_4pm, wednesday_5pm=wednesday_5pm,
                               wednesday_6pm=wednesday_6pm,

                               thursday_7am=thursday_7am, thursday_8am=thursday_8am, thursday_9am=thursday_9am,
                               thursday_10am=thursday_10am, thursday_11am=thursday_11am, thursday_12pm=thursday_12pm,
                               thursday_1pm=thursday_1pm, thursday_2pm=thursday_2pm, thursday_3pm=thursday_3pm,
                               thursday_4pm=thursday_4pm, thursday_5pm=thursday_5pm, thursday_6pm=thursday_6pm,

                               friday_7am=friday_7am, friday_8am=friday_8am, friday_9am=friday_9am,
                               friday_10am=friday_10am, friday_11am=friday_11am, friday_12pm=friday_12pm,
                               friday_1pm=friday_1pm, friday_2pm=friday_2pm, friday_3pm=friday_3pm,
                               friday_4pm=friday_4pm, friday_5pm=friday_5pm, friday_6pm=friday_6pm,

                               saturday_7am=saturday_7am, saturday_8am=saturday_8am, saturday_9am=saturday_9am,
                               saturday_10am=saturday_10am, saturday_11am=saturday_11am, saturday_12pm=saturday_12pm,
                               saturday_1pm=saturday_1pm, saturday_2pm=saturday_2pm, saturday_3pm=saturday_3pm,
                               saturday_4pm=saturday_4pm, saturday_5pm=saturday_5pm, saturday_6pm=saturday_6pm,

                               sunday_7am=sunday_7am, sunday_8am=sunday_8am, sunday_9am=sunday_9am,
                               sunday_10am=sunday_10am, sunday_11am=sunday_11am, sunday_12pm=sunday_12pm,
                               sunday_1pm=sunday_1pm, sunday_2pm=sunday_2pm, sunday_3pm=sunday_3pm,
                               sunday_4pm=sunday_4pm, sunday_5pm=sunday_5pm, sunday_6pm=sunday_6pm)

    return render_template('resident/reservation-court2.html', username=username, full_name=full_name,
                           tuesday_7am=tuesday_7am, tuesday_8am=tuesday_8am, tuesday_9am=tuesday_9am,
                           tuesday_10am=tuesday_10am, tuesday_11am=tuesday_11am, tuesday_12pm=tuesday_12pm,
                           tuesday_1pm=tuesday_1pm, tuesday_2pm=tuesday_2pm, tuesday_3pm=tuesday_3pm,
                           tuesday_4pm=tuesday_4pm, tuesday_5pm=tuesday_5pm, tuesday_6pm=tuesday_6pm,

                           wednesday_7am=wednesday_7am, wednesday_8am=wednesday_8am, wednesday_9am=wednesday_9am,
                           wednesday_10am=wednesday_10am, wednesday_11am=wednesday_11am, wednesday_12pm=wednesday_12pm,
                           wednesday_1pm=wednesday_1pm, wednesday_2pm=wednesday_2pm, wednesday_3pm=wednesday_3pm,
                           wednesday_4pm=wednesday_4pm, wednesday_5pm=wednesday_5pm, wednesday_6pm=wednesday_6pm,

                           thursday_7am=thursday_7am, thursday_8am=thursday_8am, thursday_9am=thursday_9am,
                           thursday_10am=thursday_10am, thursday_11am=thursday_11am, thursday_12pm=thursday_12pm,
                           thursday_1pm=thursday_1pm, thursday_2pm=thursday_2pm, thursday_3pm=thursday_3pm,
                           thursday_4pm=thursday_4pm, thursday_5pm=thursday_5pm, thursday_6pm=thursday_6pm,

                           friday_7am=friday_7am, friday_8am=friday_8am, friday_9am=friday_9am, friday_10am=friday_10am,
                           friday_11am=friday_11am, friday_12pm=friday_12pm, friday_1pm=friday_1pm,
                           friday_2pm=friday_2pm, friday_3pm=friday_3pm, friday_4pm=friday_4pm, friday_5pm=friday_5pm,
                           friday_6pm=friday_6pm,

                           saturday_7am=saturday_7am, saturday_8am=saturday_8am, saturday_9am=saturday_9am,
                           saturday_10am=saturday_10am, saturday_11am=saturday_11am, saturday_12pm=saturday_12pm,
                           saturday_1pm=saturday_1pm, saturday_2pm=saturday_2pm, saturday_3pm=saturday_3pm,
                           saturday_4pm=saturday_4pm, saturday_5pm=saturday_5pm, saturday_6pm=saturday_6pm,

                           sunday_7am=sunday_7am, sunday_8am=sunday_8am, sunday_9am=sunday_9am, sunday_10am=sunday_10am,
                           sunday_11am=sunday_11am, sunday_12pm=sunday_12pm, sunday_1pm=sunday_1pm,
                           sunday_2pm=sunday_2pm, sunday_3pm=sunday_3pm, sunday_4pm=sunday_4pm, sunday_5pm=sunday_5pm,
                           sunday_6pm=sunday_6pm)


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
