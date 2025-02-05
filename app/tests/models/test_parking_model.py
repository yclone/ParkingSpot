from src.models.parking import ParkingSpot
from src.models.user import User

def test_parking_spot_creation(init_database):
    user = User(
        first_name='Test',
        last_name='User',
        email='test@test.com',
        username='testuser'
    )
    user.password = 'password123'
    init_database.session.add(user)
    init_database.session.commit()
    
    spot = ParkingSpot(
        vehicle_plate='ABC1234',
        spot_number='A1',
        apartment='101',
        block='A',
        user_id=user.id
    )
    init_database.session.add(spot)
    init_database.session.commit()
    
    assert spot.id is not None
    assert spot.user == user
    assert spot in user.parking_spots
