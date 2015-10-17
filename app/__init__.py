from flask import Flask
from flask.ext.bootstrap import Bootstrap
from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand
from flask.ext.sqlalchemy import SQLAlchemy 
from flask.ext.login import LoginManager

app = Flask(__name__)
app.secret_key = "secret"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/diana/projects/greentea/app.db'
app.config['DEBUG'] = True

db = SQLAlchemy(app)
migrate = Migrate(app, db)
login_manager= LoginManager(app)
login_manager.init_app(app)
manager =  Manager(app)
manager.add_command('db', MigrateCommand)

Bootstrap(app)
from app import views, models