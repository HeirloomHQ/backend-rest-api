import os
from pathlib import Path

IS_PROD = os.environ.get("FLASK_ENV") == "production"

if not IS_PROD:
    import dotenv
    dotenv.load_dotenv()
    sendgrid_file = Path("./sendgrid.env").resolve()
    dotenv.load_dotenv(sendgrid_file)

SECRET_KEY = os.environ.get("SECRET_KEY")
MONGO_URI = os.environ.get("MONGO_URI")
DOMAIN =  os.environ.get("DOMAIN_URI")
CLIENT = os.environ.get("CLIENT_URI")

SENDGRID_API_KEY = os.environ.get("SENDGRID_API_KEY")
FROM_EMAIL = 'amanzane@usc.edu'

MAX_REFRESH = 60 * 60 * 24 * 31 # valid for 31 days
INVITE_DAYS_TTL = 7
