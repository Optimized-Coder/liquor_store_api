from flask import Blueprint, request, jsonify
from ..models import Order, User, Product
from ..models.order import order_product
from flask_login import current_user
from ..extensions import db

orders = Blueprint('orders', __name__, url_prefix='/orders')

@orders.route('/', methods=['GET'])
def get_orders():
    orders = Order.query.all()
    return jsonify([order.to_dict() for order in orders])

@orders.route('/active/', methods=['GET'])
def get_active_orders():
    orders = Order.query.filter_by(status='active').all()
    return jsonify([order.to_dict() for order in orders])

@orders.route('/cancelled/', methods=['GET'])
def get_cancelled_orders():
    orders = Order.query.filter_by(status='cancelled').all()
    return jsonify([order.to_dict() for order in orders])

@orders.route('/<int:id>/', methods=['GET'])
def get_order(id):
    order = Order.query.get_or_404(id)
    return jsonify(order.to_dict())

@orders.route('/by_user/<int:user_id>/', methods=['GET'])
def get_user_orders(user_id):
    orders = Order.query.filter_by(user_id=user_id).all()
    return jsonify([order.to_dict() for order in orders])

@orders.route('/create/', methods=['GET', 'POST'])
def create_order():
    if request.method == 'POST':
        if current_user.is_authenticated:
            data = request.get_json()
            new_order = Order(
                user_id=current_user.id
            )
            
            product_ids = [id for id in data['products']]
            products = Product.query.filter(Product.id.in_(product_ids))

            for product in products:
                new_order.products.append(product)
            db.session.add(new_order)
            db.session.commit()

            return new_order.to_dict()
        else:
            return jsonify({'error': 'You are not logged in'})
            

@orders.route('/<int:id>/mark_complete/', methods=['PUT'])
def mark_complete(id):
    order = Order.query.get_or_404(id)
    order.status = 'complete'
    db.session.commit()
    return order.to_dict()

@orders.route('/<int:id>/mark_cancelled/', methods=['PUT'])
def mark_cancelled(id):
    order = Order.query.get_or_404(id)
    order.status = 'cancelled'
    db.session.commit()
    return order.to_dict()

@orders.route('/<int:id>/mark_shipped/', methods=['PUT'])
def mark_shipped(id):
    order = Order.query.get_or_404(id)
    order.status ='shipped'
    db.session.commit()
    return order.to_dict()

