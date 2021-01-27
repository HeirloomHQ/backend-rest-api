import os
from flask import Flask
from . import routes

def create_app():
    # create and configure the app
    app = Flask(__name__)
    app.register_blueprint(routes.bp)

    return app