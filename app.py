from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate

from config import Config
from models import db, BarangayOfficial, Resident
from views import views_blueprint


def create_app():
    # initialize the flask app
    app = Flask(__name__)
    app.config.from_object(Config)

    login_manager = LoginManager()
    login_manager.login_view = 'login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        barangay_official = BarangayOfficial.query.get(int(user_id))
        if barangay_official:
            return barangay_official

        resident = Resident.query.get(int(user_id))
        if resident:
            return resident

        return None

    # initialize the db
    migrate = Migrate()
    # register the db to the migration tool
    migrate.init_app(app, db)
    # register the db to the app
    db.init_app(app)

    app.register_blueprint(views_blueprint)

    return app


app_instance = create_app()

if __name__ == '__main__':
    app_instance.run()
