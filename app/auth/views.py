from flask import render_template, flash, redirect, request, url_for
from flask_login import login_required, login_user, logout_user
from ..models import User
from .forms import LoginForm
from . import auth


@auth.route('/login', methods = ['GET', 'post'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(email=form.email.data).first()
		if user is not None and user.verify_password(form.password.data):
			login_user(user, form.remember.data)
			return redirect(request.args.get('next') or url_for('main.index'))
		flash('Invalid username or password!')
	return render_template('auth/login.html', form=form)

@auth.route('/secret')
@login_required
def secret():
	return 'Only authenticated users are allowed!'

@auth.route('/logout')
@login_required
def logout():
	logout_user()
	flash('You have been logged out!')
	return redirect(url_for('main.index'))