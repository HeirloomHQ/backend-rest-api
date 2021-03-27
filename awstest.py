import app.constants
from app.services import aws

file_path = "/Users/amanzanero/Documents/401project/backend-rest-api/tmp/ben-lei-rpsS_bx-Za8-unsplash.jpg"

with open(file_path, "rb") as file_upload:
    print(aws.upload_file("pic.jpg", file_upload))

# print(aws.get_file_extension(file_path))