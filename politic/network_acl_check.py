import boto3
from botocore.exceptions import ClientError
import logging

logger = logging.getLogger(__name__)

def warn_and_store(message, log_messages):
    logger.warning(message)
    log_messages.append(message)

def check_network_acls(log_messages, session):
    ec2 = session.client('ec2')
    try:
        response = ec2.describe_network_acls()
        for acl in response['NetworkAcls']:
            for entry in acl['Entries']:
                if entry['RuleAction'] == 'allow' and entry['CidrBlock'] == '0.0.0.0/0':
                    message = f"Network ACL {acl['NetworkAclId']} has an allow rule for all IPs (0.0.0.0/0)."
                    recommendation = "Recommendation: Restrict the CIDR block to specific IP ranges to enhance security."
                    warn_and_store(f"{message} {recommendation}", log_messages)
    except ClientError as e:
        logger.error(f"Failed to describe network ACLs: {e}")
