from flask import Blueprint, jsonify
from ..models import User

users = Blueprint('users', __name__, url_prefix='/users')

@users.route('/', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([user.to_dict() for user in users])

@users.route('/add/', methods=['GET', 'POST'])
def add_user():
    pass

@users.route('/<int:user_id>/', methods=['GET'])
def get_user(user_id):
    pass

@users.route('/<int:user_id>/delete/', methods=['DELETE'])
def delete_user(user_id):
    pass

@users.route('/<int:user_id>/edit/', methods=['GET', 'POST'])
def edit_user(user_id):
    pass
