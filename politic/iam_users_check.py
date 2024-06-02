
import boto3
from botocore.exceptions import ClientError
import logging
from utils import get_aws_session, log_and_store

logger = logging.getLogger(__name__)

def check_iam_users(log_messages):
    session = get_aws_session()
    iam = session.client('iam')

    try:
        response = iam.list_users()
        for user in response['Users']:
            user_name = user['UserName']
            attached_policies = iam.list_attached_user_policies(UserName=user_name)['AttachedPolicies']
            if not attached_policies:
                message = f"IAM user {user_name} does not have any attached policies."
                recommendation = "Recommendation: Ensure all IAM users have the appropriate policies attached."
                log_and_store(log_messages, f"{message} {recommendation}", level="warning")
    except ClientError as e:
        log_and_store(log_messages, f"Failed to describe IAM users: {e}", level="error")
