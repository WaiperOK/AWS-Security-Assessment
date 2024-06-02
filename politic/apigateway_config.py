import boto3
from botocore.exceptions import ClientError
import logging

logger = logging.getLogger(__name__)

def warn_and_store(message, log_messages):
    logger.warning(message)
    log_messages.append(message)

def check_api_gateway(log_messages, session):
    api_gateway = session.client('apigateway')
    try:
        response = api_gateway.get_rest_apis()
        for api in response['items']:
            if not api.get('endpointConfiguration') or 'PRIVATE' not in api['endpointConfiguration']['types']:
                message = f"API Gateway {api['name']} is not configured with PRIVATE endpoint."
                recommendation = "Recommendation: Configure the API Gateway to use PRIVATE endpoint to enhance security."
                warn_and_store(f"{message} {recommendation}", log_messages)
    except ClientError as e:
        logger.error(f"Failed to describe API Gateway: {e}")
