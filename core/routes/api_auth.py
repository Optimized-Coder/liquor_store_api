from flask import Blueprint, request, jsonify
from werkzeug.security import (generate_password_hash, 
                               check_password_hash)
from ..extensions import db
from ..models import APIUser

api_user = Blueprint('api_user', __name__)

'''
CREATE USER COMMAND

$ curl -H "Content-Type: application/json" 
    -X POST -d '{"email": "email@example.com", "password": "123456"}' 
    http://localhost:5000/api/create_user/
'''

'''
View API Key

$ curl -H "Content-Type: application/json"
    -X POST -d '{"email": "email@example.com", "password": "your-password"}'
    http://localhost:5000/api/user/
'''

'''
Add API Key to request

$ curl -X GET -H "x-api-key: YOUR_API_KEY" 
    http://localhost:5000/orders/
'''


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
