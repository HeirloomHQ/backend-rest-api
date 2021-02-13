import os
from dotenv import load_dotenv

IS_PROD = os.environ.get("FLASK_ENV") == "production"

if not IS_PROD:
    load_dotenv()

SECRET_KEY = os.environ.get("SECRET_KEY")
MONGO_URI = os.environ.get("MONGO_URI")

MAX_REFRESH = 60 * 60 * 24 * 31 # valid for 31 days
