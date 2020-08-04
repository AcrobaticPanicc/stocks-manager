from app import bcrypt, db
from app.database.database import User
from app.models.stock import Stock
from app.forms.forms import RegistrationsForm, AddStockForm, LoginForm, RequestResetForm, ResetPasswordForm
from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, current_user
from app.database.database import StockDb

stocks_blueprint = Blueprint('stocks', __name__)


@stocks_blueprint.route('/table', methods=['GET', 'POST'])
def table():
    stocks = StockDb.query.all()
    total = Stock.get_total(stocks)
    form = AddStockForm()

    if request.method == 'POST':
        stock_symbol = request.form['stock_symbol']
        num_of_shares = request.form['num_of_shares']
        purchase_price = request.form['purchase_price']

        stock = Stock(stock_symbol, num_of_shares, purchase_price)
        info = stock.get_stock_data()

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
        return redirect(url_for('stocks.table'))

    return render_template('stocks/table.html', stocks=stocks, Stock=Stock, total=total, form=form)


@stocks_blueprint.route('/remove_stock', methods=['POST'])
def remove_stock():
    if request.method == 'POST':
        stock_id = request.form['stock_id']
        StockDb.query.filter_by(id=stock_id).delete()
        db.session.commit()
        return redirect(url_for('stocks.table'))


@stocks_blueprint.route('/register', methods=['POST', 'GET'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('stocks.index'))
    form = RegistrationsForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(request.form['password']).decode('utf-8')
        email = request.form['email']
        user = User(email=form.email.data, password=hashed_password)
        db.create_all()
        db.session.add(user)
        db.session.commit()

        flash('Account created, you can log in now', 'alert-success')
        return redirect(url_for('stocks.login'))
    else:
        return render_template('stocks/register.html', form=form)


@stocks_blueprint.route('/login', methods=['POST', 'GET'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('stocks.index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            flash('Logged in successfully', 'alert-success')
            return redirect(url_for('stocks.index'))
        else:
            flash('Log in failed, check your email or password', 'alert-danger')

    return render_template('stocks/login.html', form=form)


@stocks_blueprint.route('/about', methods=['POST', 'GET'])
def about():
    return render_template('stocks/about.html')


@stocks_blueprint.route('/index', methods=['POST', 'GET'])
def index():
    return render_template('stocks/index.html')


@stocks_blueprint.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('stocks.index'))


@stocks_blueprint.route('/reset_password', methods=['POST', 'GET'])
def reset_request():
    form = RequestResetForm()
    return render_template('stocks/reset.html', form=form)
