from flask import redirect, render_template, request, Blueprint, url_for
from flask_login import login_required, login_user, logout_user

from models import *

views_blueprint = Blueprint('views', __name__)


@views_blueprint.route('/')
def hello_world():  # put application's code here
    return redirect('/login')


@views_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get("emaillogin")
        password = request.form.get("passwordlogin")

        # check if user is a BarangayOfficial or Resident
        user = BarangayOfficial.query.filter_by(username=username, password=password).first()
        if user:
            if user.password == password:
                login_user(user)
                return redirect(url_for('brngyofficial_views.barangay_official_home'))
            else:
                return render_template('visitor/login.html', error="Incorrect Password")
        else:
            user = Resident.query.filter_by(username=username, password=password).first()
            if user:
                if user.password == password:
                    login_user(user)
                    return redirect(url_for('resident_views.resident_home'))
                else:
                    return render_template('visitor/login.html', error="Incorrect Password")
            else:
                return render_template('visitor/login.html', error="User does not exist")

    return render_template('visitor/login.html')


@views_blueprint.route('/home')
def home():
    return render_template('visitor/home.html')


@views_blueprint.route('/the_barangay')
def the_barangay():
    return render_template('visitor/the_barangay.html')


@views_blueprint.route('/facilities')
def facilities():
    return render_template('visitor/facilities.html')


@views_blueprint.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/home')
