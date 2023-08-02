import uuid

from flask import Blueprint, render_template, request
from flask_login import login_required

from models import Resident, db

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
    return render_template('barangayofficial/residents.html')


@brngyofficial_views_blueprint.route('/barangay_official/residents/add', methods=['POST', 'GET'])
@login_required
def barangay_official_add_residents():
    # create a minimized uuidv4
    resident_id = str(uuid.uuid4())[:8]

    # profile_picture = request.form.get('profile_picture')
    full_name = request.form.get('fullname')
    barangay_number = uuid.uuid4()
    sex = request.form.get('sex')
    username = request.form.get('username')
    # password = request.form.get('password')

    birth_date = request.form.get('birthdate')
    relocation_year = request.form.get('relocationyear')
    address = request.form.get('address')
    if request.method == 'POST':
        new_resident = Resident(id=resident_id, photo=None, full_name=full_name, barangay_number=barangay_number,
            sex=sex, username=username, password=None, birthdate=birth_date, relocation_year=relocation_year,
            address=address)

        db.session.add(new_resident)
        db.session.commit()

        return render_template('barangayofficial/residents.html')

    return render_template('barangayofficial/adduser.html')


# @brngyofficial_views_blueprint.route('/', methods=['GET', 'POST'])

@brngyofficial_views_blueprint.route('/barangay_official/services')
@login_required
def barangay_official_item_tracking():
    return render_template('barangayofficial/itemrenting-admin.html')


@brngyofficial_views_blueprint.route('/barangay_official/services/maligaya-court-reservations')
@login_required
def barangay_official_maligaya_court_reservations():
    return render_template('barangayofficial/reservation-admin-court1.html')


@brngyofficial_views_blueprint.route('/barangay_official/services/countryside-court-reservations')
@login_required
def barangay_official_countryside_court_reservations():
    return render_template('barangayofficial/reservation-admin-court2.html')


@brngyofficial_views_blueprint.route('/barangay_official/services/tennis-court-reservations')
@login_required
def barangay_official_tennis_court_reservations():
    return render_template('barangayofficial/reservation-admin-tenniscourt.html')


@brngyofficial_views_blueprint.route('/barangay_official/profile/<username>')
@login_required
def barangay_official_profile(username):
    return render_template('barangayofficial/profile.html', username=username)
