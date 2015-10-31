from app import db

from werkzeug.security import generate_password_hash, check_password_hash
from flask.ext.login import UserMixin


class User (UserMixin, db.Model):
	__tablename__ = 'user'

	id = db.Column(db.Integer, primary_key = True)
	first_name = db.Column(db.String)
	last_name = db.Column(db.String)
	email = db.Column(db.String, unique=True, index=True)
	h_password = db.Column(db.String(1000))
	image_url = db.Column(db.String)
	school = db.Column(db.String(60), default="")
	class_year = db.Column(db.String(10), default="")
	game_points = db.relationship("Lesson", secondary='achievements' )


	def full_name(self):
		return self.first_name + ' ' + self.last_name

	def __repr__(self):
		return '<User %s>' % self.email

	def __init__(self, first_name, last_name, email, image_url):
		self.first_name = first_name
		self.last_name = last_name
		self.email = email
		self.image_url = image_url


	def set_password(self, password):
		self.h_password = generate_password_hash(password=password)
		self.save()
		return True

	def check_password(self, password):
		return check_password_hash(self.h_password, password)

	def save(self):
		db.session.add(self)
		db.session.commit()

class Lesson(db.Model):
	__tablename__ = 'lesson'

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(64), unique=True, index=True)
	problem_description = db.Column(db.String(1000))
	theory = db.Column(db.String(1000))
	game_points = db.Column(db.Integer(), default=0)
	user = db.relationship(User, secondary='achievements', )


	def __init__(self, name, problem_description, theory):
		self.name = name
		self.problem_description = problem_description
		self.theory = theory

	def save(self):
		db.session.add(self)
		db.session.commit()

class Achievements(db.Model):
	__tablename__ = 'achievements'

	user_id = db.Column(db.Integer, db.ForeignKey("user.id"), primary_key=True)
	lesson_id = db.Column(db.Integer, db.ForeignKey("lesson.id"), primary_key=True)
	total_points = db.Column(db.Integer)
	user = db.relationship(User, backref=db.backref("user_assoc"))
	lesson = db.relationship(Lesson, backref=db.backref("lesson_assoc"))




