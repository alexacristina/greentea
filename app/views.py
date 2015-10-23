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
<<<<<<< HEAD
=======

>>>>>>> a5af85a1b68e9554a9df3a4efaa05635b852f070

@app.route('/signup', methods = ['GET', 'POST'])
def signup():
	signup_form = SignupForm(request.form)
	login_form = LoginForm(request.form)
	if signup_form.validate_on_submit():
		return redirect(url_for('lessons'))
	return render_template('signup.html', signup_form=signup_form, login_form=login_form)

@app.route('/lessons')
def lessons():
<<<<<<< HEAD
	return render_template('lessons.html')

=======
	return render_template('dashboard.html')
>>>>>>> a5af85a1b68e9554a9df3a4efaa05635b852f070


