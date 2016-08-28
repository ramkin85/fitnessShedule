from migrate.versioning import api
from app import app
from config import SQLALCHEMY_DATABASE_URI
from config import SQLALCHEMY_MIGRATE_REPO
from app import db
import os.path


def create_db():
    v = api.db_version(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
    app.logger.debug('v is None = %s' % v is None)
    if v is None:
        db.create_all()
        if not os.path.exists(SQLALCHEMY_MIGRATE_REPO):
            api.create(SQLALCHEMY_MIGRATE_REPO, 'database repository')
            api.version_control(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
        else:
            api.version_control(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO, api.version(SQLALCHEMY_MIGRATE_REPO))
    app.logger.debug('DB CREATED')