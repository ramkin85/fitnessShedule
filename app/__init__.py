import os

from flask import Flask, json
from flask_login import LoginManager
# from flask.ext.login import LoginManager
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from config import basedir, ADMINS, MAIL_SERVER, MAIL_PASSWORD, MAIL_USERNAME, MAIL_PORT
import logging
from app import db_helper

app = Flask(__name__)

app.config.from_object('config')
db = SQLAlchemy(app)

db_helper.create_db(app, db)
# db_helper.upgrade_db(app)

# lm = LoginManager()
# lm.init_app(app)
# lm.login_view = 'login'
mail = Mail(app)
app.debug = True

if not app.debug:
    from logging.handlers import SMTPHandler

    credentials = None
    if MAIL_USERNAME or MAIL_PASSWORD:
        credentials = (MAIL_USERNAME, MAIL_PASSWORD)
    mail_handler = SMTPHandler((MAIL_SERVER, MAIL_PORT), 'no-reply@' + MAIL_SERVER, ADMINS, 'fitnesShedule failure',
                               credentials)
    mail_handler.setLevel(logging.ERROR)
    app.logger.addHandler(mail_handler)
elif app.debug:
    from logging.handlers import RotatingFileHandler

    file_handler = RotatingFileHandler(os.path.join(basedir, 'tmp/fitnesShedule.log'), 'a', 1 * 1024 * 1024, 10)
    file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    app.logger.setLevel(logging.DEBUG)
    file_handler.setLevel(logging.DEBUG)
    app.logger.addHandler(file_handler)
    app.logger.info('fitnesShedule startup')
    app.logger.debug('fitnesShedule DEBUG mode')

# logging.basicConfig(filename=os.path.join(basedir, 'tmp/fitnesShedule.log'), level=logging.DEBUG, format='%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')
# logging.debug('DEBUG ENABLED')

from migrate.versioning import api
from config import SQLALCHEMY_DATABASE_URI
from config import SQLALCHEMY_MIGRATE_REPO

from app import views
