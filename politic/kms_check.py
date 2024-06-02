
import boto3
from botocore.exceptions import ClientError
import logging
from utils import get_aws_session, log_and_store

logger = logging.getLogger(__name__)

def check_kms(log_messages):
    session = get_aws_session()
    kms = session.client('kms')

    try:
        response = kms.list_keys()
        for key in response['Keys']:
            key_id = key['KeyId']
            key_metadata = kms.describe_key(KeyId=key_id)['KeyMetadata']
            if not key_metadata['Enabled']:
                message = f"KMS key {key_id} is not enabled."
                recommendation = "Recommendation: Ensure all KMS keys are enabled."
                log_and_store(log_messages, f"{message} {recommendation}", level="warning")
    except ClientError as e:
        log_and_store(log_messages, f"Failed to describe KMS keys: {e}", level="error")
