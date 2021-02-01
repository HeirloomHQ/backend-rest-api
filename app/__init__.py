from flask import Flask
from mongoengine import connect
from flask_jwt_extended import JWTManager
from app import routes
from app.auth.routes import auth_bp
from app.constants import SECRET_KEY, MONGO_URI


def create_app():
    # create and configure the app
    app = Flask(__name__)
    app.register_blueprint(routes.bp)
    app.register_blueprint(auth_bp)

    app.config["SECRET_KEY"] = SECRET_KEY
    JWTManager(app)

    connect(host=MONGO_URI)
    return app
