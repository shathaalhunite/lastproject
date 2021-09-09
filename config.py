import os
basedir = os.path.abspath(os.path.dirname(__file__))
DEBUG = True
SECRET_KEY = os.environ.get('SECRET_KEY')
DATABASE_URL = os.environ['DATABASE_URL']
SQLALCHEMY_TRACK_MODIFICATIONS = False

