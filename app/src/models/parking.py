from .user import db

class ParkingSpot(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    vehicle_plate = db.Column(db.String(20), unique=True, nullable=False)
    spot_number = db.Column(db.String(10), nullable=False)
    apartment = db.Column(db.String(10), nullable=False)
    block = db.Column(db.String(10), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('parking_spots', lazy=True))
