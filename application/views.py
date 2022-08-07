# ///////////////////////////////////////////////////////////////////////////
# @file: views.py
# @time: 2022/07/15
# @author: Yuelin Xin
# @email: yuelinxin@miraclefactory.co
# @organisation: Miracle Factory
# @url: https://miraclefactory.co
# ///////////////////////////////////////////////////////////////////////////

# ///////////////////////////////////////////////////////////////////////////
# flask import
from flask import redirect, render_template, url_for, request
# enviromental config import
from decouple import config
# module import
from application import app
from application.email import send_email, confirm_token
from application.contacts import contacts
# ///////////////////////////////////////////////////////////////////////////


# render default index.html
@app.route('/')
def index():
    return render_template('index.html')

# render temp
@app.route('/temp')
def temp():
    return render_template('central-content.html',
                           page_title = 'Coming Soon',
                           headline = 'Coming Soon 😊',
                           message = 'We are doing our best to make this content available to you ASAP.',
                           button_text = 'Back')

# the url for joining
@app.route('/join', methods=['POST', 'GET'])
def join():
    user = request.form['name']
    email = request.form['email']
    type = 'join'
    message = request.form['message']
    email2 = request.form['email2']
    if email2:
        return 'spam'
    else:
        contact = contacts(user, email, type, message)
        contact.add_contact()
        return redirect(url_for('verification', user = user, email = email))

# the url for contact
@app.route('/contact', methods=['POST', 'GET'])
def contact():
    user = request.form['name']
    email = request.form['email']
    type = 'contact'
    message = request.form['message']
    email2 = request.form['email2']
    if email2:
        return 'spam'
    else:
        contact = contacts(user, email, type, message)
        contact.add_contact()
        return redirect(url_for('verification', user = user, email = email))

# send email and render verification.html if the user info is successfully processed
@app.route('/verification/name=<user>_email=<email>')
def verification(user, email):
    # generate and send email
    send_email(user, email)
    # render verification.html
    return render_template('central-content.html',
                           page_title = 'Email Verification', 
                           headline = f'Thank you {user}, just one more step to go 😊',
                           message = 'We have sent you an confirmation email. Please check your inbox.',
                           button_text = 'Back')

# the confirmation url
@app.route('/confirm/<token>')
def confirm_email(token):
    email = confirm_token(token)
    if email:
        # activate the contact
        contact = contacts.query.filter_by(email = email).first()
        contact.activate_contact()
        return render_template('central-content.html',
                               page_title = 'Success!',
                               headline = 'Success! Your message has been received ☑️',
                               message = 'We will get in touch with you as soon as possible. You can close this page now.',
                               button_text = 'Close')
    else:
        return render_template('central-content.html',
                               page_title = 'Oops!', 
                               headline = 'Sorry, your link seems to be invalid or expired 😢',
                               message = 'We apologise for the inconvenience. Please try to send your message again.',
                               button_text = 'Try again')

# the database portal
@app.route('/database/authorization-code=<code>')
def database(code):
    if code == config('auth_1') or code == config('auth_2') or code == config('auth_3'):
        info = contacts.query.all()
        return render_template('database.html', contacts = info)
    else:
        return render_template('central-content.html', 
                               page_title = '401 Unauthorized', 
                               headline = '401 Unauthorized ❌',
                               message = 'Sorry, you are not authorized to access this page.',
                               button_text = 'Home')

# end database session
@app.route('/database/end-session')
def end_session():
    return render_template('central-content.html',
                           page_title = 'Database Session Terminated',
                           headline = 'Your database session is terminated',
                           message = 'You can close this page now.',
                           button_text = 'Home')
