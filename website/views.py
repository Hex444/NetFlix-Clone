from flask import Blueprint, render_template

views = Blueprint('views' ,__name__)

@views.route('/')
def home():
    return render_template('home.html')

@views.route('/welcome')
def welcome():
    return render_template('welcome.html')