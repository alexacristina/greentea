from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand
from flask_wtf.csrf import CsrfProtect


from app import app, db

CsrfProtect(app)
	
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == "__main__":
	manager.run()