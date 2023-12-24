import boto3

from source.infrastructure import settings

session = boto3.Session(
    aws_access_key_id=settings.default.aws_access_key,
    aws_secret_access_key=settings.default.aws_secret_access_key
)

ses_client = session.client('ses', region_name="us-east-2")
