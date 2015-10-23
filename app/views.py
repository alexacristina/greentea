from app import app, login_manager
from flask.ext.login import login_user, login_required, current_user, logout_user
from datetime import datetime
from flask import render_template, redirect, url_for, request, abort, Markup
from app.forms import SignupForm, LoginForm
from app import db
from app.models import User
from sqlalchemy import desc
from werkzeug.security import generate_password_hash


@app.route('/')
def index():
	return render_template('index.html')


@app.route('/signup', methods = ['GET', 'POST'])
def signup():
	form = LoginForm()
	signup_form = SignupForm()
	if signup_form.validate_on_submit():
		user = User(first_name=signup_form.first_name.data, last_name=signup_form.last_name.data, \
			email=signup_form.email.data, image_url=signup_form.image_url.data)
		user.save()
		user.set_password(password=signup_form.password.data)
		
		return redirect(url_for('lessons'))
	return render_template('signup.html', signup_form=signup_form, login_form=form)


@app.route('/lessons')
def lessons():
	return render_template('dashboard.html')


