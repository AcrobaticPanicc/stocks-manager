import requests
import json
from app.models.stock import Stock
from app.forms.forms import AddStockForm
from app.database.database import StockDb
from app import db, oidc, app, okta_client
from flask import Blueprint, render_template, request, redirect, url_for, flash, g, Response

stocks_blueprint = Blueprint('stocks', __name__)


@app.before_request
def before_request():
    if oidc.user_loggedin:
        g.user = okta_client.get_user(oidc.user_getfield("sub"))

    else:
        g.user = None


@stocks_blueprint.route('/main', methods=['GET', 'POST'])
@oidc.require_login
def main():
    stocks = StockDb.query.all()
    total = Stock.get_total(stocks)
    form = AddStockForm()

    if request.method == 'POST' and form.validate_on_submit():
        stock_symbol = request.form['stock_symbol']
        num_of_shares = request.form['num_of_shares']
        purchase_price = request.form['purchase_price']

        stock = Stock(stock_symbol, num_of_shares, purchase_price)
        info = stock.stock_data

        stock = StockDb(
            id=info['_id'],
            full_name=info['full_name'],
            stock_symbol=info['stock_symbol'],
            shares=info['shares'],
            purchase_price=info['purchase_price'],
            net_buy_price=info['net_buy_price'],
            logo=info['logo']
        )

        db.create_all()
        db.session.add(stock)
        db.session.commit()

        flash(f'{stock_symbol.upper()} stock was added successfully', 'alert-success')
        return redirect(url_for('stocks.main'))

    return render_template('stocks/table.html', stocks=stocks, Stock=Stock, total=total, form=form)


@stocks_blueprint.route('/login', methods=['GET', 'POST'])
@oidc.require_login
def login():
    return redirect(url_for('stocks.main'))


@stocks_blueprint.route('/register', methods=['GET', 'POST'])
@oidc.require_login
def register():
    return redirect(url_for('stocks.index'))


@stocks_blueprint.route('/remove_stock', methods=['POST'])
def remove_stock():
    if request.method == 'POST':
        stock_id = request.form['stock_id']
        StockDb.query.filter_by(id=stock_id).delete()
        db.session.commit()
        return redirect(url_for('stocks.main'))


@stocks_blueprint.route('/logout', methods=['POST', 'GET'])
def logout():
    oidc.logout()
    return redirect(url_for('stocks.index'))


@app.route('/')
def base():
    return redirect("/stocks/main", code=302)


@stocks_blueprint.route('/index', methods=['POST', 'GET'])
def index():
    return render_template('stocks/index.html')
