from flask import Blueprint, render_template,redirect,url_for,flash
from flask_login import login_user, logout_user, login_required,current_user
from . import db,bcrypt
from .forms import RegistrationForm, LoginForm
from .models import User
from .api import MvFm

auth = Blueprint('auth' ,__name__)

@auth.route('/register', methods=['POST','GET'])
def register():
    form=RegistrationForm()
    if form.validate_on_submit():
        hashed_pw = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_pw)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('auth.login'))

    return render_template('signup.html', form=form, title='Register')


@auth.route('/login', methods=['POST','GET'])
def login():
    form=LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            flash(f"your logged in as {user.username} !", category='success')
            return redirect(url_for('views.home'))
        else:
            flash('Password invalid please try again', category='danger')
        

    return render_template('login.html', form=form, title='Login')



@auth.route('/logout', methods=['POST', 'GET'])
@login_required
def logout():
    logout_user()
    flash('logged out!', category='success')
    return redirect(url_for('auth.login'))