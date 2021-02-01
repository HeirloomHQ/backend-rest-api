import os
from dotenv import load_dotenv

if os.environ.get("FLASK_ENV") == "development":
    load_dotenv()

SECRET_KEY = os.environ.get("SECRET_KEY")
MONGO_URI = os.environ.get("MONGO_URI")
