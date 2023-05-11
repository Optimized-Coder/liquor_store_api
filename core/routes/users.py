from flask import Blueprint, jsonify, request
from ..models import User
from werkzeug.security import (generate_password_hash,
                                check_password_hash)
from ..extensions import db
from flask_login import current_user, login_user, logout_user 

users = Blueprint('users', __name__, url_prefix='/users')

@users.route('/', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([user.to_dict() for user in users])

@users.route('/add/', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        data = request.get_json()
        user = User(
            name=data['name'], 
            username=data['username'],
            email=data['email'], 
            password_hash=generate_password_hash(data['password'])
        )
        db.session.add(user)
        db.session.commit()
        print(f'Created user: {user.username}')
        return jsonify(user.to_dict()), 201
    
@users.route('/login/', methods=['POST'])
def login():
    if request.method == 'POST':
        data = request.get_json()
        user = User.query.filter_by(username=data['username']).\
            first()
        if user and check_password_hash(user.password_hash, 
                                        data['password']):
            login_user(user)
            return jsonify({"message": "Logged in successfully"}), \
                200
        else:
            return jsonify({'message': 'Invalid credentials'}), \
                401
        
@users.route('/logout/', methods=['POST'])
def logout():
    logout_user()
    return jsonify({"message": "Logged out successfully"}), 200

@users.route('/<int:user_id>/', methods=['GET'])
def get_user(user_id):
    user = User.query.filter_by(id=user_id).first()
    return jsonify(user.to_dict())

@users.route('/<int:id>/delete/', methods=['DELETE'])
def delete_user(id):
    user = User.query.filter_by(id=id).first()
    db.session.delete(user)
    db.session.commit()
    print(f'Deleted User {user.username}')
    return jsonify({"message": "User deleted successfully"}), 200

@users.route('/<int:user_id>/edit/', methods=['GET', 'POST'])
def edit_user(user_id):
    pass
