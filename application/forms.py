# ///////////////////////////////////////////////////////////////////////////
# @file: forms.py
# @time: 2022/12/05
# @author: Yuelin Xin
# @email: yuelinxin@miraclefactory.co
# @organisation: Miracle Factory
# @url: https://miraclefactory.co
# ///////////////////////////////////////////////////////////////////////////

# ///////////////////////////////////////////////////////////////////////////
# flask import
from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed
from wtforms import (StringField, 
                     PasswordField, 
                     BooleanField, 
                     FileField, 
                     EmailField,
                     TextAreaField, 
                     SubmitField)
from wtforms.validators import (ValidationError, 
                                DataRequired, 
                                Email, 
                                Regexp, 
                                EqualTo, 
                                Length,)
# environmental config import
from decouple import config
# module import
from application.user.models import contacts, joins
from re import search
# ///////////////////////////////////////////////////////////////////////////


# class JoinForm(FlaskForm):
#     username = StringField(label=('Username'), 
#         validators=[DataRequired(), 
#         Length(max=64)])
#     email = StringField(label=('Email'), 
#         validators=[DataRequired(), 
#         Email(), 
#         Length(max=120)])
#     password = PasswordField(label=('Password'), 
#         validators=[DataRequired(), 
#         Length(min=8, message='Password should be at least %(min)d characters long')])
#     confirm_password = PasswordField(
#         label=('Confirm Password'), 
#         validators=[DataRequired(message='*Required'),
#         EqualTo('password', message='Both password fields must be equal!')])
#     submit = SubmitField(label=('Submit'))

#     def validate_username(self, username):
#         excluded_chars = " *?!'^+%&/()=}][{$#"
#         for char in username.data:
#             if char in excluded_chars:
#                 raise ValidationError(f"Character {char} is not allowed in username.")


class JoinForm(FlaskForm):
    dialog_join_name = StringField('Name', [
        DataRequired(message="Please enter your name."), 
        Length(min=2, max=50)],
        render_kw={"placeholder": "Your Name"})
    dialog_join_email = EmailField('Email', [
        DataRequired(message="Please enter your email address."),
        Length(min=4, max=50)],
        render_kw={"placeholder": "Your Email", 
                   "type": "email", 
                   "pattern": "[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$"})
                   # requested format: email format
    dialog_join_password = PasswordField('Password', [
        DataRequired(message="Please enter a password."),
        Regexp('^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$', 
               message='Password must be at least 8 characters, 1 uppercase, 1 lowercase, 1 number'),
        Length(min=8, max=50),
        EqualTo('dialog_join_password_confirm', message='Passwords must match')],
        render_kw={"placeholder": "Password", 
                   "class": "input-top-round", 
                   "pattern": "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$"})
    dialog_join_password_confirm = PasswordField('Confirm Password', [
        Length(min=8, max=50),
        Regexp('^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$',
               message='Password must be at least 8 characters, 1 uppercase, 1 lowercase, 1 number'),
        DataRequired(message="Please confirm your password.")],
        render_kw={"placeholder": "Confirm Password", 
                   "class": "input-bottom-round",
                   "pattern": "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$"})
    email1 = StringField('Email1', [Length(min=0, max=50)], render_kw={"class": "hide"})

    def validate_dialog_join_name(form, self):
        excluded_chars = " *?!'^+%&/()=}][{$#"
        for char in form.dialog_join_name.data:
            if char in excluded_chars:
                raise ValidationError(f"Character {char} is not allowed in username.")

    def validate_dialog_join_email(form, self):
        email = joins.query.filter_by(email=form.dialog_join_email.data).first()
        if email is not None:
            raise ValidationError('This email is already registered.')

    def validate_dialog_join_password(form, self):
        # must contain at least 1 uppercase, 1 lowercase, 1 number, at least 8 characters
        password = form.dialog_join_password.data
        password_confirm = form.dialog_join_password_confirm.data
        regex = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$"
        if not search(regex, password):
            raise ValidationError('Password must be at least 8 characters, 1 uppercase, 1 lowercase, 1 number')
        if password != password_confirm:
            raise ValidationError('Passwords must match')


class ContactForm(FlaskForm):
    dialog_contact_name = StringField('Name', [
        DataRequired(message="Please enter your name."),
        Length(min=2, max=50)],
        render_kw={"placeholder": "Your Name"})
    dialog_contact_email = EmailField('Email', [
        DataRequired(message="Please enter your email address."),
        Length(min=4, max=50)],
        render_kw={"placeholder": "Your Email", 
                   "type": "email", 
                   "pattern": "[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$"})
    dialog_contact_message = TextAreaField('Message', [
        DataRequired(message="Please enter a message."),
        Length(min=10, max=500)],
        render_kw={"placeholder": "What do you wish to discuss?"})
    email2 = StringField('Email2', [Length(min=0, max=50)], render_kw={"class": "hide"})


class LoginForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired(), Email(), Length(min=4, max=50)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8, max=50)])


class EditProfileForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = EmailField('Email', validators=[DataRequired(), Email(), Length(min=4, max=50)])
    # old_password = PasswordField('Old Password', validators=[DataRequired(), Length(min=8, max=50)])
    new_password = PasswordField('New Password', validators=[])
    confirm_new_password = PasswordField('Confirm New Password', validators=[])
    avatar = FileField('Update Avatar', validators=[FileAllowed(['jpg', 'jpeg', 'png', 'webp'])])

    def validate_confirm_new_password(form, self):
        # must contain at least 1 uppercase, 1 lowercase, 1 number, at least 8 characters
        password = form.new_password.data
        password_confirm = form.confirm_new_password.data
        if password != "" and password_confirm != "":
            regex = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$"
            if not search(regex, password):
                raise ValidationError('Password must be at least 8 characters, 1 uppercase, 1 lowercase, 1 number')
            if password != password_confirm:
                raise ValidationError('Passwords must match')
        if password != "" and password_confirm == "":
            raise ValidationError('Please confirm your new password')
        if password == "" and password_confirm != "":
            raise ValidationError('Please enter your new password')


class NewProjectForm(FlaskForm):
    name = StringField('Project Name', validators=[DataRequired(), Length(min=2, max=100)])
    url = StringField('Project URL', validators=[DataRequired(), Length(min=2, max=200)])
    description = TextAreaField('Description', validators=[DataRequired(), Length(min=10, max=500)])


class NewTeamForm(FlaskForm):
    name = StringField('Team Name', validators=[DataRequired(), Length(min=2, max=100)])
    description = TextAreaField('Description', validators=[DataRequired(), Length(min=10, max=500)])
