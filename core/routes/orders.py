from flask import Blueprint
from ..models import Order, User, Product

orders = Blueprint('orders', __name__, url_prefix='/orders')