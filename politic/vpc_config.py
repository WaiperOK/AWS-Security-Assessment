import boto3
from botocore.exceptions import ClientError
import logging

logger = logging.getLogger(__name__)

def warn_and_store(message, log_messages):
    logger.warning(message)
    log_messages.append(message)

def check_vpc_subnets(log_messages, session):
    ec2 = session.client('ec2')
    try:
        response = ec2.describe_vpcs()
        for vpc in response['Vpcs']:
            vpc_id = vpc['VpcId']
            subnets_response = ec2.describe_subnets(Filters=[{'Name': 'vpc-id', 'Values': [vpc_id]}])
            for subnet in subnets_response['Subnets']:
                if subnet['MapPublicIpOnLaunch']:
                    message = f"Subnet {subnet['SubnetId']} in VPC {vpc_id} has public IP mapping enabled."
                    recommendation = "Recommendation: Disable public IP mapping for the subnet to enhance security."
                    warn_and_store(f"{message} {recommendation}", log_messages)
    except ClientError as e:
        logger.error(f"Failed to describe VPCs or Subnets: {e}")
