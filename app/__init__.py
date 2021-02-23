from flask import Flask
from mongoengine import connect
from flask_jwt_extended import JWTManager
from app import routes
from app.auth.routes import auth_bp
from app.invites.routes import invite_bp
from app.memorial.routes import memorial_bp
from app.constants import SECRET_KEY, MONGO_URI, IS_PROD

connect(host=MONGO_URI)

app = Flask(__name__)
app.register_blueprint(routes.bp)
app.register_blueprint(auth_bp)
app.register_blueprint(invite_bp)
app.register_blueprint(memorial_bp)

app.config['JWT_SECRET_KEY'] = SECRET_KEY
app.config['JWT_TOKEN_LOCATION'] = ['cookies']
app.config['JWT_COOKIE_CSRF_PROTECT'] = False
app.config['JWT_COOKIE_SECURE'] = IS_PROD

JWTManager(app)
