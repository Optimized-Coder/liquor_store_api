from ..extensions import db
from datetime import datetime

order_product = db.Table('order_product', 
            db.Column('order_id', db.Integer, db.ForeignKey('order.id')),
            db.Column('product_id', db.Integer, db.ForeignKey('product.id'))
)

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    products = db.relationship('Product', secondary=order_product, backref=db.backref('orders', lazy='dynamic'))
    quantity = db.Column(db.Integer)
    value = db.Column(db.Float)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(100), default='pending')
    
    def __repr__(self):
        return '<Order {}>'.format(self.id)
    
    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'product_id': self.product_id,
            'quantity': self.quantity,
            'value': self.value,
            'date': self.date,
           'status': self.status
        }