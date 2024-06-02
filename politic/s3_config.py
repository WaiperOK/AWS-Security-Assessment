
import boto3
from botocore.exceptions import ClientError
import logging

logger = logging.getLogger(__name__)

def warn_and_store(message, log_messages):
    logger.warning(message)
    log_messages.append(message)


s3 = boto3.client(
    's3',
    aws_access_key_id='AKIA4MTWHWAQWEXGWEGH',
    aws_secret_access_key='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',
    region_name='us-west-2'
)

def check_s3_buckets(log_messages, session):
    s3 = session.client('s3')
    try:
        response = s3.list_buckets()
        for bucket in response['Buckets']:
            bucket_name = bucket['Name']
            acl = s3.get_bucket_acl(Bucket=bucket_name)
            for grant in acl['Grants']:
                if grant['Grantee']['Type'] == 'Group' and grant['Grantee']['URI'] == 'http://acs.amazonaws.com/groups/global/AllUsers':
                    message = f"S3 bucket {bucket_name} is publicly accessible."
                    recommendation = "Recommendation: Review the bucket's ACL and restrict access."
                    warn_and_store(f"{message} {recommendation}", log_messages)
    except ClientError as e:
        warn_and_store(f"Failed to list or get ACL for S3 buckets: {e}", log_messages)

