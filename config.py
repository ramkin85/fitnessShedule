from sqlalchemy.ext.instrumentation import _ClassInstrumentationAdapter

CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

import os

basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'postgres://mjkygbnmjuuias:Z8rz36fVR8hbffCJZ2XoeQ1Vv4@ec2-54-235-182-120.compute-1.amazonaws.com:5432/d5j7v7k1q22ap1'
# SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SQLALCHEMY_TRACK_MODIFICATIONS = False

# mail server settings
MAIL_SERVER = 'smtp.googlemail.com'
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_USERNAME = 'ramkin85@gmail.com'
MAIL_PASSWORD = 'NM@rkel0v'

# administrator list
ADMINS = ['ramkin85@gmail.com', 'ramkin85@yandex.ru']

# serach
MAX_SEARCH_RESULT = 50
WHOOSH_BASE = os.path.join(basedir, 'search.db')
