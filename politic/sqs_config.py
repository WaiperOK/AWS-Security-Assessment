import boto3
from botocore.exceptions import ClientError
import logging

logger = logging.getLogger(__name__)

def warn_and_store(message, log_messages):
    logger.warning(message)
    log_messages.append(message)

def check_sqs(log_messages, session):
    sqs = session.client('sqs')
    try:
        response = sqs.list_queues()
        for queue_url in response.get('QueueUrls', []):
            attributes = sqs.get_queue_attributes(QueueUrl=queue_url, AttributeNames=['All'])['Attributes']
            if 'KmsMasterKeyId' not in attributes:
                message = f"SQS Queue {queue_url} does not have server-side encryption enabled."
                recommendation = "Recommendation: Enable server-side encryption for this SQS queue to enhance security."
                warn_and_store(f"{message} {recommendation}", log_messages)
    except ClientError as e:
        logger.error(f"Failed to describe SQS queues: {e}")
