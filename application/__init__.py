# ///////////////////////////////////////////////////////////////////////////
# @file: __init__.py
# @time: 2022/07/15
# @author: Yuelin Xin
# @email: yuelinxin@miraclefactory.co
# @organisation: Miracle Factory
# @url: https://miraclefactory.co
# ///////////////////////////////////////////////////////////////////////////

# ///////////////////////////////////////////////////////////////////////////
# flask import
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from concurrent.futures import ThreadPoolExecutor
from flask_mail import Mail
# enviromental config import
from decouple import config
# ///////////////////////////////////////////////////////////////////////////


# initialize flask app
app = Flask(__name__)

# app cache config
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = -1        #debug(disable cache)
# app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 43200     #deploy(12 hours cache)

# mail configuration and initialization
app.config['MAIL_SERVER'] = config('email_server', '')
app.config['MAIL_PORT'] = config('email_port', '')
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = config('email_username', '')
app.config['MAIL_PASSWORD'] = config('email_password', '')
app.config['SECRET_KEY'] = config('secret_key', '')
app.config['SECURITY_PASSWORD_SALT'] = config('security_password_salt', '')
mail = Mail(app)

# database configuration and initialization
app.config['SQLALCHEMY_DATABASE_URI'] = config('database_uri', '')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
db.create_all()

# concurrency control (Threadpool)
pool = ThreadPoolExecutor(max_workers=10)

import application.views
