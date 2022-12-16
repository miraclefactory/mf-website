import pytest
from application import create_app
from flask import Flask


@pytest.fixture(autouse=True)
def app():
    app, mail, db, migrate, pool = create_app()
    yield app