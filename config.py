import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    SQLALCHEMY_DATABASE_URI = "mysql://ghandylan2:barangay@ghandylan2.mysql.pythonanywhere-services.com/ghandylan2$default"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY')
