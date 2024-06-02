import boto3
from botocore.exceptions import ClientError
import logging
from utils import get_aws_session, log_and_store

logger = logging.getLogger(__name__)

def check_cloudformation(log_messages):
    session = get_aws_session()
    cloudformation = session.client('cloudformation')

    try:
        response = cloudformation.describe_stacks()
        for stack in response['Stacks']:
            stack_id = stack['StackId']
            stack_status = stack['StackStatus']
            if stack_status not in ["CREATE_COMPLETE", "UPDATE_COMPLETE"]:
                message = f"CloudFormation stack {stack_id} has status {stack_status}."
                recommendation = "Recommendation: Ensure all CloudFormation stacks are successfully created or updated."
                log_and_store(log_messages, f"{message} {recommendation}", level="warning")
    except ClientError as e:
        log_and_store(log_messages, f"Failed to describe CloudFormation stacks: {e}", level="error")
