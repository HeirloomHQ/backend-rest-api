import os
from pathlib import Path

IS_PROD = os.environ.get("FLASK_ENV") == "production"

if not IS_PROD:
    import dotenv
    dotenv.load_dotenv()
    sendgrid_file = Path("./sendgrid.env").resolve()
    aws_env = Path("./aws.env").resolve()
    dotenv.load_dotenv(sendgrid_file)
    dotenv.load_dotenv(aws_env)

SECRET_KEY = os.environ.get("SECRET_KEY")
MONGO_URI = os.environ.get("MONGO_URI")
DOMAIN =  os.environ.get("DOMAIN_URI")
CLIENT = os.environ.get("CLIENT_URI")

SENDGRID_API_KEY = os.environ.get("SENDGRID_API_KEY")
FROM_EMAIL = 'amanzane@usc.edu'

MAX_REFRESH = 60 * 60 * 24 * 31 # valid for 31 days
INVITE_DAYS_TTL = 7
IMG_TMP_UPLOAD = Path("./tmp").resolve()
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY =  os.environ.get("AWS_SECRET_ACCESS_KEY")
AWS_REGION = os.environ.get("AWS_REGION")
AWS_BUCKET_NAME = os.environ.get("AWS_BUCKET_NAME")
AWS_MEDIA_URL = "https://heirloom-media-uploads.s3.us-east-2.amazonaws.com/"