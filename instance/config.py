import os

basedir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
print basedir
DEBUG = True

SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, 'data.sqlite')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository	')




