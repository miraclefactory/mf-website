from flask import Flask
import pytest
from application import create_app

# pytestmark = pytest.mark.usefixtures('app')

def test_init():
    app, mail, db, migrate, pool = create_app()
    assert isinstance(app, Flask)

def test_config():
    app, mail, db, migrate, pool = create_app()
    assert app.config['DEBUG'] is True
