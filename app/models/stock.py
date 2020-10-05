import uuid
from typing import Dict
from wallstreet import Stock as WS
from app.models.stock_info import StockInfo


class Stock:

    def __init__(self, stock_symbol: str, number_of_shares: float, purchase_price: float, _id: str = None):
        self._id = _id or uuid.uuid4().hex
        self.number_of_shares = number_of_shares
        self.purchase_price = purchase_price
        self.stock_info = StockInfo()
        self.stock_data = self._add_stock(stock_symbol)

    def _add_stock(self, stock_symbol) -> Dict:
        stock_symbol = stock_symbol.upper()
        return dict(
            _id=self._id,
            full_name=self.stock_info.get_full_name(stock_symbol)['company'],
            stock_symbol=stock_symbol,
            shares=float(self.number_of_shares),
            purchase_price=float(self.purchase_price),
            net_buy_price=round(float(self.number_of_shares) * float(self.purchase_price), 2),
            logo=self.stock_info.get_logo_url(stock_symbol)
        )

    @staticmethod
    def get_current_price_by_symbol(stock_symbol) -> float:
        upper_stock_symbol = stock_symbol.upper()
        return WS(upper_stock_symbol).price

    @classmethod
    def get_yield_of_single_stock(cls, stock) -> Dict:
        num_of_shares = stock.shares
        stock_symbol = stock.stock_symbol
        purchase_price = stock.purchase_price
        current_price = cls.get_current_price_by_symbol(stock_symbol)

        profit_in_usd = (current_price - purchase_price) * num_of_shares
        profit_prec = (current_price - purchase_price) / purchase_price * 100
        total_value = num_of_shares * current_price

        return dict(symbol=stock_symbol,
                    profit_in_usd=round(profit_in_usd, 2),
                    profit_prec=round(profit_prec, 2),
                    total_value=round(total_value, 2))

    @classmethod
    def get_total(cls, stocks):
        quantity = 0
        value = 0
        profit_loss = 0

        for stock in stocks:
            stock_yeild = cls.get_yield_of_single_stock(stock)

            quantity += stock.shares
            value += stock_yeild['total_value']
            profit_loss += stock_yeild['profit_in_usd']

        return dict(quantity=round(quantity, 2), value=round(value, 2), profit_loss=round(profit_loss, 2))
