from flask import Blueprint, render_template,redirect,url_for
from . import db,bcrypt
from .forms import RegistrationForm
from .models import User

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
    return render_template('login.html')