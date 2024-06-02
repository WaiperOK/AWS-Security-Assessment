import boto3
from botocore.exceptions import ClientError
import logging

logger = logging.getLogger(__name__)

def warn_and_store(message, log_messages):
    logger.warning(message)
    log_messages.append(message)

def check_mfa(log_messages, session):
    iam = session.client('iam')
    try:
        response = iam.list_users()
        for user in response['Users']:
            mfa_devices = iam.list_mfa_devices(UserName=user['UserName'])
            if not mfa_devices['MFADevices']:
                message = f"IAM User {user['UserName']} does not have MFA enabled."
                recommendation = "Recommendation: Enable MFA for all IAM users to enhance security."
                warn_and_store(f"{message} {recommendation}", log_messages)
    except ClientError as e:
        logger.error(f"Failed to list MFA devices: {e}")
