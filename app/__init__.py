import os
from flask import Flask
from okta import UsersClient
from flask_bcrypt import Bcrypt
from flask_oidc import OpenIDConnect
from flask_sqlalchemy import SQLAlchemy
from oauth2client.client import OAuth2Credentials


app = Flask(__name__)

app.config['SECRET_KEY'] = '6c9a0af7a220762b3ec7d435b3ff14a4'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.database'

SQLALCHEMY_DATABASE_URI = os.environ.get(
    "DATABASE_URI", 'sqlite:///site.database'
)

app.config["OIDC_CLIENT_SECRETS"] = "client_secrets.json"
app.config["OIDC_COOKIE_SECURE"] = False
app.config["OIDC_CALLBACK_ROUTE"] = "/oidc/callback"
app.config["OIDC_SCOPES"] = ["openid", "email", "profile"]
app.config["OIDC_ID_TOKEN_COOKIE_NAME"] = "oidc_token"
app.config["SECRET_KEY"] = "xe5zbyscaf1vr4325KIdzBrRCGKf4htsnjxX_g8R3B"
app.config["OIDC_ID_TOKEN_COOKIE_SECURE"] = False

oidc = OpenIDConnect(app)
okta_client = UsersClient("https://dev-770962.okta.com", "00cHd49AKtn3S0qjQDy8UR9R_7ycPgffTDvt0UhvNN")
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
