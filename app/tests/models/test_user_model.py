import pytest
from src.models.user import User

def test_password_hashing(init_database):
    user = User(
        first_name='Test',
        last_name='User',
        email='test@test.com',
        username='testuser'
    )
    user.password = 'password123'
    
    assert user.password_hash is not None
    assert user.password_hash != 'password123'
    assert user.check_password('password123')
    assert not user.check_password('wrongpassword')

def test_password_not_readable(init_database):
    user = User(
        first_name='Test',
        last_name='User',
        email='test@test.com',
        username='testuser'
    )
    user.password = 'password123'
    
    with pytest.raises(AttributeError):
        _ = user.password
