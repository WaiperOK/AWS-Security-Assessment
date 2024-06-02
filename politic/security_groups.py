import boto3
from botocore.exceptions import ClientError
import logging

logger = logging.getLogger(__name__)

def warn_and_store(message, log_messages):
    logger.warning(message)
    log_messages.append(message)

def check_security_groups(log_messages, session):
    ec2 = session.client('ec2')
    try:
        response = ec2.describe_security_groups()
        for sg in response['SecurityGroups']:
            sg_id = sg['GroupId']
            for perm in sg['IpPermissions']:
                if 'IpRanges' in perm:
                    for ip_range in perm['IpRanges']:
                        if ip_range['CidrIp'] == '0.0.0.0/0':
                            message = f"Security Group {sg_id} allows access from all IPs (0.0.0.0/0)."
                            recommendation = "Recommendation: Restrict access to specific IP ranges."
                            warn_and_store(f"{message} {recommendation}", log_messages)
    except ClientError as e:
        warn_and_store(f"Failed to describe security groups: {e}", log_messages)
