import os

from dotenv import load_dotenv
from flask import Flask, redirect, render_template, request
from flask_login import *
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

load_dotenv()
app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL') + os.getenv('DATABASE_NAME')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return Admin.query.get(int(user_id))


db = SQLAlchemy()
db.init_app(app)


class Admin(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)


class BarangayOfficial(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)


@app.route('/')
def hello_world():  # put application's code here
    return redirect('/login')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get("username")
        password = request.form.get("password")
        new_admin = Admin(username=username, password=password)
        db.session.add(new_admin)
        db.session.commit()
        db.session.close()

    return render_template('login.html')


if __name__ == '__main__':
    app.run()
    db.create_all()
