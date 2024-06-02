import boto3
import logging
import json
from colorama import Fore, Style, init

init(autoreset=True)

logger = logging.getLogger(__name__)

def get_aws_session(account_index=0):
    """
    Возвращает сессию AWS для заданного аккаунта из файла accounts.json.
    """
    with open('config/accounts.json', 'r') as f:
        accounts = json.load(f)

    if account_index >= len(accounts):
        raise IndexError("Указанный индекс аккаунта выходит за пределы списка аккаунтов.")

    account = accounts[account_index]

    return boto3.Session(
        aws_access_key_id=account['aws_access_key_id'],
        aws_secret_access_key=account['aws_secret_access_key'],
        region_name=account['region']
    )

def log_and_store(log_messages, message, level="info"):
    """
    Логирует и сохраняет сообщение.
    """
    if level == "info":
        formatted_message = f"{Fore.GREEN}[INFO] {message}{Style.RESET_ALL}"
        logger.info(formatted_message)
    elif level == "warning":
        formatted_message = f"{Fore.YELLOW}[WARNING] {message}{Style.RESET_ALL}"
        logger.warning(formatted_message)
    elif level == "error":
        formatted_message = f"{Fore.RED}[ERROR] {message}{Style.RESET_ALL}"
        logger.error(formatted_message)
    print(formatted_message)
    log_messages.append(formatted_message)

def format_report(log_messages):
    """
    Форматирует отчет для вывода в файл.
    """
    report = "\n".join(log_messages)
    return report
