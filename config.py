import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    SQLALCHEMY_DATABASE_URI = "mysql://ghandylan2:8AWqNfQ-fWuhSt_@ghandylan2.mysql.pythonanywhere-services.com/ghandylan2$barangay_db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
