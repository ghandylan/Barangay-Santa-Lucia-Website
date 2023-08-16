from flask import Flask
from flask_login import LoginManager

from blueprints.barangayofficialviews import brngyofficial_views_blueprint
from blueprints.residentviews import resident_views_blueprint
from blueprints.views import views_blueprint
from config import Config
from models import db


def create_app():
    # initialize the flask app
    app = Flask(__name__)
    app.config.from_object(Config)

    login_manager = LoginManager()
    login_manager.login_view = 'views.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(barangay_number):
        from models import BarangayOfficial, Resident
        if BarangayOfficial.query.get(barangay_number):
            return BarangayOfficial.query.get(barangay_number)
        elif Resident.query.get(barangay_number):
            return Resident.query.get(barangay_number)
        else:
            return None

    # register the db to the app
    db.init_app(app)

    app.register_blueprint(views_blueprint)
    app.register_blueprint(brngyofficial_views_blueprint)
    app.register_blueprint(resident_views_blueprint)

    return app


app_instance = create_app()

if __name__ == '__main__':
    app_instance.run(threaded=True)
