import pytest
import sys
import os
from pathlib import Path

# Add the project root directory to Python path
project_root = str(Path(__file__).parent.parent.parent)
sys.path.insert(0, project_root)

from src.services.user_service import UserService
from src.models.user import User

def test_create_user_success(init_database):
    data = {
        'first_name': 'Test',
        'last_name': 'User',
        'email': 'test@test.com',
        'username': 'testuser',
        'password': 'password123'
    }
    
    user = UserService.create_user(data)
    assert user.username == 'testuser'
    assert user.email == 'test@test.com'

def test_create_duplicate_username(init_database):
    data = {
        'first_name': 'Test',
        'last_name': 'User',
        'email': 'test@test.com',
        'username': 'testuser',
        'password': 'password123'
    }
    
    UserService.create_user(data)
    
    with pytest.raises(ValueError, match='Username já existe!'):
        UserService.create_user(data)

def test_authenticate_user(init_database):
    data = {
        'first_name': 'Test',
        'last_name': 'User',
        'email': 'test@test.com',
        'username': 'testuser',
        'password': 'password123'
    }
    
    UserService.create_user(data)
    
    user = UserService.authenticate_user('testuser', 'password123')
    assert user is not None
    assert user.username == 'testuser'

def test_authenticate_user_invalid_credentials(init_database):
    data = {
        'first_name': 'Test',
        'last_name': 'User',
        'email': 'test@test.com',
        'username': 'testuser',
        'password': 'password123'
    }
    
    UserService.create_user(data)
    
    user = UserService.authenticate_user('testuser', 'wrongpassword')
    assert user is None
