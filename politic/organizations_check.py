import boto3
from botocore.exceptions import ClientError
import logging

logger = logging.getLogger(__name__)

def warn_and_store(message, log_messages):
    logger.warning(message)
    log_messages.append(message)

def check_organizations(log_messages, session):
    organizations = session.client('organizations')
    try:
        response = organizations.describe_organization()
        if 'MasterAccountId' not in response['Organization']:
            message = "AWS Organization does not have a master account configured."
            recommendation = "Recommendation: Ensure that the AWS Organization has a master account configured."
            warn_and_store(f"{message} {recommendation}", log_messages)
    except ClientError as e:
        logger.error(f"Failed to describe AWS Organization: {e}")
