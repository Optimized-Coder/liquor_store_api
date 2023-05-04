from flask import Blueprint, jsonify, request
from ..models import Product
from ..extensions import db

products = Blueprint('products', __name__, url_prefix='/products')

@products.route('/', methods=['GET'])
def get_products():
    products = Product.query.all()
    return jsonify([product.to_dict() for product in products])

@products.route('/add/', methods=['GET', 'POST'])
def add_product():
    if request.method == 'POST':
        data = request.get_json()
        new_product = Product(
            name=data['name'],
            price=data['price'],
            abv=data['abv'],
            image_url=data['image_url'],
            description=data['description'],
            country_of_origin=data['country'],
            brand=data['brand'],
            product_type=data['product_type']
        )
        db.session.add(new_product)
        db.session.commit()
        return jsonify(new_product.to_dict()), 201

@products.route('/<int:id>/', methods=['GET'])
def get_product(id):
    product = Product.query.filter_by(id=id).first()
    return jsonify(product.to_dict())

@products.route('/brands/<brand>/', methods=['GET'])
def get_products_by_brand(brand):
    product = Product.query.filter_by(brand=brand).all()
    return jsonify([product.to_dict() for product in product])

@products.route('/<int:id>/edit/', methods=['PUT', 'GET'])
def edit_product(id):
    pass

@products.route('/<int:id>/delete/', methods=['DELETE'])
def delete_product(id):
    product = Product.query.filter_by(id=id).first()
    db.session.delete(product)
    db.session.commit()
    return {"message": "Product deleted"}, 300