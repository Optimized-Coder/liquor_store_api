from flask import Flask
from .extensions import db, migrate, login_manager
from .models import User

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = \
        'sqlite:///main.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] ='jhiufuyvr8fref4j'

    # initialize extensions
    db.init_app(app)
    print(f'initialized: {db}')
    migrate.init_app(app, db)
    print(f'initialized: {migrate}')
    login_manager.init_app(app)

    # register blueprints
    from .routes import users as users_bp,\
                    products as product_bp,\
                    orders as order_bp,\
                    api_user as api_bp
    app.register_blueprint(users_bp)
    app.register_blueprint(product_bp)
    app.register_blueprint(order_bp)
    app.register_blueprint(api_bp)
    print(f'blueprints registered: {users_bp}, {order_bp}, {product_bp}')
    
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))


    return app