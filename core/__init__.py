from flask import Flask
from .extensions import db, migrate

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = \
        'sqlite:///main.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # initialize extensions
    db.init_app(app)
    print(f'initialized: {db}')
    migrate.init_app(app, db)
    print(f'initialized: {migrate}')

    # register blueprints
    from .routes import users as users_bp,\
                    products as product_bp,\
                    orders as order_bp
    app.register_blueprint(users_bp)
    app.register_blueprint(product_bp)
    app.register_blueprint(order_bp)
    print(f'blueprints registered: {users_bp}, {order_bp}, {product_bp}')
    

    return app