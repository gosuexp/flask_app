import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:123@localhost:5432/app'
    #SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:123@db:5432/app'  #docker
    SQLALCHEMY_TRACK_MODIFICATIONS = False