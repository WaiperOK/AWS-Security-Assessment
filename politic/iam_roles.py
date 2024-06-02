import boto3
from botocore.exceptions import ClientError
import logging

logger = logging.getLogger(__name__)

def warn_and_store(message, log_messages):
    logger.warning(message)
    log_messages.append(message)

def check_iam_roles(log_messages, session):
    iam = session.client('iam')
    try:
        response = iam.list_roles()
        for role in response['Roles']:
            if 'AssumeRolePolicyDocument' not in role:
                message = f"IAM Role {role['RoleName']} does not have an assume role policy document."
                recommendation = "Recommendation: Ensure that each IAM role has a properly configured assume role policy document."
                warn_and_store(f"{message} {recommendation}", log_messages)
    except ClientError as e:
        logger.error(f"Failed to list IAM roles: {e}")
