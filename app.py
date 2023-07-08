import os

from dotenv import load_dotenv
from flask import Flask, redirect, render_template, request
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import db, Admin

# load the env vars
load_dotenv()
# initialize the flask app
app = Flask(__name__)

# configure the database connection
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL') + os.getenv('DATABASE_NAME')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return Admin.query.get(int(user_id))


db.init_app(app)
migrate = Migrate(app, db)


@app.route('/')
def hello_world():  # put application's code here
    return redirect('/login')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get("username")
        password = request.form.get("password")
        # noinspection PyArgumentList
        new_admin = Admin(username=username, password=password)
        db.session.add(new_admin)
        db.session.commit()
        db.session.close()

    return render_template('login.html')


if __name__ == '__main__':
    app.run()
