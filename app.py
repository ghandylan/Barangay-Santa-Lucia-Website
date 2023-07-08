from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate

from config import Config
from views import *

# initialize the flask app
app = Flask(__name__)
app.config.from_object(Config)

login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return Admin.query.get(int(user_id))


db.init_app(app)
migrate = Migrate(app, db)
init_views(app)

if __name__ == '__main__':
    app.run()
