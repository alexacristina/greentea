from app import db
import datetime
from flask.ext.login import UserMixin


class User(UserMixin, db.Model):
	__tablename__ = 'user'
	id = db.Column(db.Integer, primary_key = True)
	first_name = db.Column(db.String)
	last_name = db.Column(db.String)
	email = db.Column(db.String)
	password = db.Column(db.String)
	about_you = db.Column(db.Text)
	image_url = db.Column(db.String)

	def full_name(self):
		return self.first_name + ' ' + self.last_name


