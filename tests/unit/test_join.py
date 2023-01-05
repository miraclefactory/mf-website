from flask import Flask
from application import create_app
from application import app, db
from application.user.models import joins

app.config['WTF_CSRF_ENABLED'] = False

def test_join_page():
    client = app.test_client()
    response = client.get('/join')
    assert response.status_code == 200
    assert b'Join' in response.data

def test_join_success():
    with app.test_client() as client:
        response = client.post('/join', data=dict(
            dialog_join_name='TestUser',
            dialog_join_email='test@miraclefactory.co',
            dialog_join_password='TestPassword123',
            dialog_join_password_confirm='TestPassword123',
            email1='',
        ), follow_redirects=True)
        assert response.status_code == 200
        assert b'Join' not in response.data
        # revert the database to its original state
        db.session.query(joins).filter(joins.name == 'TestUser').delete()
        db.session.commit()

def test_join_illegal_name():
    with app.test_client() as client:
        response = client.post('/join', data=dict(
            dialog_join_name='a%$&',
            dialog_join_email='test@miraclefactory.co',
            dialog_join_password='TestPassword123',
            dialog_join_password_confirm='TestPassword123',
            email1='',
        ), follow_redirects=True)
        assert response.status_code == 200
        assert b'Character' in response.data

def test_join_illegal_email():
    with app.test_client() as client:
        response = client.post('/join', data=dict(
            dialog_join_name='TestUser',
            dialog_join_email='test',
            dialog_join_password='TestPassword123',
            dialog_join_password_confirm='TestPassword123',
            email1='',
        ), follow_redirects=True)
        assert response.status_code == 200
        assert b'Please enter a valid email address' in response.data

def test_join_duplicate_email():
    with app.test_client() as client:
        response = client.post('/join', data=dict(
            dialog_join_name='TestUser',
            dialog_join_email='yuelinxin@miraclefactory.co',
            dialog_join_password='TestPassword123',
            dialog_join_password_confirm='TestPassword123',
            email1='',
        ), follow_redirects=True)
        assert response.status_code == 200
        assert b'This email is already registered' in response.data

def test_join_illegal_password():
    with app.test_client() as client:
        response = client.post('/join', data=dict(
            dialog_join_name='TestUser',
            dialog_join_email='test@miraclefactory.co',
            dialog_join_password='test',
            dialog_join_password_confirm='test',
            email1='',
        ), follow_redirects=True)
        assert response.status_code == 200
        assert b'Password must be at least 8 characters' in response.data

def test_join_password_mismatch():
    with app.test_client() as client:
        response = client.post('/join', data=dict(
            dialog_join_name='TestUser',
            dialog_join_email='test@miraclefactory.co',
            dialog_join_password='TestPassword123',
            dialog_join_password_confirm='TestPassword1234',
            email1='',
        ), follow_redirects=True)
        assert response.status_code == 200
        assert b'Passwords must match' in response.data

def test_join_no_confirmation_password():
    with app.test_client() as client:
        response = client.post('/join', data=dict(
            dialog_join_name='TestUser',
            dialog_join_email='test@miraclefactory.co',
            dialog_join_password='TestPassword123',
            dialog_join_password_confirm='',
            email1='',
        ), follow_redirects=True)
        assert response.status_code == 200
        assert b'Passwords must match' in response.data
