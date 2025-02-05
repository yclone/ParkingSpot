import allure
import pytest
import json
from src.models.user import User

@allure.feature('User API')
class TestUserAPI:
    
    @allure.story('User Registration')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_user_registration(self, client):
        with allure.step('Create new user'):
            response = client.post('/register', json={
                'first_name': 'Test',
                'last_name': 'User',
                'email': 'test@example.com',
                'username': 'testuser',
                'password': 'testpass123'
            })
            
        with allure.step('Verify response'):
            assert response.status_code == 201
            data = json.loads(response.data)
            assert 'message' in data
            assert data['message'] == 'User created successfully'

    @allure.story('User Login')
    @allure.severity(allure.severity_level.BLOCKER)
    def test_user_login(self, client):
        # Create test user
        with allure.step('Create test user'):
            client.post('/register', json={
                'first_name': 'Test',
                'last_name': 'User',
                'email': 'test@example.com',
                'username': 'testuser',
                'password': 'testpass123'
            })

        with allure.step('Attempt login'):
            response = client.post('/login', json={
                'username': 'testuser',
                'password': 'testpass123'
            })

        with allure.step('Verify login success'):
            assert response.status_code == 200
            data = json.loads(response.data)
            assert 'message' in data
            assert data['message'] == 'Login successful'
