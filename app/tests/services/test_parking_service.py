import pytest
import sys
import os
from pathlib import Path

# Add the project root directory to Python path
project_root = str(Path(__file__).parent.parent.parent)
sys.path.insert(0, project_root)

from src.services.parking_service import ParkingService
from src.services.user_service import UserService
from src.models.parking import ParkingSpot

def test_create_parking_spot_success(init_database):
    # First create a user
    user_data = {
        'first_name': 'Test',
        'last_name': 'User',
        'email': 'test@test.com',
        'username': 'testuser',
        'password': 'password123'
    }
    user = UserService.create_user(user_data)
    
    parking_data = {
        'vehicle_plate': 'ABC1234',
        'spot_number': 'A1',
        'apartment': '101',
        'block': 'A',
        'user_id': user.id
    }
    
    spot = ParkingService.create_parking_spot(parking_data)
    assert spot.vehicle_plate == 'ABC1234'
    assert spot.spot_number == 'A1'

def test_create_duplicate_vehicle_plate(init_database):
    # First create a user
    user_data = {
        'first_name': 'Test',
        'last_name': 'User',
        'email': 'test@test.com',
        'username': 'testuser',
        'password': 'password123'
    }
    user = UserService.create_user(user_data)
    
    parking_data = {
        'vehicle_plate': 'ABC1234',
        'spot_number': 'A1',
        'apartment': '101',
        'block': 'A',
        'user_id': user.id
    }
    
    ParkingService.create_parking_spot(parking_data)
    
    with pytest.raises(ValueError, match='Veículo já cadastrado!'):
        ParkingService.create_parking_spot(parking_data)
