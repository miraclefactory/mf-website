# ///////////////////////////////////////////////////////////////////////////
# @file: __init__.py
# @time: 2022/07/15
# @author: Yuelin Xin
# @email: yuelinxin@miraclefactory.ai
# @organisation: Miracle Factory
# @url: https://miraclefactory.ai
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
from logs.config import log_config
# python import
import os
# ///////////////////////////////////////////////////////////////////////////


def create_app():
    logger.debug('initializing app...')
    # initialize flask app
    app = Flask(__name__)

    logger.debug('loading app configuration...')
    # load app configuration
    configure_app(app)

    # mail initialization
    mail = Mail(app)

    # database initialization
    db = SQLAlchemy(app)
    migrate = Migrate(app, db)

    # concurrency control (Threadpool)
    pool = ThreadPoolExecutor(max_workers=10)

    logger.debug('app initialized')
    return app, mail, db, migrate, pool

def configure_app(app):
    # app cache config
    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = -1        #debug(disable cache)
    # app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 43200     #deploy(12 hours cache)

    # mail configuration
    app.config['MAIL_SERVER'] = config('email_server', 
                                       default=os.environ.get('email_server', ''))
    app.config['MAIL_PORT'] = config('email_port', 
                                     default=os.environ.get('email_port', ''))
    app.config['MAIL_USE_SSL'] = True
    app.config['MAIL_USERNAME'] = config('email_username', 
                                         default=os.environ.get('email_username', ''))
    app.config['MAIL_PASSWORD'] = config('email_password', 
                                         default=os.environ.get('email_password', ''))
    app.config['SECRET_KEY'] = config('secret_key', 
                                      default=os.environ.get('secret_key', ''))
    app.config['SECURITY_PASSWORD_SALT'] = config('security_password_salt', 
                                                  default=os.environ.get('security_password_salt', ''))

    # database configuration
    app.config['SQLALCHEMY_DATABASE_URI'] = config('database_uri', 
                                                   default=os.environ.get('database_uri', ''))
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # save uploaded files configuration
    app.config['UPLOAD_FOLDER'] = os.path.join('.', os.path.dirname(__file__), 
                                               config('upload_folder', default=os.environ.get('upload_folder', '')))

    # sijax configuration
    # path = os.path.join('.', os.path.dirname(__file__), 'static/js/sijax/')
    # app.config['SIJAX_STATIC_PATH'] = path
    # app.config['SIJAX_JSON_URI'] = '/static/js/sijax/json2.js'
    # flask_sijax.Sijax(app)

    # github oauth configuration
    github_blueprint = make_github_blueprint(client_id=config('github_client_id', 
                                                              default=os.environ.get('github_client_id', '')), 
                                             client_secret=config('github_client_secret', 
                                                                  default=os.environ.get('github_client_secret', '')))
    app.register_blueprint(github_blueprint)

    # debug configuration
    app.config['DEBUG'] = True

def init_root(db):
    # from application.user.models import joins, teams
    if joins.query.filter_by(id=1, is_admin=True).first() is None:
        root_user = joins(config('root_user_name', default=os.environ.get('root_user_name', '')), 
                        config('root_user_email', default=os.environ.get('root_user_email', '')), 
                        'join', 
                        config('root_user_password', default=os.environ.get('root_user_password', '')))
        root_user.is_admin = True
        description = 'This is the team made up by all the members of the Miracle Factory community, share your ideas with the other members!'
        root_team = teams(name='Miracle Factory Root', description=description, owner=1)
        root_user.teams.append(root_team)
        db.session.add(root_user, root_team)
        db.session.commit()

# create logger
logger = logging.getLogger(__name__)

# create an instance of the app
# along with the mail, db, and pool
app, mail, db, migrate, pool = create_app()
with app.app_context():
    from application.user.models import *
    db.create_all()

    # initialize root user and root team if not exist
    init_root(db)

import application.views
