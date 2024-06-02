import boto3
from botocore.exceptions import ClientError
import logging

logger = logging.getLogger(__name__)

def warn_and_store(message, log_messages):
    logger.warning(message)
    log_messages.append(message)

def check_dynamodb(log_messages, session):
    dynamodb = session.client('dynamodb')
    try:
        response = dynamodb.list_tables()
        for table_name in response['TableNames']:
            table = dynamodb.describe_table(TableName=table_name)
            if 'SSEDescription' not in table['Table']:
                message = f"DynamoDB table {table_name} does not have server-side encryption enabled."
                recommendation = "Recommendation: Enable server-side encryption for this DynamoDB table to enhance security."
                warn_and_store(f"{message} {recommendation}", log_messages)
    except ClientError as e:
        logger.error(f"Failed to describe DynamoDB tables: {e}")
