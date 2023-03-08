from flask import Blueprint

from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, logout_user, current_user
from .forms import RegistrationForm, LoginForm
from .models import User
from utils.database import db
from werkzeug.urls import url_parse

auth = Blueprint("auth", __name__, template_folder="templates")


@auth.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('task.tasks'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data.lower(), email=form.email.data.lower())
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('auth.login'))
    return render_template('register.html', title='Register', form=form)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    nologin = False
    if current_user.is_authenticated:
        return redirect(url_for('task.tasks'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data.lower()).first()
        if user is None or not user.check_password(form.password.data):
            nologin = True
        else:
            login_user(user, remember=form.remember_me.data)
            next_page = request.args.get('next')
            if not next_page or url_parse(next_page).netloc != '':
                next_page = url_for('task.tasks')
            return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form, message=nologin)


@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('core.index'))
