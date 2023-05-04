from flask import Blueprint
from ..models import Order, User, Product

orders = Blueprint('orders', __name__, url_prefix='/orders')

@orders.route('/', methods=['GET'])
def get_orders():
    pass

@orders.route('/active/', methods=['GET'])
def get_active_orders():
    pass

@orders.route('/cancelled/', methods=['GET'])
def get_cancelled_orders():
    pass

@orders.route('/<int:id>/', methods=['GET'])
def get_order(id):
    pass

@orders.route('<int:user_id>', methods=['GET'])
def get_user_orders(user_id):
    pass

@orders.route('/create/', methods=['GET', 'POST'])
def create_order():
    pass

@orders.route('/<int:id>/mark_complete/', methods=['PUT'])
def mark_complete(id):
    pass

@orders.route('/<int:id>/mark_cancelled/', methods=['PUT'])
def mark_cancelled(id):
    pass

@orders.route('/<int:id>/mark_shipped/', methods=['PUT'])
def mark_shipped(id):
    pass

