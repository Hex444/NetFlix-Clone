import email
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,EmailField
from wtforms.validators import Length, InputRequired, ValidationError, EqualTo, Email
from .models import User


class RegistrationForm(FlaskForm):
    username = StringField('username' ,
                            validators=[InputRequired(), Length(min=1, max=20)], 
                            render_kw={'placeholder':'Enter your username'})
    email = EmailField('email', 
                        validators=[InputRequired(), Email()],
                        render_kw={'placeholder':'example@domain.com'})
    password = PasswordField('password' ,
                            validators=[InputRequired(), Length(min=8, max=50)],
                            render_kw={'placeholder':'Enter a secure password'})
    confirm_password = PasswordField('confirm password' ,
                            validators=[InputRequired(), Length(min=8, max=50), EqualTo('password')],
                            render_kw={'placeholder':'Enter a secure password'})
    submit = SubmitField('Sign Up')
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username is Taken please choose a different one')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('email is Taken please choose a different one')


class LoginForm(FlaskForm):
    email = EmailField('email',
                        validators=[InputRequired(), Email()],
                        render_kw={"placeholder":"Enter your email"})
    
    password = PasswordField('password',
                        validators=[InputRequired(), Length(min=8,max=50)],
                        render_kw={"placeholder":"Enter your email"})

    submit = SubmitField('Sign Up')


    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if not user:
            raise ValidationError('There is no account with that email, please try a different one')