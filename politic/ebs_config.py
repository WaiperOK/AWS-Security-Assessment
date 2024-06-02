import boto3
from botocore.exceptions import ClientError
import logging

logger = logging.getLogger(__name__)

def warn_and_store(message, log_messages):
    logger.warning(message)
    log_messages.append(message)

def check_ebs_volumes(log_messages, session):
    ec2 = session.client('ec2')
    try:
        response = ec2.describe_volumes()
        for volume in response['Volumes']:
            if volume['Encrypted'] is False:
                message = f"EBS volume {volume['VolumeId']} is not encrypted."
                recommendation = "Recommendation: Enable encryption for this EBS volume to enhance security."
                warn_and_store(f"{message} {recommendation}", log_messages)
    except ClientError as e:
        logger.error(f"Failed to describe EBS volumes: {e}")
