# ///////////////////////////////////////////////////////////////////////////
# @file: email.py
# @time: 2022/07/15
# @author: Yuelin Xin
# @email: yuelinxin@miraclefactory.ai
# @organisation: Miracle Factory
# @url: https://miraclefactory.ai
# ///////////////////////////////////////////////////////////////////////////

# ///////////////////////////////////////////////////////////////////////////
# flask import
from itsdangerous import URLSafeTimedSerializer
from flask import render_template
from flask_mail import Message
# module import
from application import app, mail, pool
# config import
from decouple import config
# time import
import datetime
# ///////////////////////////////////////////////////////////////////////////


# generate email
def send_email(user, email, type):
    # send confirmation email
    token = generate_confirmation_token(email)
    email_link = config('email_prefix', '')+'confirm/'+token+'/'+type
    msg = Message('Email Verification <noreply>', \
                  sender=('Miracle Factory', app.config["MAIL_USERNAME"]), \
                  recipients=[email])
    msg.html = render_template('emails/confirmation.html', name = user, link = email_link)
    try:
        pool.submit(send_async_email, app, msg)
        return True
    except Exception as e:
        print(e)
        return False

def send_change_email(user, email, type):
    # send confirmation email
    token = generate_confirmation_token(email)
    email_link = config('email_prefix', '')+'confirm/'+token+'/'+type
    msg = Message('Email Verification <noreply>', \
                  sender=('Miracle Factory', app.config["MAIL_USERNAME"]), \
                  recipients=[email])
    msg.html = render_template('emails/change-confirmation.html', name = user, link = email_link)
    try:
        pool.submit(send_async_email, app, msg)
        return True
    except Exception as e:
        print(e)
        return False

# generate and send approval email
def send_approved_email(user, email):
    msg = Message('Congratulations! <needaction>', \
                  sender=('Miracle Factory', app.config["MAIL_USERNAME"]), \
                  recipients=[email])
    msg.html = render_template('emails/approved.html', name = user, time = datetime.datetime.now())
    try:
        pool.submit(send_async_email, app, msg)
        return True
    except Exception as e:
        print(e)
        return False

# generate token
def generate_confirmation_token(email):
    serializer = URLSafeTimedSerializer(app.config["SECRET_KEY"])
    return serializer.dumps(email, app.config["SECURITY_PASSWORD_SALT"])

# check token (validation integrity and expiration)
def confirm_token(token, expiration=3600):
    serializer = URLSafeTimedSerializer(app.config["SECRET_KEY"])
    try:
        email = serializer.loads(
            token,
            salt=app.config['SECURITY_PASSWORD_SALT'],
            max_age=expiration  # expires in 1 hour
        )
    except:
        return False
    return email

# send email (asynchronous)
def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)
