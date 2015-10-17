from app import db
from werkzeug.security import generate_password_hash
from flask.ext.login import UserMixin


class User (UserMixin, db.Model):
	__tablename__ = 'user'

	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(64), unique=True, index=True)
	h_password = db.Column(db.String(1000))

	def __init__(self, username):
		self.username = username

	def __repr__(self):
		return '<User %s>' % self.name

	def set_password(self, password):
		self.h_password = generate_password_hash(password=password)
		self.save()
		return True

	def save(self):
		db.session.add(self)
		db.session.commit()

