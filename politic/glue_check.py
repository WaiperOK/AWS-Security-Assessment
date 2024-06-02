
import boto3
from botocore.exceptions import ClientError
import logging
from utils import get_aws_session, log_and_store

logger = logging.getLogger(__name__)

def check_glue(log_messages):
    session = get_aws_session()
    glue = session.client('glue')

    try:
        response = glue.get_crawlers()
        for crawler in response['Crawlers']:
            crawler_name = crawler['Name']
            state = crawler['State']
            if state != 'READY':
                message = f"Glue Crawler {crawler_name} is not in READY state."
                recommendation = "Recommendation: Check and resolve issues with the Glue Crawler."
                log_and_store(log_messages, f"{message} {recommendation}", level="warning")
    except ClientError as e:
        log_and_store(log_messages, f"Failed to describe Glue Crawlers: {e}", level="error")
