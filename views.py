from flask import redirect, render_template, request

from models import Admin, db


def init_views(app):
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
