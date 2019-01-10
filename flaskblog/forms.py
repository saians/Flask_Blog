from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flaskblog.models import User


class RegistrationForm(FlaskForm):
    username = StringField('username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('email',
                        validators=[DataRequired(), Email()])

    password = PasswordField('password',
                             validators=[DataRequired()])
    confirm_password = PasswordField('confirm password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken, please choose another one.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken, please choose another one.')


class LoginForm(FlaskForm):
    email = StringField('email',
                        validators=[DataRequired(), Email()])

    password = PasswordField('password',
                             validators=[DataRequired()])
    remember = BooleanField('Remember Me')

    submit = SubmitField('Login');


class UpdateAccountForm(FlaskForm):
    username = StringField('username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('email',
                        validators=[DataRequired(), Email()])

    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])

    submit = SubmitField('Update')

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('That username is taken, please choose another one.')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('That email is taken, please choose another one.')
