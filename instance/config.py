import os

basedir = os.path.abspath(os.path.dirname(__file__))
print basedir
DEBUG = True

SQLALCHEMY_DATABASE_URI = "sqlite:////tmp/app.db"
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository	')




