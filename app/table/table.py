from flask_table import Table, Col
from app.database.database import StockDb


class StocksTable(Table):
    symbol = Col('Symbol')
    stock_name = Col('Stock')
    quantity = Col('Quantity')
    value = Col('value')
    profit = Col('Profit')
    change = Col('Change from buy')


class Stock:
    def __init__(self, symbol, stock_name, quantity, value, profit, change):
        self.symbol = symbol
        self.stock_name = stock_name
        self.quantity = quantity
        self.value = value
        self.profit = profit
        self.change = change


stocks = StockDb.query.all()

# [Stock symbol: FB, Shares: 2.0, Purchase price: 324.0, Stock symbol: NVDA, Shares: 1.0, Purchase price: 51.0]
