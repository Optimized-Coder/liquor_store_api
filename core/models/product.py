from ..extensions import db

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    price = db.Column(db.Float)
    abv = db.Column(db.Float)
    country_of_origin = db.Column(db.String(50))
    brand = db.Column(db.String(50))
    product_type = db.Column(db.String(50))
    description = db.Column(db.String(1000))
    image_url = db.Column(db.String(1000))

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'product_type': self.product_type,
            'description': self.description,
            'image_url': self.image_url,
            'abv': self.abv,
            'country_of_origin': self.country_of_origin,
            'brand': self.brand
        }