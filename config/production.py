import os

import psycopg2
import urlparse

ADMINS = ['admin@test.com']
DEBUG = False
SECRET_KEY = 'top secret!'
#SQLALCHEMY_DATABASE_URI = 'postgresql://username:password@localhost:5432/VideoDashBoard'
#SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(
#    os.path.dirname(__file__), '../data.sqlite3')

urlparse.uses_netloc.append("postgres")
url = urlparse.urlparse(os.environ["DATABASE_URL"])
conn = psycopg2.connect(
    database=url.path[1:],
    user=url.username,
    password=url.password,
    host=url.hostname,
    port=url.port
)

