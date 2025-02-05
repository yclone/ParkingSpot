from flask import Blueprint, request, jsonify, render_template
from src.services.parking_service import ParkingService
from src.models.user import User, db
from src.models.parking import ParkingSpot

parking_bp = Blueprint('parking', __name__)

@parking_bp.route('/register_car', methods=['GET'])
def register_car_page():
    users = User.query.all()
    return render_template('register_car.html', users=users)

@parking_bp.route('/register_parking_spot', methods=['POST'])
def register_parking_spot():
    try:
        data = request.get_json()
        ParkingService.create_parking_spot(data)
        return jsonify({'message': 'Veículo cadastrado com sucesso!'}), 201
    except ValueError as e:
        return jsonify({'message': str(e)}), 400
    except Exception as e:
        return jsonify({'message': f'Erro ao cadastrar veículo: {str(e)}'}), 500

@parking_bp.route('/parking_spots', methods=['GET'])
def get_parking_spots():
    spots = ParkingSpot.query.all()
    return jsonify([{
        'id': spot.id,
        'vehicle_plate': spot.vehicle_plate,
        'spot_number': spot.spot_number,
        'apartment': spot.apartment,
        'block': spot.block,
        'user_id': spot.user_id
    } for spot in spots])

@parking_bp.route('/parking_spot/<int:id>', methods=['PUT'])
def update_parking_spot(id):
    try:
        spot = ParkingSpot.query.get_or_404(id)
        data = request.get_json()
        
        spot.vehicle_plate = data.get('vehicle_plate', spot.vehicle_plate)
        spot.spot_number = data.get('spot_number', spot.spot_number)
        spot.apartment = data.get('apartment', spot.apartment)
        spot.block = data.get('block', spot.block)
        
        db.session.commit()
        return jsonify({'message': 'Vaga atualizada com sucesso!'})
    except Exception as e:
        return jsonify({'message': f'Erro ao atualizar: {str(e)}'}), 500

@parking_bp.route('/delete_parking_spot/<int:id>', methods=['DELETE'])
def delete_parking_spot(id):
    try:
        spot = ParkingSpot.query.get_or_404(id)
        db.session.delete(spot)
        db.session.commit()
        return jsonify({'message': 'Vaga deletada com sucesso!'})
    except Exception as e:
        return jsonify({'message': f'Erro ao deletar: {str(e)}'}), 500
