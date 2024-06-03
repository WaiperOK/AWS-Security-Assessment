import boto3
from botocore.exceptions import ClientError
import logging

logger = logging.getLogger(__name__)

def warn_and_store(message, log_messages):
    logger.warning(message)
    log_messages.append(message)

iam = boto3.client(
    'iam',
    aws_access_key_id='',
    aws_secret_access_key='',
    region_name='us-west-2'
)

def check_iam_policies(log_messages, session):
    iam = session.client('iam')
    try:
        response = iam.list_users()
        for user in response['Users']:
            user_name = user['UserName']
            policies = iam.list_user_policies(UserName=user_name)
            for policy_name in policies['PolicyNames']:
                policy = iam.get_user_policy(UserName=user_name, PolicyName=policy_name)
                if 'Effect' in policy['PolicyDocument']['Statement'][0] and policy['PolicyDocument']['Statement'][0]['Effect'] == 'Allow':
                    if '*' in policy['PolicyDocument']['Statement'][0]['Action']:
                        message = f"IAM User {user_name} has overly permissive policy: {policy_name}"
                        recommendation = "Recommendation: Review and update the IAM policy to follow the principle of least privilege."
                        warn_and_store(f"{message} {recommendation}", log_messages)
    except ClientError as e:
        warn_and_store(f"Failed to check IAM policies: {e}", log_messages)

