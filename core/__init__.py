from flask import Flask
from flask_admin.contrib.sqla import ModelView
from .extensions import db, migrate, login_manager, cors, admin
from .models import User, Product, Order

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///main.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'jhiufuyvr8fref4j'
    app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'

    # CORS headers
    @app.after_request
    def add_cors_headers(response):
        response.headers['Access-Control-Allow-Origin'] = 'http://localhost:5173'
        response.headers['Access-Control-Allow-Methods'] = 'GET'
        response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
        response.headers['Access-Control-Allow-Credentials'] = 'true'
        return response


    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    cors.init_app(app)
    admin.init_app(app)

    # Register blueprints
    from .routes import users as users_bp, products as product_bp, orders as order_bp, api_user as api_bp
    app.register_blueprint(users_bp)
    app.register_blueprint(product_bp)
    app.register_blueprint(order_bp)
    app.register_blueprint(api_bp)

    # flask admin
    admin.add_view(ModelView(User, db.session))
    admin.add_view(ModelView(Product, db.session))
    admin.add_view(ModelView(Order, db.session))

    # Home page
    @app.route('/', methods=['GET'])
    def home():
        return '<h1>Liquor Store API</h1>'

    # Login manager 
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    return app
