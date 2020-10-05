from app import db


class StockDb(db.Model):
    id = db.Column(db.String(120), primary_key=True)
    full_name = db.Column(db.String(120))
    stock_symbol = db.Column(db.String(120))
    shares = db.Column(db.Float(120))
    purchase_price = db.Column(db.Float(120))
    net_buy_price = db.Column(db.Float(120))
    logo = db.Column(db.String(120))

    def __repr__(self):
        return f'Stock symbol: {self.stock_symbol}, Shares: {self.shares}, Purchase price: {self.purchase_price}'
