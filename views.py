from flask import redirect, render_template, request, Blueprint
from models import Admin, db

views_blueprint = Blueprint('views', __name__)


@views_blueprint.route('/')
def hello_world():  # put application's code here
    return redirect('/login')


@views_blueprint.route('/login', methods=['GET', 'POST'])
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
