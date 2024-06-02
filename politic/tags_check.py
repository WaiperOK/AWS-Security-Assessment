import boto3
from botocore.exceptions import ClientError
import logging

logger = logging.getLogger(__name__)

def warn_and_store(message, log_messages):
    logger.warning(message)
    log_messages.append(message)

def check_tags(log_messages, session):
    ec2 = session.client('ec2')
    try:
        response = ec2.describe_tags()
        for tag in response['Tags']:
            if 'aws:cloudformation' not in tag['Key']:
                message = f"Resource {tag['ResourceId']} does not have the required CloudFormation tag."
                recommendation = "Recommendation: Ensure all resources have the required CloudFormation tags for proper tracking."
                warn_and_store(f"{message} {recommendation}", log_messages)
    except ClientError as e:
        logger.error(f"Failed to describe tags: {e}")
