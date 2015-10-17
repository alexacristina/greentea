from app import app, login_manager
from flask.ext.login import login_user, login_required, current_user, logout_user
from datetime import datetime
from flask import render_template, redirect, url_for, request, abort, Markup
from app.forms import SignupForm, LoginForm
from app import db
from app.models import User
from sqlalchemy import desc
from werkzeug.security import generate_password_hashe

@app.route('/')
def index():
	return render_template('base.html')

@app.route('/signup')
def signup():
	return render_template('signup.html')