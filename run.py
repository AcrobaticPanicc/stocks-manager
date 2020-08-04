import os
from app import app
from flask import redirect
from app.routes.routes import stocks_blueprint

app.register_blueprint(stocks_blueprint, url_prefix='/stocks')

@app.route('/')
def base():
    return redirect("/stocks/table", code=302)

production = os.environ.get("PRODUCTION", False)

if __name__ == '__main__':
    if production:
        app.run()
    else:
        app.run(host='127.0.0.1', port=8000, debug=True)
