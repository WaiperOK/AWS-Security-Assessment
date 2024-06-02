import boto3
from botocore.exceptions import ClientError
import logging

logger = logging.getLogger(__name__)

def warn_and_store(message, log_messages):
    logger.warning(message)
    log_messages.append(message)

def check_rds(log_messages, session):
    rds = session.client('rds')
    try:
        response = rds.describe_db_instances()
        for db_instance in response['DBInstances']:
            if db_instance['PubliclyAccessible']:
                message = f"RDS instance {db_instance['DBInstanceIdentifier']} is publicly accessible."
                recommendation = "Recommendation: Disable public access to this RDS instance."
                warn_and_store(f"{message} {recommendation}", log_messages)
    except ClientError as e:
        logger.error(f"Failed to describe RDS instances: {e}")
