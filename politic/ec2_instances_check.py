import boto3
from botocore.exceptions import ClientError
import logging

logger = logging.getLogger(__name__)

def warn_and_store(message, log_messages):
    logger.warning(message)
    log_messages.append(message)

def check_ec2_instances(log_messages, session):
    ec2 = session.client('ec2')
    try:
        response = ec2.describe_instances()
        for reservation in response['Reservations']:
            for instance in reservation['Instances']:
                if instance['State']['Name'] != 'running':
                    continue
                if 'PublicIpAddress' in instance:
                    message = f"EC2 instance {instance['InstanceId']} has a public IP address."
                    recommendation = "Recommendation: Remove public IP addresses from EC2 instances or ensure they are securely configured."
                    warn_and_store(f"{message} {recommendation}", log_messages)
    except ClientError as e:
        logger.error(f"Failed to describe EC2 instances: {e}")
