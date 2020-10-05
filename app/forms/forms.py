from flask_wtf import FlaskForm
from wtforms.validators import InputRequired, ValidationError
from wtforms import StringField, SubmitField, IntegerField, Form, TextField
from app.models.stock_info import StockInfo


def validate_stock_symbol(form, field):
    if field.data.upper() not in [stock['symbol'] for stock in StockInfo().tickers]:
        raise ValidationError(f'Stock "{field.data}" was not found')


def validate_input_isnumeric(form, field):
    try:
        float(field.data)
    except ValueError:
        raise ValidationError(f'Please enter numbers only')


class AddStockForm(FlaskForm):
    stock_symbol = StringField('Stock Symbol',
                               validators=[InputRequired(), validate_stock_symbol])
    purchase_price = StringField('Price at Purchase',
                                 validators=[InputRequired(), validate_input_isnumeric])
    num_of_shares = StringField('Number of Shares',
                                validators=[InputRequired(), validate_input_isnumeric])
    submit = SubmitField('Add Stock')
