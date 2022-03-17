from flask import Flask, url_for,redirect,render_template
from os import path
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt


bcrypt = Bcrypt()
# init db
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'asdfasdffasdf'
    # know where it is (same directory)
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///database.db"
    db.init_app(app)
    bcrypt.init_app(app)
    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prfix="/")
    app.register_blueprint(auth, url_prefix="/")

    from .models import User
    create_database(app)
    return app

def create_database(app):
    if not path.exists('website/' + 'database.db'):
        db.create_all(app=app)
        print('Created Database')