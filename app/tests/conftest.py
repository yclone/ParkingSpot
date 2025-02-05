import pytest
import sys
import os
from pathlib import Path

# Add both project root and app directory to Python path
project_root = str(Path(__file__).parent.parent)
sys.path.insert(0, project_root)

from src.app import app
from src.models.user import db

@pytest.fixture
def test_app():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    app.config['SECRET_KEY'] = 'test_secret_key'
    
    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()

@pytest.fixture
def test_client(test_app):
    return test_app.test_client()

@pytest.fixture
def init_database(test_app):
    with test_app.app_context():
        db.create_all()
        yield db
        db.session.remove()
        db.drop_all()
