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
from flask_mail import Mail
from flask_dance.contrib.github import make_github_blueprint, github
from flask_migrate import Migrate
import flask_sijax
# environmental config import
from decouple import config
# concurrency control import
from concurrent.futures import ThreadPoolExecutor
# log import
import logging
import logging.config
# python import
import os
# ///////////////////////////////////////////////////////////////////////////


def create_app():
    # initialize flask app
    app = Flask(__name__)

    # load app configuration
    configure_app(app)

    # mail initialization
    mail = Mail(app)

    # database initialization
    db = SQLAlchemy(app)
    db.create_all()
    migrate = Migrate(app, db)

    # concurrency control (Threadpool)
    pool = ThreadPoolExecutor(max_workers=10)

    return app, mail, db, migrate, pool

def configure_app(app):
    # app cache config
    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = -1        #debug(disable cache)
    # app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 43200     #deploy(12 hours cache)

    # mail configuration
    app.config['MAIL_SERVER'] = config('email_server', '')
    app.config['MAIL_PORT'] = config('email_port', '')
    app.config['MAIL_USE_SSL'] = True
    app.config['MAIL_USERNAME'] = config('email_username', '')
    app.config['MAIL_PASSWORD'] = config('email_password', '')
    app.config['SECRET_KEY'] = config('secret_key', '')
    app.config['SECURITY_PASSWORD_SALT'] = config('security_password_salt', '')

    # database configuration
    app.config['SQLALCHEMY_DATABASE_URI'] = config('database_uri', '')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # save uploaded files configuration
    app.config['UPLOAD_FOLDER'] = os.path.join('.', os.path.dirname(__file__), 
                                               config('upload_folder', ''))

    # sijax configuration
    # path = os.path.join('.', os.path.dirname(__file__), 'static/js/sijax/')
    # app.config['SIJAX_STATIC_PATH'] = path
    # app.config['SIJAX_JSON_URI'] = '/static/js/sijax/json2.js'
    # flask_sijax.Sijax(app)

    # github oauth configuration
    github_blueprint = make_github_blueprint(client_id=config('github_client_id', ''), 
                                            client_secret=config('github_client_secret', ''))
    app.register_blueprint(github_blueprint)

# create logger
logger = logging.getLogger(__name__)

# create an instance of the app
# along with the mail, db, and pool
app, mail, db, migrate, pool = create_app()

import application.views
