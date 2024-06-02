
import boto3
from botocore.exceptions import ClientError
import logging
from utils import get_aws_session, log_and_store

logger = logging.getLogger(__name__)

def check_autoscaling(log_messages):
    session = get_aws_session()
    autoscaling = session.client('autoscaling')

    try:
        response = autoscaling.describe_auto_scaling_groups()
        for group in response['AutoScalingGroups']:
            if not group['DesiredCapacity']:
                message = f"Auto Scaling group {group['AutoScalingGroupName']} does not have a desired capacity set."
                recommendation = "Recommendation: Ensure all Auto Scaling groups have a desired capacity set."
                log_and_store(log_messages, f"{message} {recommendation}", level="warning")
    except ClientError as e:
        log_and_store(log_messages, f"Failed to describe Auto Scaling groups: {e}", level="error")
