
import boto3
from botocore.exceptions import ClientError
import logging

logger = logging.getLogger(__name__)

def enable_s3_encryption(bucket_name, session):
    s3 = session.client('s3')
    try:
        s3.put_bucket_encryption(
            Bucket=bucket_name,
            ServerSideEncryptionConfiguration={
                'Rules': [{
                    'ApplyServerSideEncryptionByDefault': {
                        'SSEAlgorithm': 'AES256'
                    }
                }]
            }
        )
        logger.info(f"Enabled encryption for S3 bucket: {bucket_name}")
    except ClientError as e:
        logger.error(f"Failed to enable encryption for S3 bucket {bucket_name}: {e}")
