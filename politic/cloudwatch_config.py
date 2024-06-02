import boto3
from botocore.exceptions import ClientError
import logging

logger = logging.getLogger(__name__)

def warn_and_store(message, log_messages):
    logger.warning(message)
    log_messages.append(message)

def check_cloudwatch(log_messages, session):
    cloudwatch = session.client('cloudwatch')
    try:
        response = cloudwatch.describe_alarms()
        if not response['MetricAlarms']:
            message = "No CloudWatch alarms are configured."
            recommendation = "Recommendation: Configure CloudWatch alarms to monitor critical metrics and set up alerts for any anomalies."
            warn_and_store(f"{message} {recommendation}", log_messages)
    except ClientError as e:
        logger.error(f"Failed to describe CloudWatch alarms: {e}")
