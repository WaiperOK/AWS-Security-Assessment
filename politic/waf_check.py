
import boto3
from botocore.exceptions import ClientError
import logging
from utils import get_aws_session, log_and_store

logger = logging.getLogger(__name__)

def check_waf(log_messages):
    session = get_aws_session()
    waf = session.client('waf')

    try:
        response = waf.list_web_acls()
        for acl in response['WebACLs']:
            if not acl['Rules']:
                message = f"WAF ACL {acl['WebACLId']} does not have any rules configured."
                recommendation = "Recommendation: Ensure all WAF ACLs have appropriate rules configured."
                log_and_store(log_messages, f"{message} {recommendation}", level="warning")
    except ClientError as e:
        log_and_store(log_messages, f"Failed to describe WAF ACLs: {e}", level="error")
