import os

ADMINS = ['admin@test.com']
DEBUG = False
SECRET_KEY = 'top secret!'
SQLALCHEMY_DATABASE_URI = 'postgresql://username:password@localhost:5432/VideoDashBoard'
#SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(
#    os.path.dirname(__file__), '../data.sqlite3')
