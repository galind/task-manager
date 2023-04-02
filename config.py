import os


class Config:
    SECRET_KEY = os.urandom(12)
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = True
