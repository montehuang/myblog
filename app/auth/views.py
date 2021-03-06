from flask import render_template, flash, redirect, request, url_for
from flask_login import login_required, login_user, logout_user, current_user
from ..models import User
from .forms import LoginForm, RegisterForm
from . import auth
from .. import db
from ..mail import send_mail


@auth.route('/login', methods = ['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(email=form.email.data).first()
		if user is not None and user.verify_password(form.password.data):
			login_user(user, form.remember.data)
			return redirect(request.args.get('next') or url_for('main.index'))
		flash('Invalid username or password!')
	return render_template('auth/login.html', form=form)

@auth.route('/register', methods = ['GET', 'POST'])
def register():
	form = RegisterForm()
	if form.validate_on_submit():
		user = User(email=form.email.data,
					username=form.username.data,
					password=form.password.data)
		db.session.add(user)
		db.session.commit()
		token = user.generate_confirmation_token()
		send_mail(user.email, 'Confirm your account','auth/email/confirm', user = user, token = token)

		flash('You can login now.')
		return redirect(url_for('auth.login'))
	return render_template('auth/register.html', form=form)
@auth.route('/confirm/<token>', methods = ['GET', 'POST'])
@login_required
def confirm(token):
	if current_user.confirmed:
		return redirect(url_for('main.index'))
	if current_user.confirm(token):
		flash('You have confirmed your account.Thanks')
	else:
		flash('The confirmation link is invalid or has expired.')
	return redirect(url_for('main.index'))

# @auth.before_app_request
# def before_request():
# 	if current_user.is_authenticated:
# 		current_user.ping()
# 		if not current_user.confirmed \
# 			and request.endpoint[:5] != 'auth.' \
# 			and request.endpoint != 'static':
# 			return redirect(url_for('auth.unconfirmed'))

@auth.route('/unconfirmed')
def unconfirmed():
	if current_user.is_anonymous or current_user.confirmed:
		return redirect(url_for('main.index'))
	return render_template('auth/unconfirmed.html')

@auth.route('/confirm')
@login_required
def resend_confirmation():
	token = current_user.generate_confirmation_token()
	send_mail(current_user.email, 'Confirm your Account', 'auth/email/confirm', user = current_user, token = token)
	flash('A new confirmation email has been sent to you by email.')
	return redirect(url_for('main.index'))

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