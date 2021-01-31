from flask import Flask
from mongoengine import connect
from . import routes
from .auth.routes import auth_bp

def create_app():
    # create and configure the app
    app = Flask(__name__)
    app.register_blueprint(routes.bp)
    app.register_blueprint(auth_bp)

    connect('heirloom')
    return app
