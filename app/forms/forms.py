import csv
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Length, Email, EqualTo, Regexp, InputRequired, ValidationError
from wtforms import StringField, PasswordField, SubmitField, IntegerField, BooleanField
from app.database.database import User
from app.models.stock_info import StockInfo


def validate_stock_symbol(form, field):
    if field.data.upper() not in [stock['symbol'] for stock in StockInfo().tickers]:
        raise ValidationError(f'Stock "{field.data}" was not found')


def validate_input_isnumeric(form, field):
    try:
        int(field.data)
    except TypeError:
        raise ValidationError(f'Please enter numbers only')


class AddStockForm(FlaskForm):
    stock_symbol = StringField('Stock Symbol',
                               validators=[InputRequired(), validate_stock_symbol])
    purchase_price = IntegerField('Price at Purchase',
                                  validators=[InputRequired(), validate_input_isnumeric])
    num_of_shares = IntegerField('Number of Shares',
                                 validators=[InputRequired(), validate_input_isnumeric])
    submit = SubmitField('Add Stock')


class LoginForm(FlaskForm):
    email = StringField('Email*', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class RegistrationsForm(FlaskForm):
    email = StringField('Email*', validators=[DataRequired(), Email()])
    password = PasswordField('Password*', validators=[DataRequired(), Length(min=5, max=20)])
    confirm_password = PasswordField('Confirm password*',
                                     validators=[DataRequired(), Length(min=5, max=20),
                                                 EqualTo('password', message='Passwords must match')])
    submit = SubmitField('Sign Up')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Email already in use')


class RequestResetForm(FlaskForm):
    email = StringField('Email*', validators=[DataRequired(), Email()])
    submit = SubmitField('Request new password')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is None:
            raise ValidationError('There is no account associated with this email address')


class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password*', validators=[DataRequired(), Length(min=5, max=20)])
    confirm_password = PasswordField('Confirm password*',
                                     validators=[DataRequired(), Length(min=5, max=20),
                                                 EqualTo('password', message='Passwords must match')])
    submit = SubmitField('Reset password')
