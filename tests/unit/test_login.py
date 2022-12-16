from flask import Flask
from application import create_app, app


def test_login_page():
    with app.test_client() as client:
        response = client.get('/login')
        assert response.status_code == 200
        assert b'Login' in response.data

def test_login_success():
    with app.test_client() as client:
        response = client.post('/login', data=dict(
            email='sc20yx2@leeds.ac.uk',
            password='Abc123456',
        ), follow_redirects=True)
        assert response.status_code == 200
        assert b'Login' not in response.data

def test_login_user_not_exist():
    with app.test_client() as client:
        response = client.post('/login', data=dict(
            email='email@gmail.com',
            password='Abc123456',
        ), follow_redirects=True)
        assert response.status_code == 200
        assert b'Login' in response.data

def test_login_wrong_password():
    with app.test_client() as client:
        response = client.post('/login', data=dict(
            email='sc20yx2@leeds.ac.uk',
            password='Abc12345678',
        ), follow_redirects=True)
        assert response.status_code == 200
        assert b'Login' in response.data
