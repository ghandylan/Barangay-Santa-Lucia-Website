import uuid

import bcrypt
from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate

from blueprints.barangayofficialviews import brngyofficial_views_blueprint
from blueprints.residentviews import resident_views_blueprint
from blueprints.views import views_blueprint
from config import Config
from models import db, BarangayOfficial


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
    migrate = Migrate(app, db)
    migrate.init_app(app, db)
    app.register_blueprint(views_blueprint)
    app.register_blueprint(brngyofficial_views_blueprint)
    app.register_blueprint(resident_views_blueprint)

    # create an admin user if not exists
    with app.app_context():
        admin_init = BarangayOfficial.query.filter_by(username="admin").first()
        if admin_init is None:
            admin_init = BarangayOfficial(
                id=uuid.uuid4(),
                role="barangay_official",
                full_name="admin",
                sex="male",
                username="admin",
                password=bcrypt.hashpw("admin".encode('utf-8'), bcrypt.gensalt()),
                birthdate="1999-01-01",
                relocation_year="1999",
                address="admin")
            db.session.add(admin_init)
            db.session.commit()

    return app


app_instance = create_app()

if __name__ == '__main__':
    app_instance.run(threaded=True, debug=True)
