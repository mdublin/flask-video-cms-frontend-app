import os

ADMINS = ['admin@test.com']
#DEBUG = False
DEBUG = True
SECRET_KEY = 'top secret!'
#SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(
#    os.path.dirname(__file__), '../data.sqlite3')

SQLALCHEMY_DATABASE_URI = "postgresql://mdublin1@localhost:5432/VideoDashBoard"



