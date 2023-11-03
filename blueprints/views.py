import bcrypt
from flask import redirect, render_template, request, Blueprint, url_for, flash
from flask_login import login_required, login_user, logout_user

from models import BarangayOfficial, Resident

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
        user = BarangayOfficial.query.filter_by(username=username).first()
        if user:
            if bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
                login_user(user)
                return redirect(url_for('brngyofficial_views.barangay_official_home'))
            else:
                flash("Incorrect Password", category='error')
                return render_template('visitor/login.html', error="Incorrect Password")
        else:
            if bcrypt.checkpw(bytes(password, encoding='utf-8'), bytes(user.password, encoding='utf-8')):
                login_user(user)
                return redirect(url_for('resident_views.resident_home'))

        # TODO: update the password checking
        if user:
            if user.password == password:
                login_user(user)
                return redirect(url_for('resident_views.resident_home'))
            else:
                flash("Incorrect Password", category='error')
                return render_template('visitor/login.html', error="Incorrect Password")
        else:
            flash("User does not exist", category='error')
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
