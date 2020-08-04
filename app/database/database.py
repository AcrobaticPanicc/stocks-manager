from app import db, login_manager, app
from flask_login import UserMixin
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

    def get_reset_token(self, expires_sec=1800):
        s = Serializer(app.config['SECRET_KEY'], expires_sec)
        return s.dumps({'user_id': self.id}).decode('utf-8')

    @staticmethod
    def verify_reset_token(token):
        s = Serializer(app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)

    def __repr__(self):
        return f"User('{self.email}')"


class StockDb(db.Model):
    id = db.Column(db.String(120), primary_key=True)
    full_name = db.Column(db.String(120))
    stock_symbol = db.Column(db.String(120))
    shares = db.Column(db.Float(120))
    purchase_price = db.Column(db.Float(120))
    net_buy_price = db.Column(db.Float(120))
    logo = db.Column(db.String(120))

    # def __repr__(self):
    #     return f'Stock symbol: {self.stock_symbol}, Shares: {self.shares}, Purchase price: {self.purchase_price}'
