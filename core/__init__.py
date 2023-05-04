from flask import Flask

def create_app():
    app = Flask(__name__)

    # register blueprints
    from routes import users as users_bp,\
                    products as product_bp,\
                    orders as order_bp
    app.register_blueprint(users_bp)
    app.register_blueprint(product_bp)
    app.register_blueprint(order_bp)
    

    return app