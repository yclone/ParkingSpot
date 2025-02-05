from models.parking import ParkingSpot, db

class ParkingService:
    @staticmethod
    def create_parking_spot(data):
        if ParkingSpot.query.filter_by(vehicle_plate=data['vehicle_plate']).first():
            raise ValueError('Veículo já cadastrado!')

        new_spot = ParkingSpot(
            vehicle_plate=data['vehicle_plate'],
            spot_number=data['spot_number'],
            apartment=data['apartment'],
            block=data['block'],
            user_id=data['user_id']
        )
        db.session.add(new_spot)
        db.session.commit()
        return new_spot
