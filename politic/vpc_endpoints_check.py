import boto3
from botocore.exceptions import ClientError
import logging

logger = logging.getLogger(__name__)

def warn_and_store(message, log_messages):
    logger.warning(message)
    log_messages.append(message)

def check_vpc_endpoints(log_messages, session):
    ec2 = session.client('ec2')
    try:
        response = ec2.describe_vpc_endpoints()
        for endpoint in response['VpcEndpoints']:
            if endpoint['State'] != 'available':
                message = f"VPC Endpoint {endpoint['VpcEndpointId']} is not in 'available' state."
                recommendation = "Recommendation: Ensure all VPC endpoints are in the 'available' state for proper operation."
                warn_and_store(f"{message} {recommendation}", log_messages)
    except ClientError as e:
        logger.error(f"Failed to describe VPC endpoints: {e}")
