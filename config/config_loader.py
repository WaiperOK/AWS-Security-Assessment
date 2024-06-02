import json
import os

def load_config():
    config_path = 'config/accounts.json'
    if not os.path.exists(config_path):
        aws_access_key_id = input("Enter AWS Access Key ID: ")
        aws_secret_access_key = input("Enter AWS Secret Access Key: ")
        region = input("Enter AWS Region: ")

        accounts = [{
            "aws_access_key_id": aws_access_key_id,
            "aws_secret_access_key": aws_secret_access_key,
            "region": region
        }]
        with open(config_path, 'w') as f:
            json.dump(accounts, f, indent=4)
        print(f"Configuration saved to {config_path}")

    with open(config_path) as f:
        accounts = json.load(f)

    sessions = []
    for account in accounts:
        session = {
            "aws_access_key_id": account["aws_access_key_id"],
            "aws_secret_access_key": account["aws_secret_access_key"],
            "region": account["region"]
        }
        sessions.append(session)
    return sessions
