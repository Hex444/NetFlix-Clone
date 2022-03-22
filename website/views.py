from flask import Blueprint, redirect, render_template,url_for
from flask_login import login_required,current_user

views = Blueprint('views' ,__name__)

@views.route('/')
def dash():
    if current_user.is_authenticated:
        return redirect(url_for('views.home'))
    return render_template('newuser.html')


@views.route('/home')
@login_required
def home():
    return render_template('home.html')

@views.route('/welcome')
def welcome():
    return render_template('welcome.html')