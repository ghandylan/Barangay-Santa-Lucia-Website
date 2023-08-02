from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate

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
    login_manager.login_view = 'login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        from models import BarangayOfficial, Resident
        if BarangayOfficial.query.get(int(user_id)):
            return BarangayOfficial.query.get(int(user_id))
        elif Resident.query.get(int(user_id)):
            return Resident.query.get(int(user_id))
        else:
            return None

    # initialize the db
    migrate = Migrate()
    # register the db to the migration tool
    migrate.init_app(app, db)
    # register the db to the app
    db.init_app(app)

    app.register_blueprint(views_blueprint)
    app.register_blueprint(brngyofficial_views_blueprint)
    app.register_blueprint(resident_views_blueprint)

    return app


app_instance = create_app()

if __name__ == '__main__':
    app_instance.run(threaded=True)
