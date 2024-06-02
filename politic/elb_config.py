import boto3
from botocore.exceptions import ClientError
import logging

logger = logging.getLogger(__name__)

def warn_and_store(message, log_messages):
    logger.warning(message)
    log_messages.append(message)

def check_elb(log_messages, session):
    elb = session.client('elb')
    try:
        response = elb.describe_load_balancers()
        for load_balancer in response['LoadBalancerDescriptions']:
            if 'HTTP' in load_balancer['ListenerDescriptions'][0]['Listener']['Protocol']:
                message = f"Load Balancer {load_balancer['LoadBalancerName']} is using HTTP instead of HTTPS."
                recommendation = "Recommendation: Use HTTPS for secure communication."
                warn_and_store(f"{message} {recommendation}", log_messages)
    except ClientError as e:
        logger.error(f"Failed to describe load balancers: {e}")
