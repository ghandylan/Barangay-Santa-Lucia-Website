import os
from dotenv import load_dotenv

load_dotenv()


class Config:
<<<<<<< HEAD
    SQLALCHEMY_DATABASE_URI = "mysql://ghandylan2:barangay@ghandylan2.mysql.pythonanywhere-services.com/ghandylan2$default"
=======
    #  SQLALCHEMY_DATABASE_URI = "mysql://ghandylan2:barangay@ghandylan2.mysql.pythonanywhere-services.com/ghandylan2$default"
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL') + os.getenv('DATABASE_NAME')
>>>>>>> 64a6a8d0396ea91f3107cb529056eca7529276f5
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY')
