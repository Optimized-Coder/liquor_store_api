from ..extensions import db
from datetime import datetime
from flask_login import UserMixin

user_orders = db.Table('user_orders',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('order_id', db.Integer, db.ForeignKey('order.id'))
)

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.Text)
    orders = db.relationship('Order', secondary=user_orders, backref=db.backref('users', lazy='dynamic'))
    street_address = db.Column(db.String(50))
    city = db.Column(db.String(50))
    state = db.Column(db.String(50))
    postcode = db.Column(db.String(20))
    country = db.Column(db.String(50))
    phone = db.Column(db.String(20))
    created_at = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'orders': self.orders,
            'street_address': self.street_address,
            'city': self.city,
            'state': self.state,
            'postcode': self.postcode,
            'country': self.country,
            'phone': self.phone,
            'created_at': self.created_at
        }
    
    def __repr__(self):
        return '<User {}>'.format(self.username)
    
    