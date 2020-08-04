from app import app
from app.routes.routes import stocks_blueprint

app.register_blueprint(stocks_blueprint, url_prefix='/stocks')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
