import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    SQLALCHEMY_DATABASE_URI = "mysql://ghandylan2:barangay_db@ghandylan2.mysql.pythonanywhere-services.com/ghandylan2$default"
    # SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL') + os.getenv('DATABASE_NAME')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY')
