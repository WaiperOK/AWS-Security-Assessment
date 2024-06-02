import boto3
from botocore.exceptions import ClientError
import logging

logger = logging.getLogger(__name__)


def warn_and_store(message, log_messages):
    logger.warning(message)
    log_messages.append(message)


def check_containers(log_messages, session):
    ecs = session.client('ecs')
    try:
        response = ecs.list_clusters()
        for cluster_arn in response['clusterArns']:
            services_response = ecs.list_services(cluster=cluster_arn)
            for service_arn in services_response['serviceArns']:
                service = ecs.describe_services(cluster=cluster_arn, services=[service_arn])['services'][0]
                if 'networkConfiguration' in service:
                    for config in service['networkConfiguration']['awsvpcConfiguration']['assignPublicIp']:
                        if config == 'ENABLED':
                            message = f"ECS service {service['serviceName']} in cluster {cluster_arn} has public IP assignment enabled."
                            recommendation = "Recommendation: Disable public IP assignment for ECS services to enhance security."
                            warn_and_store(f"{message} {recommendation}", log_messages)
    except ClientError as e:
        logger.error(f"Failed to describe ECS services: {e}")

    eks = session.client('eks')
    try:
        response = eks.list_clusters()
        for cluster_name in response['clusters']:
            cluster = eks.describe_cluster(name=cluster_name)['cluster']
            if cluster['resourcesVpcConfig']['endpointPublicAccess']:
                message = f"EKS cluster {cluster_name} has public endpoint access enabled."
                recommendation = "Recommendation: Disable public endpoint access for EKS clusters to enhance security."
                warn_and_store(f"{message} {recommendation}", log_messages)
    except ClientError as e:
        logger.error(f"Failed to describe EKS clusters: {e}")
