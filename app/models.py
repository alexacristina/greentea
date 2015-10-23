from app import db

from werkzeug.security import generate_password_hash
from flask.ext.login import UserMixin


class User (UserMixin, db.Model):
	__tablename__ = 'user'

	id = db.Column(db.Integer, primary_key = True)
	first_name = db.Column(db.String)
	last_name = db.Column(db.String)
	email = db.Column(db.String, unique=True, index=True)
	h_password = db.Column(db.String(1000))
	image_url = db.Column(db.String)

	def full_name(self):
		return self.first_name + ' ' + self.last_name

	def __init__(self, username):
		self.username = username

	def __repr__(self):
		return '<User %s>' % full_name(self)

	def set_password(self, password):
		self.h_password = generate_password_hash(password=password)
		self.save()
		return True

	def save(self):
		db.session.add(self)
		db.session.commit()


