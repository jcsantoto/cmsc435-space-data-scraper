from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
import flask_app


class RegistrationForm(FlaskForm):
    """A class representing a registration form when a user wants to create an account

    """
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        """

        Args:
            username:

        Returns:
            validation error if the user does not input valid information
        """
        user = flask_app.User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        """

        Args:
            email:

        Returns:
            validation error if the user does not input a valid email
        """
        user = flask_app.User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose a different one.')


class LoginForm(FlaskForm):
    """ A class representing a login submission. If the user has the correct login credentials

    """
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class UpdateAccountForm(FlaskForm):
    """A class representing an update account form. This is to change a users account information
    """
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    biography = StringField('Biography', validators=[Length(max=240)])
    submit = SubmitField('Update')

    def validate_username(self, username):
        """

        Args:
            username:

        Returns:
            validation error when a username was already taken
        """
        if username.data != flask_app.current_user.username:
            user = flask_app.User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        """

        Args:
            email:

        Returns:
            validation error when an email has already been taken
        """
        if email.data != flask_app.current_user.email:
            user = flask_app.User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('That email is taken. Please choose a different one.')