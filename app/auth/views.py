from flask import  render_template, redirect, request, url_for, flash
from . import auth
from flask.ext.login import login_user,logout_user,login_required
from ..models import User 
from .forms import LoginForm,RegForm
from .. import db
from ..email import send_email
from flask.ext.login import current_user 
@auth.route('/login',methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(email=form.email.data).first()
		if user is not None and user.verify_password(form.password.data):
			login_user(user,form.remember_me.data)
			return redirect(request.args.get('next') or url_for('main.index')) 
		flash('Invalid username or password.')  
	return render_template('auth/login.html',form=form)
@auth.route('/logout')
@login_required
def logout():
	logout_user()
	flash('Logout!')
	return redirect(url_for('main.index'))
@auth.route('/register',methods=['GET','POST'])
def register():
	form = RegForm()
	if form.validate_on_submit():
		user = User(email=form.email.data,username = form.username.data,password=form.password.data)
		db.session.add(user)
		token = user.generate_confirmation_token()
		send_email(user.email,'Confirm Your Account','auth/email/confirm.txt', user=user, token=token)
		flash('A confirmation email has been sent to you by email.')
		db.session.commit()
		return render_template(url_for('atuh.login'))
	return render_template('auth/register.html',form=form)
@auth.route('confirm/<token>')
@login_required
def confirm(token):
	if current_user.confirmed:
		return redirect(url_for('mian.index'))
	if current_user.confirm(token):
		flash('You have confirmed your account. Thanks!') 
	else:
		flash('The confirmation link is invalid or has expired.')
	return redirect(url_for('main.index'))

