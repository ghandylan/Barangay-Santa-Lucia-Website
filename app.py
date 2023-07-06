import os

from dotenv import load_dotenv
from flask import Flask, redirect, render_template, request
from flask_login import *
from flask_wtf.csrf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

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

# csrf protection
csrf = CSRFProtect(app)
csrf.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return Admin.query.get(int(user_id))


with app.app_context():
    db = SQLAlchemy()
    db.init_app(app)




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
    db.create_all()
