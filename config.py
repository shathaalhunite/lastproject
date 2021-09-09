import os
basedir = os.path.abspath(os.path.dirname(__file__))
DEBUG = True
SECRET_KEY = os.urandom(32)
SQLALCHEMY_DATABASE_URI = 'postgresql://nlvupvrifzdcoz:4ae6bcce2eb595915c6d77d290c4f209fb43aac05dbb2b946c399ec34d0b4be3@localhost:5432/d6cmhnoaos9b2r'
SQLALCHEMY_TRACK_MODIFICATIONS = False
