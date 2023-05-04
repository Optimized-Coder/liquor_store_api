from flask import Blueprint, jsonify
from ..models import Product

products = Blueprint('products', __name__, url_prefix='/products')

@products.route('/', methods=['GET'])
def get_products():
    products = Product.query.all()
    return jsonify([product.to_dict() for product in products])

@products.route('/add/', methods=['GET', 'POST'])
def add_product():
    pass

@products.route('/<int:id>/', methods=['GET'])
def get_product(id):
    pass

@products.route('/<int:id>/edit/', methods=['PUT', 'GET'])
def edit_product(id):
    pass

@products.route('/<int:id>/delete/', methods=['DELETE'])
def delete_product(id):
    pass