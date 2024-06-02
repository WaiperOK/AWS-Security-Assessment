import boto3
from botocore.exceptions import ClientError
import logging

logger = logging.getLogger(__name__)

def warn_and_store(message, log_messages):
    logger.warning(message)
    log_messages.append(message)

def check_cloudtrail(log_messages, session):
    cloudtrail = session.client('cloudtrail')
    try:
        response = cloudtrail.describe_trails()
        for trail in response['trailList']:
            if not trail['IsMultiRegionTrail']:
                message = f"CloudTrail {trail['Name']} is not a multi-region trail."
                recommendation = "Recommendation: Enable multi-region trail for better coverage."
                warn_and_store(f"{message} {recommendation}", log_messages)
            if 'KmsKeyId' not in trail:
                message = f"CloudTrail {trail['Name']} does not have encryption enabled."
                recommendation = "Recommendation: Enable encryption for CloudTrail logs."
                warn_and_store(f"{message} {recommendation}", log_messages)
    except ClientError as e:
        logger.error(f"Failed to describe CloudTrail trails: {e}")
