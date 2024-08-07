#!/usr/bin/env python3
import os
import aws_cdk as cdk
from stacks.main_stack import main_stack
from dotenv import load_dotenv

app = cdk.App()

# Load environment variables from .env file
load_dotenv()

# Retrieve parameters from environment variables or other sources
email_subscription_endpoint = os.getenv("EMAIL_SUBSCRIPTION_ENDPOINT")
file_upload_bucket = os.getenv("FILE_UPLOAD_BUCKET")

main_stack(
    app,
    "S3FileUploadNotification",
    email_subscription_endpoint=email_subscription_endpoint,
    file_upload_bucket=file_upload_bucket,
)

app.synth()
