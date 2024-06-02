import boto3
from botocore.exceptions import ClientError
import logging

logger = logging.getLogger(__name__)

def warn_and_store(message, log_messages):
    logger.warning(message)
    log_messages.append(message)

def check_backups(log_messages, session):
    backup = session.client('backup')
    try:
        response = backup.list_backup_jobs()
        for job in response['BackupJobs']:
            if job['State'] != 'COMPLETED':
                message = f"Backup job {job['BackupJobId']} is not completed."
                recommendation = "Recommendation: Ensure all backup jobs are completed successfully."
                warn_and_store(f"{message} {recommendation}", log_messages)
    except ClientError as e:
        logger.error(f"Failed to list backup jobs: {e}")
