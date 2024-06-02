import boto3
from botocore.exceptions import ClientError
import logging

logger = logging.getLogger(__name__)

def warn_and_store(message, log_messages):
    logger.warning(message)
    log_messages.append(message)

def check_security_hub(log_messages, session):
    security_hub = session.client('securityhub')
    try:
        response = security_hub.get_findings()
        for finding in response['Findings']:
            if finding['Workflow']['Status'] != 'RESOLVED':
                message = f"Security Hub finding {finding['Id']} is not resolved."
                recommendation = "Recommendation: Review and resolve all Security Hub findings."
                warn_and_store(f"{message} {recommendation}", log_messages)
    except ClientError as e:
        logger.error(f"Failed to get Security Hub findings: {e}")
