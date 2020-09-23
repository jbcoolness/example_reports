import os


#class config():
#    SECRET_KEY = 'my_secret_key'


class DevelopmentConfig():
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql://root:Julio123456*@localhost:test'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
