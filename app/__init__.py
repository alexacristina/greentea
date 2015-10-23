from flask import Flask, request
from flask.ext.bootstrap import Bootstrap
from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand
from flask.ext.sqlalchemy import SQLAlchemy 
from flask.ext.login import LoginManager
from flask_wtf.csrf import CsrfProtect

app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('config.py')
app.secret_key = "secret"	

CsrfProtect(app)

db = SQLAlchemy(app)

login_manager= LoginManager(app)


Bootstrap(app)

from app import views, models

