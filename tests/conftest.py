import pytest
from application import create_app


@pytest.fixture
def app():
    app, mail, db, migrate, pool = create_app()
    yield app

@pytest.fixture
def client(app):
    return app.test_client()
