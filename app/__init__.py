from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app = Flask(__name__)
app.config['SECRET_KEY'] = '6c9a0af7a220762b3ec7d435b3ff14a4'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.database'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
