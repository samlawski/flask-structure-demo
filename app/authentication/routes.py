from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_user, logout_user
from app.authentication.helpers.forms import LoginForm, RegisterForm
from app.authentication.models import User

blueprint = Blueprint('authentication', __name__)

@blueprint.route('/login', methods=['GET', 'POST'])
def login():
  form = LoginForm()

  if form.validate_on_submit():
    user = User.query.filter_by(email=form.email.data).first()

    if user and user.check_password(form.password.data):
      login_user(user)
      return redirect(url_for('simple_pages.index'))

  return render_template('authentication/login.html', form=form)

@blueprint.route('/logout')
def logout():
  logout_user()
  return redirect(url_for('authentication.login'))


@blueprint.route('/register', methods=['GET', 'POST'])
def register():
  form = RegisterForm()

  if form.validate_on_submit():
    user = User(email=form.email.data, password=form.password.data)
    user.save()

    login_user(user)
    return redirect(url_for('simple_pages.index'))

  return render_template('authentication/register.html', form=form)