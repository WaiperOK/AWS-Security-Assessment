import boto3
from botocore.exceptions import ClientError
import logging

logger = logging.getLogger(__name__)

def warn_and_store(message, log_messages):
    logger.warning(message)
    log_messages.append(message)

def check_config_rules(log_messages, session):
    config = session.client('config')
    try:
        response = config.describe_config_rules()
        for rule in response['ConfigRules']:
            if rule['ConfigRuleState'] != 'ACTIVE':
                message = f"Config rule {rule['ConfigRuleName']} is not active."
                recommendation = "Recommendation: Ensure all Config rules are active to continuously monitor your AWS resources."
                warn_and_store(f"{message} {recommendation}", log_messages)
    except ClientError as e:
        logger.error(f"Failed to describe Config rules: {e}")
