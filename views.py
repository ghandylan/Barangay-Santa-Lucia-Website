from flask import redirect, render_template, request, Blueprint
from flask_login import login_required, login_user, current_user, logout_user

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
        user = BarangayOfficial.query.filter_by(username=username).first()
        if user:
            if user.password == password:
                login_user(user, remember=True)
                return redirect('/barangay_official')
            else:
                return render_template('login.html', error="Incorrect Password")
        else:
            user = Resident.query.filter_by(username=username).first()
            if user:
                if user.password == password:
                    login_user(user, remember=True)
                    return redirect('/resident')
                else:
                    return render_template('login.html', error="Incorrect Password")
            else:
                return render_template('login.html', error="User does not exist")

    return render_template('login.html')


@views_blueprint.route('/barangay_official')
@login_required
def barangay_official():
    user = current_user.get_id()
    user_name = BarangayOfficial.query.filter_by(id=user).first()
    return render_template('barangayofficial/draft-home.html', user_name=user_name.username)


@views_blueprint.route('/resident')
@login_required
def resident():
    user = current_user.get_id()
    user_name = Resident.query.filter_by(id=user).first()
    return render_template('resident/draft-home.html', user_name=user_name.username)


@views_blueprint.route('/home')
def home():
    return render_template('home.html')


@views_blueprint.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/home')
