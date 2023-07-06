import os

from dotenv import load_dotenv
from flask import Flask, redirect
from flask_login import *
from flask_sqlalchemy import SQLAlchemy

# from models import *

load_dotenv()

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL') + '/' + os.getenv('DATABASE_NAME')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)

db = SQLAlchemy(app)


@app.route('/')
def hello_world():  # put application's code here
    return redirect('/login')


@app.route('/login')
def login():
    admin = Admin.query.filter_by(username='admin').first()
    return admin


if __name__ == '__main__':
    app.run()
    db.create_all()
