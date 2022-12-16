from application import app, db
from application.user.models import joins, projects, teams
from flask import session, g


def login():
    user = db.session.query(joins).filter_by(email='sc20yx2@leeds.ac.uk').first()
    g.user = user

def test_profile_page_redirect():
    with app.test_client() as client:
        response = client.get('/profile')
        assert response.status_code == 302
        assert b'redirect' in response.data

def test_profile_page():
    app_context = app.app_context()
    app_context.push()
    with app.test_client() as client:
        login = client.post('/login', data=dict(
            email='sc20yx2@leeds.ac.uk',
            password='Abc123456',
        ), follow_redirects=True)
        response = client.get('/profile')
        assert response.status_code == 200
        assert b'Profile' in response.data
    app_context.pop()

def test_profile_update():
    app_context = app.app_context()
    app_context.push()
    with app.test_client() as client:
        login = client.post('/login', data=dict(
            email='sc20yx2@leeds.ac.uk',
            password='Abc123456',
        ), follow_redirects=True)
        response = client.post('/profile/edit-profile', data=dict(
            name='Test1',
            email='sc20yx2@leeds.ac.uk',
            new_password='',
            confirm_new_password='',
        ), follow_redirects=True)
        assert response.status_code == 200
        assert b'Profile' in response.data
        db.session.query(joins).filter_by(email='sc20yx2@leeds.ac.uk').update(dict(name='Test'))
        db.session.commit()
    app_context.pop()

def test_profile_update_password():
    app_context = app.app_context()
    app_context.push()
    with app.test_client() as client:
        login = client.post('/login', data=dict(
            email='sc20yx2@leeds.ac.uk',
            password='Abc123456',
        ), follow_redirects=True)
        response = client.post('/profile/edit-profile', data=dict(
            name='Test',
            email='sc20yx2@leeds.ac.uk',
            new_password='Abc1234567',
            confirm_new_password='Abc1234567',
        ), follow_redirects=True)
        assert response.status_code == 200
        assert b'Profile' in response.data
        db.session.query(joins).filter_by(email='sc20yx2@leeds.ac.uk').update(dict(password='Abc123456'))
        db.session.commit()
    app_context.pop()

def test_profile_new_project():
    app_context = app.app_context()
    app_context.push()
    with app.test_client() as client:
        login = client.post('/login', data=dict(
            email='sc20yx2@leeds.ac.uk',
            password='Abc123456',
        ), follow_redirects=True)
        response = client.post('/profile/new-project', data=dict(
            name='TestProject',
            url='test',
            description='Testtesttest',
            owner=g.user.id,
        ), follow_redirects=True)
        assert response.status_code == 200
        assert b'TestProject' in response.data
        db.session.query(projects).filter_by(owner=g.user.id).delete()
        db.session.commit()
    app_context.pop()

def test_profile_new_team():
    app_context = app.app_context()
    app_context.push()
    with app.test_client() as client:
        login = client.post('/login', data=dict(
            email='sc20yx2@leeds.ac.uk',
            password='Abc123456',
        ), follow_redirects=True)
        response = client.post('/profile/new-team', data=dict(
            name='TestTeam',
            description='Testtesttest',
            owner=g.user.id,
        ), follow_redirects=True)
        assert response.status_code == 200
        assert b'TestTeam' in response.data
        db.session.query(teams).filter_by(owner=g.user.id).delete()
        db.session.commit()
    app_context.pop()

def test_profile_update_settings():
    app_context = app.app_context()
    app_context.push()
    with app.test_client() as client:
        login = client.post('/login', data=dict(
            email='sc20yx2@leeds.ac.uk',
            password='Abc123456',
        ), follow_redirects=True)
        response = client.post('/profile/save-settings', data=dict(
            email_feed = 'on',
            public_member = 'on',
            active_contributor = 'on',
            code_reviewer = 'on',
        ), follow_redirects=True)
        assert response.status_code == 200
        assert b'Profile' in response.data
        db.session.query(joins).filter_by(email='sc20yx2@leeds.ac.uk').update(
            dict(email_feed=False, public_member=False, active_contributor=False, code_reviewer=False))
        db.session.commit()
    app_context.pop()
