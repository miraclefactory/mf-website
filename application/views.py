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
from flask import (redirect, 
                   render_template, 
                   url_for, 
                   request, 
                   flash, 
                   session, 
                   g)
from flask_dance.contrib.github import github
from werkzeug.security import generate_password_hash
from werkzeug.utils import secure_filename
# environmental config import
from decouple import config
# module import
from application import app
from application.email import (send_email, 
                               confirm_token, 
                               send_change_email, 
                               send_approved_email)
from application.user.models import contacts, joins, projects, teams
from application.forms import (JoinForm, 
                               ContactForm, 
                               LoginForm, 
                               NewProjectForm,
                               NewTeamForm,
                               EditProfileForm)
# python import
import os
import random
import string
import uuid as uuid
import logging
# ///////////////////////////////////////////////////////////////////////////


logger = logging.getLogger(__name__)

# render default index.html
@app.route('/')
def index():
    # check if the user is logged in
    # if g.user:
    #     return redirect(url_for('profile'))
    return render_template('site/index.html')

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
    form = JoinForm()
    if request.method == 'POST' and form.validate():
        user = request.form['dialog_join_name']
        email = request.form['dialog_join_email']
        type = 'join'
        password = request.form['dialog_join_password']
        email1 = request.form['email1']
        if email1:
            return 'spam'
        else:
            join = joins(user, email, type, password)
            join.add_user()
            logger.debug(f'new user {user} added')
            return redirect(url_for('verification', user = user, email = email, type = type))
    return render_template('forms/join.html', form = form)

# the url for contact
@app.route('/contact', methods=['POST', 'GET'])
def contact():
    form = ContactForm()
    if request.method == 'POST' and form.validate():
        user = request.form['dialog_contact_name']
        email = request.form['dialog_contact_email']
        type = 'contact'
        message = request.form['dialog_contact_message']
        email2 = request.form['email2']
        if email2:
            return 'spam'
        else:
            contact = contacts(user, email, type, message)
            contact.add_user()
            logger.debug(f'new contact {user} added')
            return redirect(url_for('verification', user = user, email = email, type = type))
    return render_template('forms/contact.html', form = form)

# send email and render verification.html if the user info is successfully processed
@app.route('/verification/name=<user>_email=<email>_type=<type>')
def verification(user, email, type):
    # generate and send email
    send_email(user, email, type)
    logger.debug(f'verification email sent to {email}')
    # render verification.html
    return render_template('central-content.html',
                           page_title = 'Email Verification', 
                           headline = f'Thank you {user}, just one more step to go 😊',
                           message = 'We have sent you an confirmation email. Please check your inbox.',
                           button_text = 'Back')

# the confirmation url
@app.route('/confirm/<token>/<type>')
def confirm_email(token, type):
    email = confirm_token(token)
    if email:
        logger.debug(f'email confirmed')
        if type == 'join':
            # activate the user
            user = joins.query.filter_by(email = email).first()
            user.activate_user()
            return render_template('central-content.html',
                                   page_title = 'Success!',
                                   headline = 'Success! Your email has been verified ☑️',
                                   message = 'You can close this page now.',
                                   button_text = 'Close')
        elif type == 'contact':
            # activate the user
            user = contacts.query.filter_by(email = email).first()
            user.activate_user()
            return render_template('central-content.html',
                                   page_title = 'Success!',
                                   headline = 'Success! Your message has been received ☑️',
                                   message = 'We will get in touch with you as soon as possible. You can close this page now.',
                                   button_text = 'Close')
        else:
            return render_template('central-content.html',
                                   page_title = 'Oops!', 
                                   headline = 'Sorry, your link seems to be invalid 😢',
                                   message = 'We apologise for the inconvenience. Please try to send your message again.',
                                   button_text = 'Try again')
    else:
        return render_template('central-content.html',
                               page_title = 'Oops!', 
                               headline = 'Sorry, your link seems to be invalid or expired 😢',
                               message = 'We apologise for the inconvenience. Please try to send your message again.',
                               button_text = 'Try again')

# the database portal
@app.route('/database', methods=['POST', 'GET'])
def database():
    if request.method == 'POST':
        # admin_name = request.form['name']
        admin_password = request.form['password']
        if admin_password in config('auth_code'):
            logger.debug(f'admin logged in')
            info = joins.query.all()
            return render_template('database/database.html', contacts = info)
        else:
            return redirect(url_for('database_login'))
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

# database login
@app.route('/database-login')
def database_login():
    return render_template('database/login.html')

# GitHub auth
@app.route('/github-auth')
def github_auth():
    if not github.authorized:
        return redirect(url_for('github.login'))
    else:
        return render_template('central-content.html',
                        page_title = 'Success!',
                        headline = 'You have already authorised with GitHub before ☑️',
                        message = 'You do not need to worry about this as long as your GitHub account is logged in.',
                        button_text = 'Home')

# GitHub auth success
@app.route('/github-auth/success')
def github_auth_success():
    account_info = github.get('/user')
    if account_info.ok:
        account_info_json = account_info.json()
        username = account_info_json['login']
        email = account_info_json['email']
        # generate a random password
        password = generate_password_hash(email)
        type = 'join'
        user = joins(username, email, type, password)
        user.add_user()
        user.activate_user()
        return render_template('central-content.html',
                            page_title = 'Success!',
                            headline = 'You have successfully authorised with GitHub ☑️',
                            message = f'Thank you for taking an interest in our community, {user}.',
                            button_text = 'Home')
    else:
        return render_template('central-content.html',
                            page_title = 'Oops!',
                            headline = 'Sorry, we are unable to retrieve your GitHub account information 😢',
                            message = 'We apologise for the inconvenience. Please try to authorise again later.',
                            button_text = 'Try again')

@app.before_request
def before_request():
    g.user = None
    if 'user' in session:
        user = joins.query.filter_by(id=session['user']).first()
        g.user = user

@app.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit() and request.method == 'POST':
        session.pop('user', None)
        email = form.email.data
        password = form.password.data
        user = joins.query.filter_by(email=email).first()
        if user:
            if user.password == password:
                session['user'] = user.id
                logger.debug(f'{user.name} has logged in')
                return redirect(url_for('profile'))
            else:
                errors = {'Your password is incorrect'}
                return render_template('forms/login.html', form = form, errors = errors)
        else:
            errors = {'This account does not exist'}
            return render_template('forms/login.html', form = form, errors = errors)
    errors = form.errors.values()
    return render_template('forms/login.html', form = form, errors = errors)

@app.route('/profile')
def profile():
    if 'user' in session:
        user = joins.query.filter_by(id=session['user']).first()
        g.user = user
        return render_template('site/profile.html')
    else:
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('user', None)
    logger.debug(f'{g.user.name} has logged out')
    return redirect(url_for('index'))

@app.route('/profile/new-project', methods=['POST', 'GET'])
def new_project():
    if 'user' not in session:
        return redirect(url_for('login'))
    form = NewProjectForm()
    if form.validate_on_submit() and request.method == 'POST':
        name = form.name.data
        description = form.description.data
        url = form.url.data
        owner = g.user
        project = projects(name, description, url, owner.id)
        owner.projects.append(project)
        project.add_project()
        return redirect(url_for('profile'))
    errors = form.errors.values()
    return render_template('forms/new-project.html', form = form, errors = errors)

@app.route('/profile/new-team', methods=['POST', 'GET'])
def new_team():
    if 'user' not in session:
        return redirect(url_for('login'))
    form = NewTeamForm()
    if form.validate_on_submit() and request.method == 'POST':
        name = form.name.data
        description = form.description.data
        owner = g.user
        team = teams(name, description, owner.id)
        owner.teams.append(team)
        team.add_team()
        return redirect(url_for('profile'))
    errors = form.errors.values()
    return render_template('forms/new-team.html', form = form, errors = errors)

@app.route('/profile/edit-profile', methods=['POST', 'GET'])
def edit_profile():
    if 'user' not in session:
        return redirect(url_for('login'))
    form = EditProfileForm()
    if form.validate_on_submit() and request.method == 'POST':
        user = g.user
        if user.name != form.username.data:
            user.name = form.username.data
        if user.email != form.email.data:
            user.email = form.email.data
            user.activated = False
            send_change_email(user.name, user.email, 'join')
        if user.password != form.new_password.data and form.new_password.data != '':
            user.password = form.new_password.data
        if form.avatar.data:
            image = form.avatar.data
            unique_filename = str(uuid.uuid1()) + "_" + secure_filename(image.filename)
            image.save(os.path.join(app.config['UPLOAD_FOLDER'], unique_filename))
            user.avatar = "../" + config('upload_folder') + unique_filename
        try:
            user.update_user_profile(user.name, user.email, user.password, user.avatar)
            return redirect(url_for('profile'))
        except Exception as e:
            errors = {e}
            return render_template('forms/edit-profile.html', form = form, errors = errors)
    errors = form.errors.values()
    return render_template('forms/edit-profile.html', form = form, errors = errors)

@app.route('/profile/save-settings', methods=['POST', 'GET'])
def save_settings():
    if 'user' not in session:
        return redirect(url_for('login'))
    if request.method == 'POST':
        email_feed = False
        public_member = False
        active_contributor = False
        code_reviewer = False
        for item in request.form.keys():
            if item == 'email-feed':
                email_feed = True
            elif item == 'public-member':
                public_member = True
            elif item == 'active-contributor':
                active_contributor = True
            elif item == 'code-reviewer':
                code_reviewer = True
        try:
            g.user.update_user_settings(email_feed, public_member, 
                                        active_contributor, code_reviewer)
        except Exception as e:
            logger.error(f'Failed to update user settings: {e}')
    return redirect(url_for('profile'))

# url for people page
@app.route('/people')
def people():
    info = joins.query.all()
    return render_template('site/people.html', users = info)

# @app.route('/send-email')
# def test_email():
#     # param1 = name, param2 = email
#     send_approved_email('', '')
#     return render_template('central-content.html',
#                            page_title = 'Email Sent',
#                            headline = 'Email Sent',
#                            message = 'You can close this page now.',
#                            button_text = 'Back')
