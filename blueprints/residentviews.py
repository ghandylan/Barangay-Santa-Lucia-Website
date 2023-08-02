from flask import Blueprint, render_template
from flask_login import login_required

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


@resident_views_blueprint.route('/resident/facilities/court1')
@login_required
def resident_facilities_court1():
    return render_template('resident/reservation-court1.html')


@resident_views_blueprint.route('/resident/facilities/court2')
@login_required
def resident_facilities_court2():
    return render_template('resident/reservation-court2.html')


@resident_views_blueprint.route('/resident/facilities/tennis-court')
@login_required
def resident_facilities_tennis_court():
    return render_template('resident/reservation-tenniscourt.html')


@resident_views_blueprint.route('/resident/services')
@login_required
def resident_services():
    return render_template('resident/itemrenting.html')


@resident_views_blueprint.route('/resident/profile/<username>')
@login_required
def resident_profile(username):
    return render_template('resident/profile.html', username=username)