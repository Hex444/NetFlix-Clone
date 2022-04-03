from flask import Blueprint, redirect, render_template,url_for
from flask_login import login_required,current_user
from .api import MvFm

views = Blueprint('views' ,__name__)
api = MvFm()
poster_path = "https://image.tmdb.org/t/p/original/"

@views.route('/')
def dash():
    if current_user.is_authenticated:
        return redirect(url_for('views.home'))
    return render_template('newuser.html', title='new user')


@views.route('/home')
@login_required
def home():
    return render_template('home.html', api=api, poster_path=poster_path, title='home')

@views.route('/welcome')
def welcome():
    return render_template('welcome.html', title='welcome')
