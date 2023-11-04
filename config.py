import os
from dotenv import load_dotenv

load_dotenv()


class Config:
<<<<<<< HEAD
    SQLALCHEMY_DATABASE_URI = "mysql://ghandylan2:8AWqNfQ-fWuhSt_@ghandylan2.mysql.pythonanywhere-services.com/ghandylan2$barangay_db"
    # SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL') + os.getenv('DATABASE_NAME')
=======
    SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}"
>>>>>>> f3dcc15303d43e41086a9b2721a57114c002a64b
    SQLALCHEMY_TRACK_MODIFICATIONS = False
