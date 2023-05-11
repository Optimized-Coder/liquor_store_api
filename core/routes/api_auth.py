from flask import Blueprint, request, jsonify
from werkzeug.security import (generate_password_hash, 
                               check_password_hash)
from ..extensions import db
from ..models import APIUser

api_user = Blueprint('api_user', __name__)

@api_user.route('/api/create_user/', methods=['POST'])
def create_user():
    data = request.get_json()
    user = APIUser.query.filter_by(email=data['email']).first()
    if user:
        return jsonify({'message': 'User already exists'}), 400
    user = APIUser(
        email=data['email'], 
        password_hash=generate_password_hash(data['password'])
    )
    db.session.add(user)
    db.session.commit()

    user.create_api_key()

    return jsonify({'message': 'User created'}), 201

@api_user.route('/api/user/', methods=['POST'])
def get_user():
    data = request.get_json()
    user = APIUser.query.filter_by(email=data['email']).first()
    if not user:
        return jsonify({"message": "User does not exist"}), 404
    
    if check_password_hash(user.password_hash, data['password']):
        return jsonify(user.to_dict())
    else: return jsonify({"Error": "Invalid Credentials"})
