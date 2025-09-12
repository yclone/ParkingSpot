from flask import Blueprint, request, jsonify, session
from models.user import User, db
import logging

user_bp = Blueprint('user', __name__)

@user_bp.route('/register_user', methods=['POST'])
def register_user():
    try:
        data = request.get_json()
        # Check if email or username is already registered
        if User.query.filter_by(email=data['email']).first() or User.query.filter_by(username=data['username']).first():
            logging.warning('Attempt to register with existing email or username')
            return jsonify({'message': 'Usuário já cadastrado no sistema!'}), 400
        
        user = User(
            first_name=data['first_name'],
            last_name=data['last_name'],
            email=data['email'],
            username=data['username']
        )
        user.password = data['password']

        db.session.add(user)
        db.session.commit()
        logging.info(f'User {user.username} registered successfully')
        return jsonify({'message': 'Usuário cadastrado com sucesso!', 'user_id': user.id}), 201
    except Exception as e:
        db.session.rollback()
        logging.error(f'Error registering user: {str(e)}')
        return jsonify({'message': f'Erro ao cadastrar usuário: {str(e)}'}), 400

@user_bp.route('/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        user = User.query.filter_by(username=data['username']).first()
        
        if user and user.check_password(data['password']):
            session['user_id'] = user.id
            session['user_name'] = f"{user.first_name} {user.last_name}"
            logging.info(f'User {user.username} logged in successfully')
            return jsonify({'message': 'Login successful'}), 200
        
        logging.warning('Invalid login attempt')
        return jsonify({'message': 'Username ou senha inválidos'}), 401
    except Exception as e:
        logging.error(f'Error during login: {str(e)}')
        return jsonify({'message': f'Erro no login: {str(e)}'}), 500


@user_bp.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([{
        'id': user.id,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'email': user.email,
        'username': user.username
    } for user in users])

@user_bp.route('/user/<int:id>', methods=['GET'])
def get_user(id):
    user = User.query.get_or_404(id)
    return jsonify({
        'id': user.id,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'email': user.email,
        'username': user.username
    })

@user_bp.route('/user/<int:id>', methods=['PUT'])
def update_user(id):
    try:
        user = User.query.get_or_404(id)
        data = request.get_json()
        
        user.first_name = data.get('first_name', user.first_name)
        user.last_name = data.get('last_name', user.last_name)
        user.email = data.get('email', user.email)
        user.username = data.get('username', user.username)
        if data.get('password'):
            user.password = data['password']
        
        db.session.commit()
        return jsonify({'message': 'Usuário atualizado com sucesso!'})
    except Exception as e:
        return jsonify({'message': f'Erro ao atualizar: {str(e)}'}), 500

@user_bp.route('/current_user')
def get_current_user():
    if 'user_id' in session:
        return jsonify({
            'id': session['user_id'],
            'name': session['user_name']
        })
    return jsonify({'message': 'Not logged in'}), 401

@user_bp.route('/logout', methods=['POST'])
def logout():
    session.clear()
    return jsonify({'message': 'Logout successful'})

@user_bp.route('/dashboard')
def dashboard():
    if 'user_id' in session:
        return jsonify({'message': 'Bem-vindo ao dashboard!'})
    return jsonify({'message': 'Usuário não autenticado'}), 401

def create_initial_user():
    try:
        if User.query.first() is None:
            admin = User(
                first_name='Admin',
                last_name='System',
                email='admin@system.com',
                username='admin'
            )
            admin.password = 'admin123'
            db.session.add(admin)
            db.session.commit()
            logging.info("Usuário inicial criado com sucesso!")
    except Exception as e:
        logging.error(f"Erro ao criar usuário inicial: {str(e)}")
