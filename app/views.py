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
	return render_template('no-jquery.html')

@app.route('/signup', methods = ['GET', 'POST'])
def signup():
	signup_form = SignupForm(request.form)
	login_form = LoginForm(request.form)
	if signup_form.validate_on_submit():
		return redirect(url_for('lessons'))
	return render_template('signup.html', signup_form=signup_form, login_form=login_form)

@app.route('/lessons')
def lessons():
	return render_template('lessons.html')



