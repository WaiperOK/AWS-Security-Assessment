import boto3
from botocore.exceptions import ClientError
import logging

logger = logging.getLogger(__name__)

def warn_and_store(message, log_messages):
    logger.warning(message)
    log_messages.append(message)

def check_lambda_functions(log_messages, session):
    lambda_client = session.client('lambda')
    try:
        response = lambda_client.list_functions()
        for function in response['Functions']:
            if function['VpcConfig']['VpcId'] is None:
                message = f"Lambda function {function['FunctionName']} is not configured to run within a VPC."
                recommendation = "Recommendation: Configure the Lambda function to run within a VPC to enhance security."
                warn_and_store(f"{message} {recommendation}", log_messages)
    except ClientError as e:
        logger.error(f"Failed to list Lambda functions: {e}")
