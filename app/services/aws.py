import boto3
from botocore.exceptions import ClientError
from app.constants import AWS_BUCKET_NAME, AWS_MEDIA_URL
import uuid


def upload_file(filename, file):
    """Upload a file to an S3 bucket

    :param file: File to upload
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """
    ext = get_file_extension(filename)
    object_name = "{}.{}".format(str(uuid.uuid4()), ext)

    # Upload the file
    s3_client = boto3.client('s3')
    try:
        s3_client.upload_fileobj(file, AWS_BUCKET_NAME, object_name, ExtraArgs={'ACL': 'public-read'})
    except ClientError as e:
        print(e)
        return None
    return AWS_MEDIA_URL + object_name

def get_file_extension(filename):
    return filename.rsplit('.', 1)[1].lower()