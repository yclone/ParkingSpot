from werkzeug.security import generate_password_hash, check_password_hash
from models.user import User, db

class UserService:
    @staticmethod
    def create_user(data):
        if User.query.filter_by(username=data['username']).first():
            raise ValueError('Username já existe!')
        if User.query.filter_by(email=data['email']).first():
            raise ValueError('Email já cadastrado!')

        new_user = User(
            first_name=data['first_name'],
            last_name=data['last_name'],
            email=data['email'],
            username=data['username'],
            password_hash=generate_password_hash(data['password'])
        )
        db.session.add(new_user)
        db.session.commit()
        return new_user

    @staticmethod
    def authenticate_user(username, password):
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password_hash, password):
            return user
        return None
