import allure
import pytest
import json
from src.models.parking import ParkingSpot

@allure.feature('Parking API')
class TestParkingAPI:
    
    @allure.story('Create Parking Spot')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_create_parking_spot(self, client):
        # First login to get session
        with allure.step('Login user'):
            client.post('/login', json={
                'username': 'admin',
                'password': 'admin'
            })

        with allure.step('Create parking spot'):
            response = client.post('/parking/create', json={
                'vehicle_plate': 'ABC1234',
                'spot_number': 'A101',
                'apartment': '101',
                'block': 'A'
            })

        with allure.step('Verify parking spot creation'):
            assert response.status_code == 201
            data = json.loads(response.data)
            assert 'message' in data
            assert data['message'] == 'Parking spot created successfully'

    @allure.story('Get Parking Spots')
    @allure.severity(allure.severity_level.NORMAL)
    def test_get_parking_spots(self, client):
        # Login first
        with allure.step('Login user'):
            client.post('/login', json={
                'username': 'admin',
                'password': 'admin'
            })

        with allure.step('Get all parking spots'):
            response = client.get('/parking/spots')

        with allure.step('Verify response'):
            assert response.status_code == 200
            data = json.loads(response.data)
            assert isinstance(data, list)
