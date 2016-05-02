import os

import psycopg2
import urlparse

ADMINS = ['admin@test.com']
DEBUG = False
SECRET_KEY = 'top secret!'
#SQLALCHEMY_DATABASE_URI = 'postgresql://mdublin:buggy101@localhost:5432/VideoDashBoard'
DATABASE_URL = 'postgresql://mdublin:buggy101@localhost:5432/VideoDashBoard'


basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = True
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'this-really-needs-to-be-changed'
    #SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    SQLALCHEMY_DATABASE_URI = DATABASE_URL


class ProductionConfig(Config):
    DEBUG = True



#SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(
#    os.path.dirname(__file__), '../data.sqlite3')

#DATABASE_URL = "postgres://oxogvaquetjage:X4wK3auttNuB2oZTkqzoI7Gid_@ec2-54-243-196-42.compute-1.amazonaws.com:5432/df6vtpcae81mm5"
#urlparse.uses_netloc.append("postgres")
#url = urlparse.urlparse(os.environ[DATABASE_URL])
#url = urlparse.urlparse(os.environ["DATABASE_URL"])
#url = urlparse.urlparse(os.environ["postgres://oxogvaquetjage:X4wK3auttNuB2oZTkqzoI7Gid_@ec2-54-243-196-42.compute-1.amazonaws.com:5432/df6vtpcae81mm5"])
#conn = psycopg2.connect(
#    database=url.path[1:],
#    user=url.username,
#    password=url.password,
#    host=url.hostname,
#    port=url.port
#)

