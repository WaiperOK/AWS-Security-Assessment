# AWS-Security-Assessment

## Описание

Проект предназначен для автоматизации оценки безопасности AWS инфраструктуры. Он включает автоматическое сканирование различных ресурсов AWS, обнаружение аномалий, генерацию отчетов и возможность взаимодействия через веб-интерфейс.

## Функционал проекта

1. **Автоматическая оценка безопасности AWS**
2. **Обнаружение аномалий в логах**
3. **Генерация отчетов**

## Структура проекта

```plaintext
aws_pentest/
├── config/
│   └── accounts.json
├── politic/
│   ├── ai_module.py
│   ├── apigateway_config.py
│   ├── backups_check.py
│   ├── cloudfront_config.py
│   ├── cloudtrail_config.py
│   ├── cloudwatch_config.py
│   ├── config_rules.py
│   ├── containers_check.py
│   ├── data_visualization.py
│   ├── dynamodb_config.py
│   ├── ec2_instances_check.py
│   ├── ebs_config.py
│   ├── elb_config.py
│   ├── iam_policies.py
│   ├── iam_roles.py
│   ├── kms_check.py
│   ├── lambda_config.py
│   ├── logging_monitoring_check.py
│   ├── mfa_check.py
│   ├── network_acl_check.py
│   ├── organizations_check.py
│   ├── report_generator.py
│   ├── rds_config.py
│   ├── s3_config.py
│   ├── security_groups.py
│   ├── security_hub.py
│   ├── sqs_config.py
│   ├── tags_check.py
│   ├── vpc_config.py
│   ├── vpc_endpoints_check.py
│   └── utils.py
├── aws_pentest.py
├── app.py
├── requirements.txt
└── templates/
    └── index.html
```

## Основные функции

### 1. Автоматическая оценка безопасности AWS
Этот модуль включает различные проверки безопасности AWS ресурсов, таких как группы безопасности, ведра S3, политики IAM и другие. Каждая проверка реализована в отдельном файле внутри папки `politic`.

#### Проверки безопасности:

1. **Security Groups** (`politic/security_groups.py`):
    Проверяет настройки групп безопасности для обнаружения неправильно настроенных правил, которые могут сделать ресурсы уязвимыми.

2. **S3 Buckets** (`politic/s3_config.py`):
    Проверяет конфигурацию ведер S3, включая права доступа, шифрование и журналы аудита.

3. **IAM Policies** (`politic/iam_policies.py`):
    Проверяет политики IAM на предмет чрезмерных прав и неправильно настроенных политик.

4. **CloudTrail Configuration** (`politic/cloudtrail_config.py`):
    Проверяет настройки CloudTrail для обеспечения правильного ведения журналов и аудита действий в аккаунте.

5. **CloudWatch Configuration** (`politic/cloudwatch_config.py`):
    Проверяет конфигурацию CloudWatch для мониторинга критических метрик и настройки тревог.

6. **VPC and Subnet Configuration** (`politic/vpc_config.py`):
    Проверяет настройки VPC и подсетей на предмет правильной сегментации и настройки безопасности.

7. **RDS Configuration** (`politic/rds_config.py`):
    Проверяет настройки баз данных RDS, включая шифрование, резервное копирование и сетевую безопасность.

8. **Lambda Functions** (`politic/lambda_config.py`):
    Проверяет конфигурацию функций Lambda, включая права доступа и настройки среды выполнения.

9. **API Gateway Configuration** (`politic/apigateway_config.py`):
    Проверяет настройки API Gateway для обеспечения безопасности API.

10. **EBS Volumes** (`politic/ebs_config.py`):
    Проверяет конфигурацию томов EBS, включая шифрование и резервное копирование.

11. **ELB Configuration** (`politic/elb_config.py`):
    Проверяет настройки балансировщиков нагрузки (ELB) для обеспечения безопасности и правильного распределения трафика.

12. **DynamoDB Configuration** (`politic/dynamodb_config.py`):
    Проверяет настройки DynamoDB, включая шифрование и управление доступом.

13. **SQS Configuration** (`politic/sqs_config.py`):
    Проверяет конфигурацию очередей SQS для обеспечения безопасности сообщений.

14. **CloudFront Distributions** (`politic/cloudfront_config.py`):
    Проверяет настройки CloudFront для обеспечения безопасности и производительности распределения контента.

15. **AWS Config Rules** (`politic/config_rules.py`):
    Проверяет конфигурацию правил AWS Config для обеспечения соответствия политикам безопасности.

16. **IAM Roles** (`politic/iam_roles.py`):
    Проверяет настройки ролей IAM на предмет правильного управления доступом.

17. **MFA Configuration** (`politic/mfa_check.py`):
    Проверяет настройку многофакторной аутентификации (MFA) для повышения безопасности учетных записей.

18. **Security Hub Findings** (`politic/security_hub.py`):
    Проверяет результаты сканирования AWS Security Hub для выявления уязвимостей и нарушений политики.

19. **Backups** (`politic/backups_check.py`):
    Проверяет настройки резервного копирования для различных сервисов AWS.

20. **Resource Tags** (`politic/tags_check.py`):
    Проверяет теги ресурсов для обеспечения их правильного управления и учета.

21. **VPC Endpoints** (`politic/vpc_endpoints_check.py`):
    Проверяет настройки конечных точек VPC для обеспечения безопасности и производительности.

22. **Organizations** (`politic/organizations_check.py`):
    Проверяет настройки AWS Organizations для управления несколькими аккаунтами AWS.

23. **Network ACLs** (`politic/network_acl_check.py`):
    Проверяет настройки сетевых ACL для обеспечения безопасности сетевого трафика.

24. **EC2 Instances** (`politic/ec2_instances_check.py`):
    Проверяет конфигурацию экземпляров EC2 для обеспечения безопасности и производительности.

25. **Logging and Monitoring** (`politic/logging_monitoring_check.py`):
    Проверяет настройки логирования и мониторинга для обеспечения полного учета действий в аккаунте.

26. **Containers** (`politic/containers_check.py`):
    Проверяет настройки контейнеров ECS/EKS для обеспечения безопасности и производительности.

### 2. Обнаружение аномалий в логах
Используется машинное обучение для анализа логов и выявления аномалий. В `ai_module.py` реализованы функции для предобработки логов, извлечения признаков и анализа на наличие аномалий.

### 3. Генерация отчетов
Генерация отчетов осуществляется модулем `report_generator.py`. Отчеты создаются в формате PDF и содержат результаты всех проверок безопасности.

## Установка

1. Клонируйте репозиторий:
    ```sh
    git clone <repository_url>
    cd aws_pentest
    ```

2. Установите зависимости:
    ```sh
    pip install -r requirements.txt
    ```

3. Настройте AWS учетные данные в файле `config/accounts.json`.

## Запуск

### Запуск проверки безопасности

Для запуска проверки безопасности:
```sh
python aws_pentest.py
```

## Структура кода

### aws_pentest.py

Основной скрипт для запуска всех проверок безопасности. Включает выполнение всех модулей проверки, генерацию отчетов и обнаружение аномалий.

### app.py

Скрипт для запуска веб-интерфейса на Flask. Позволяет пользователям запускать проверки безопасности через браузер.

### config/accounts.json

Файл конфигурации с учетными данными AWS.

### Политические модули

Каждый модуль в папке `politic` отвечает за определенный аспект безопасности AWS, такие как группы безопасности, ведра S3, политики IAM и другие.

### ai_module.py

Модуль для анализа логов с использованием машинного обучения для обнаружения аномалий.

### report_generator.py

Модуль для генерации PDF отчетов о результатах проверок безопасности.

### utils.py

Утилиты, используемые в других модулях, такие как логгирование и получение сессий AWS.
