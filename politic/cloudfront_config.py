import boto3
from botocore.exceptions import ClientError
import logging

logger = logging.getLogger(__name__)

def warn_and_store(message, log_messages):
    logger.warning(message)
    log_messages.append(message)

def check_cloudfront_distributions(log_messages, session):
    cloudfront = session.client('cloudfront')
    try:
        response = cloudfront.list_distributions()
        for distribution in response.get('DistributionList', {}).get('Items', []):
            if 'ViewerCertificate' not in distribution or distribution['ViewerCertificate']['CloudFrontDefaultCertificate']:
                message = f"CloudFront distribution {distribution['Id']} does not use a custom SSL certificate."
                recommendation = "Recommendation: Use a custom SSL certificate for better security."
                warn_and_store(f"{message} {recommendation}", log_messages)
    except ClientError as e:
        logger.error(f"Failed to describe CloudFront distributions: {e}")
