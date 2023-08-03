from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from check_reservation import check_reservation_maligaya, check_reservation_countryside, check_reservation_tennis

from models import Resident, MaligayaCourtReservationList, CountrysideCourtReservationList, db, \
    TennisCourtReservationList, Items, ItemRentals

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

        # check if the user already reserved a slot
        check_reservation = MaligayaCourtReservationList.query.filter_by(reservation_date=reservation_day,
                                                                         reservation_time=reservation_time,
                                                                         resident_id=user_id).first()
        if check_reservation:
            flash('You already reserved a slot for this day and time!', 'danger')
            return redirect(url_for('resident_views.resident_facilities_court1'))
        else:
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


@resident_views_blueprint.route('/resident/facilities/court2', methods=['GET', 'POST'])
@login_required
def resident_facilities_court2():
    user_id = current_user.id
    username = current_user.username
    full_name = current_user.full_name
    purpose = request.form.get('purpose')
    number_of_attendees = request.form.get('pax')
    reservation_day = request.form.get('date')
    reservation_time = request.form.get('time')

    tuesday_7am = check_reservation_countryside('Tuesday', '7amslot')
    tuesday_8am = check_reservation_countryside('Tuesday', '8amslot')
    tuesday_9am = check_reservation_countryside('Tuesday', '9amslot')
    tuesday_10am = check_reservation_countryside('Tuesday', '10amslot')
    tuesday_11am = check_reservation_countryside('Tuesday', '11amslot')
    tuesday_12pm = check_reservation_countryside('Tuesday', '12pmslot')
    tuesday_1pm = check_reservation_countryside('Tuesday', '1pmslot')
    tuesday_2pm = check_reservation_countryside('Tuesday', '2pmslot')
    tuesday_3pm = check_reservation_countryside('Tuesday', '3pmslot')
    tuesday_4pm = check_reservation_countryside('Tuesday', '4pmslot')
    tuesday_5pm = check_reservation_countryside('Tuesday', '5pmslot')
    tuesday_6pm = check_reservation_countryside('Tuesday', '6pmslot')

    wednesday_7am = check_reservation_countryside('Wednesday', '7amslot')
    wednesday_8am = check_reservation_countryside('Wednesday', '8amslot')
    wednesday_9am = check_reservation_countryside('Wednesday', '9amslot')
    wednesday_10am = check_reservation_countryside('Wednesday', '10amslot')
    wednesday_11am = check_reservation_countryside('Wednesday', '11amslot')
    wednesday_12pm = check_reservation_countryside('Wednesday', '12pmslot')
    wednesday_1pm = check_reservation_countryside('Wednesday', '1pmslot')
    wednesday_2pm = check_reservation_countryside('Wednesday', '2pmslot')
    wednesday_3pm = check_reservation_countryside('Wednesday', '3pmslot')
    wednesday_4pm = check_reservation_countryside('Wednesday', '4pmslot')
    wednesday_5pm = check_reservation_countryside('Wednesday', '5pmslot')
    wednesday_6pm = check_reservation_countryside('Wednesday', '6pmslot')

    thursday_7am = check_reservation_countryside('Thursday', '7amslot')
    thursday_8am = check_reservation_countryside('Thursday', '8amslot')
    thursday_9am = check_reservation_countryside('Thursday', '9amslot')
    thursday_10am = check_reservation_countryside('Thursday', '10amslot')
    thursday_11am = check_reservation_countryside('Thursday', '11amslot')
    thursday_12pm = check_reservation_countryside('Thursday', '12pmslot')
    thursday_1pm = check_reservation_countryside('Thursday', '1pmslot')
    thursday_2pm = check_reservation_countryside('Thursday', '2pmslot')
    thursday_3pm = check_reservation_countryside('Thursday', '3pmslot')
    thursday_4pm = check_reservation_countryside('Thursday', '4pmslot')
    thursday_5pm = check_reservation_countryside('Thursday', '5pmslot')
    thursday_6pm = check_reservation_countryside('Thursday', '6pmslot')

    friday_7am = check_reservation_countryside('Friday', '7amslot')
    friday_8am = check_reservation_countryside('Friday', '8amslot')
    friday_9am = check_reservation_countryside('Friday', '9amslot')
    friday_10am = check_reservation_countryside('Friday', '10amslot')
    friday_11am = check_reservation_countryside('Friday', '11amslot')
    friday_12pm = check_reservation_countryside('Friday', '12pmslot')
    friday_1pm = check_reservation_countryside('Friday', '1pmslot')
    friday_2pm = check_reservation_countryside('Friday', '2pmslot')
    friday_3pm = check_reservation_countryside('Friday', '3pmslot')
    friday_4pm = check_reservation_countryside('Friday', '4pmslot')
    friday_5pm = check_reservation_countryside('Friday', '5pmslot')
    friday_6pm = check_reservation_countryside('Friday', '6pmslot')

    saturday_7am = check_reservation_countryside('Saturday', '7amslot')
    saturday_8am = check_reservation_countryside('Saturday', '8amslot')
    saturday_9am = check_reservation_countryside('Saturday', '9amslot')
    saturday_10am = check_reservation_countryside('Saturday', '10amslot')
    saturday_11am = check_reservation_countryside('Saturday', '11amslot')
    saturday_12pm = check_reservation_countryside('Saturday', '12pmslot')
    saturday_1pm = check_reservation_countryside('Saturday', '1pmslot')
    saturday_2pm = check_reservation_countryside('Saturday', '2pmslot')
    saturday_3pm = check_reservation_countryside('Saturday', '3pmslot')
    saturday_4pm = check_reservation_countryside('Saturday', '4pmslot')
    saturday_5pm = check_reservation_countryside('Saturday', '5pmslot')
    saturday_6pm = check_reservation_countryside('Saturday', '6pmslot')

    sunday_7am = check_reservation_countryside('Sunday', '7amslot')
    sunday_8am = check_reservation_countryside('Sunday', '8amslot')
    sunday_9am = check_reservation_countryside('Sunday', '9amslot')
    sunday_10am = check_reservation_countryside('Sunday', '10amslot')
    sunday_11am = check_reservation_countryside('Sunday', '11amslot')
    sunday_12pm = check_reservation_countryside('Sunday', '12pmslot')
    sunday_1pm = check_reservation_countryside('Sunday', '1pmslot')
    sunday_2pm = check_reservation_countryside('Sunday', '2pmslot')
    sunday_3pm = check_reservation_countryside('Sunday', '3pmslot')
    sunday_4pm = check_reservation_countryside('Sunday', '4pmslot')
    sunday_5pm = check_reservation_countryside('Sunday', '5pmslot')
    sunday_6pm = check_reservation_countryside('Sunday', '6pmslot')

    if request.method == 'POST':
        countryside_court_reservation_list = CountrysideCourtReservationList(full_name=full_name, purpose=purpose,
                                                                             number_of_attendees=int(
                                                                                 number_of_attendees),
                                                                             reservation_date=reservation_day,
                                                                             reservation_time=reservation_time,
                                                                             resident_id=user_id)

        check_reservation = CountrysideCourtReservationList.query.filter_by(reservation_date=reservation_day,
                                                                            reservation_time=reservation_time,
                                                                            resident_id=user_id).first()
        if check_reservation:
            flash('You already reserved a slot for this day and time!', 'danger')
            return redirect(url_for('resident_views.resident_facilities_court2'))
        else:
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


@resident_views_blueprint.route('/resident/facilities/tennis-court', methods=['GET', 'POST'])
@login_required
def resident_facilities_tennis_court():
    user_id = current_user.id
    username = current_user.username
    full_name = current_user.full_name
    purpose = request.form.get('purpose')
    number_of_attendees = request.form.get('pax')
    reservation_day = request.form.get('date')
    reservation_time = request.form.get('time')

    tuesday_7am = check_reservation_tennis('Tuesday', '7amslot')
    tuesday_8am = check_reservation_tennis('Tuesday', '8amslot')
    tuesday_9am = check_reservation_tennis('Tuesday', '9amslot')
    tuesday_10am = check_reservation_tennis('Tuesday', '10amslot')
    tuesday_11am = check_reservation_tennis('Tuesday', '11amslot')
    tuesday_12pm = check_reservation_tennis('Tuesday', '12pmslot')
    tuesday_1pm = check_reservation_tennis('Tuesday', '1pmslot')
    tuesday_2pm = check_reservation_tennis('Tuesday', '2pmslot')
    tuesday_3pm = check_reservation_tennis('Tuesday', '3pmslot')
    tuesday_4pm = check_reservation_tennis('Tuesday', '4pmslot')
    tuesday_5pm = check_reservation_tennis('Tuesday', '5pmslot')
    tuesday_6pm = check_reservation_tennis('Tuesday', '6pmslot')

    wednesday_7am = check_reservation_tennis('Wednesday', '7amslot')
    wednesday_8am = check_reservation_tennis('Wednesday', '8amslot')
    wednesday_9am = check_reservation_tennis('Wednesday', '9amslot')
    wednesday_10am = check_reservation_tennis('Wednesday', '10amslot')
    wednesday_11am = check_reservation_tennis('Wednesday', '11amslot')
    wednesday_12pm = check_reservation_tennis('Wednesday', '12pmslot')
    wednesday_1pm = check_reservation_tennis('Wednesday', '1pmslot')
    wednesday_2pm = check_reservation_tennis('Wednesday', '2pmslot')
    wednesday_3pm = check_reservation_tennis('Wednesday', '3pmslot')
    wednesday_4pm = check_reservation_tennis('Wednesday', '4pmslot')
    wednesday_5pm = check_reservation_tennis('Wednesday', '5pmslot')
    wednesday_6pm = check_reservation_tennis('Wednesday', '6pmslot')

    thursday_7am = check_reservation_tennis('Thursday', '7amslot')
    thursday_8am = check_reservation_tennis('Thursday', '8amslot')
    thursday_9am = check_reservation_tennis('Thursday', '9amslot')
    thursday_10am = check_reservation_tennis('Thursday', '10amslot')
    thursday_11am = check_reservation_tennis('Thursday', '11amslot')
    thursday_12pm = check_reservation_tennis('Thursday', '12pmslot')
    thursday_1pm = check_reservation_tennis('Thursday', '1pmslot')
    thursday_2pm = check_reservation_tennis('Thursday', '2pmslot')
    thursday_3pm = check_reservation_tennis('Thursday', '3pmslot')
    thursday_4pm = check_reservation_tennis('Thursday', '4pmslot')
    thursday_5pm = check_reservation_tennis('Thursday', '5pmslot')
    thursday_6pm = check_reservation_tennis('Thursday', '6pmslot')

    friday_7am = check_reservation_tennis('Friday', '7amslot')
    friday_8am = check_reservation_tennis('Friday', '8amslot')
    friday_9am = check_reservation_tennis('Friday', '9amslot')
    friday_10am = check_reservation_tennis('Friday', '10amslot')
    friday_11am = check_reservation_tennis('Friday', '11amslot')
    friday_12pm = check_reservation_tennis('Friday', '12pmslot')
    friday_1pm = check_reservation_tennis('Friday', '1pmslot')
    friday_2pm = check_reservation_tennis('Friday', '2pmslot')
    friday_3pm = check_reservation_tennis('Friday', '3pmslot')
    friday_4pm = check_reservation_tennis('Friday', '4pmslot')
    friday_5pm = check_reservation_tennis('Friday', '5pmslot')
    friday_6pm = check_reservation_tennis('Friday', '6pmslot')

    saturday_7am = check_reservation_tennis('Saturday', '7amslot')
    saturday_8am = check_reservation_tennis('Saturday', '8amslot')
    saturday_9am = check_reservation_tennis('Saturday', '9amslot')
    saturday_10am = check_reservation_tennis('Saturday', '10amslot')
    saturday_11am = check_reservation_tennis('Saturday', '11amslot')
    saturday_12pm = check_reservation_tennis('Saturday', '12pmslot')
    saturday_1pm = check_reservation_tennis('Saturday', '1pmslot')
    saturday_2pm = check_reservation_tennis('Saturday', '2pmslot')
    saturday_3pm = check_reservation_tennis('Saturday', '3pmslot')
    saturday_4pm = check_reservation_tennis('Saturday', '4pmslot')
    saturday_5pm = check_reservation_tennis('Saturday', '5pmslot')
    saturday_6pm = check_reservation_tennis('Saturday', '6pmslot')

    sunday_7am = check_reservation_tennis('Sunday', '7amslot')
    sunday_8am = check_reservation_tennis('Sunday', '8amslot')
    sunday_9am = check_reservation_tennis('Sunday', '9amslot')
    sunday_10am = check_reservation_tennis('Sunday', '10amslot')
    sunday_11am = check_reservation_tennis('Sunday', '11amslot')
    sunday_12pm = check_reservation_tennis('Sunday', '12pmslot')
    sunday_1pm = check_reservation_tennis('Sunday', '1pmslot')
    sunday_2pm = check_reservation_tennis('Sunday', '2pmslot')
    sunday_3pm = check_reservation_tennis('Sunday', '3pmslot')
    sunday_4pm = check_reservation_tennis('Sunday', '4pmslot')
    sunday_5pm = check_reservation_tennis('Sunday', '5pmslot')
    sunday_6pm = check_reservation_tennis('Sunday', '6pmslot')

    if request.method == 'POST':
        tennis_court_reservation_list = TennisCourtReservationList(full_name=full_name, purpose=purpose,
                                                                   number_of_attendees=int(number_of_attendees),
                                                                   reservation_date=reservation_day,
                                                                   reservation_time=reservation_time,
                                                                   resident_id=user_id)

        check_reservation = TennisCourtReservationList.query.filter_by(reservation_date=reservation_day,
                                                                       reservation_time=reservation_time,
                                                                       resident_id=user_id).first()
        if check_reservation:
            flash('You already reserved a slot for this day and time!', 'danger')
            return redirect(url_for('resident_views.resident_facilities_court2'))
        else:
            db.session.add(tennis_court_reservation_list)
            db.session.commit()

        return render_template('resident/reservation-tenniscourt.html', username=username, full_name=full_name,
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

    return render_template('resident/reservation-tenniscourt.html', username=username, full_name=full_name,
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


@resident_views_blueprint.route('/resident/services', methods=['GET', 'POST'])
@login_required
def resident_services():
    username = current_user.username

    # query all items from the database
    chairs = Items.query.filter_by(item_name='Chairs').first().item_quantity
    tables = Items.query.filter_by(item_name='Tables').first().item_quantity
    tents = Items.query.filter_by(item_name='Tents').first().item_quantity



    if request.method == 'POST':
        # get user's details
        resident_id = current_user.id
        full_name = current_user.full_name
        rent_date = request.form.get('rentdate')
        barangay_number = current_user.barangay_number
        address = current_user.address

        # get the number of items borrowed from the form
        chairs_borrowed = request.form.get('chairs')
        tables_borrowed = request.form.get('tables')
        tents_borrowed = request.form.get('tents')

        # deducting the borrowed items from the database
        chair_count = chairs - chairs_borrowed
        table_count = chairs - tables_borrowed
        tent_count = chairs - tents_borrowed

        # update the database, deduct the borrowed items
        Items.query.filter_by(item_name='Chairs').update(dict(item_quantity=chair_count))
        Items.query.filter_by(item_name='Tables').update(dict(item_quantity=table_count))
        Items.query.filter_by(item_name='Tents').update(dict(item_quantity=tent_count))

        # add the record to the database
        borrow_record = ItemRentals(full_name=full_name,
                                    chairs_borrowed=chairs_borrowed,
                                    tables_borrowed=tables_borrowed,
                                    tents_borrowed=tents_borrowed,
                                    barangay_number=barangay_number,
                                    id=resident_id,
                                    borrow_date=rent_date
                                    )
        db.session.add(borrow_record)
        db.session.commit()

        return redirect(url_for('resident_views.resident_services', username=username))

    return render_template('resident/itemrenting.html', username=username, chairs=chairs, tables=tables, tents=tents)


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
