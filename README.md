### **AWS-Security-Assessment**  

## **Description**  
The project is designed to automate the security assessment of AWS infrastructure. It includes **automatic scanning** of various AWS resources, **anomaly detection**, and **report generation**.  

## **Project Features**  
1. **Automated AWS Security Assessment**  
2. **Anomaly Detection in Logs**  
3. **Report Generation**  

## **Key Features**  

### **1. Automated AWS Security Assessment**  
This module performs security checks on AWS resources such as security groups, S3 buckets, IAM policies, and more. Each check is implemented in a separate file within the `politic` folder.  

#### **Security Checks:**  
- **Security Groups** (`politic/security_groups.py`) – Identifies misconfigured rules that could expose resources.  
- **S3 Buckets** (`politic/s3_config.py`) – Checks access control, encryption, and logging.  
- **IAM Policies** (`politic/iam_policies.py`) – Detects excessive permissions and policy misconfigurations.  
- **CloudTrail & CloudWatch Configurations** – Ensures proper logging and alert configurations.  
- **RDS, EC2, ELB, Lambda, VPC, and other AWS services** – Security audits for encryption, backup, access control, and compliance.  

### **2. Anomaly Detection in Logs**  
Utilizes **machine learning** to analyze logs and detect anomalies. Implemented in `ai_module.py`, it includes log preprocessing, feature extraction, and anomaly detection models.  

### **3. Report Generation**  
The `report_generator.py` module generates **PDF security reports**, summarizing all findings and recommendations.  

## **Installation**  

1. Clone the repository:  
    ```sh
    git clone <repository_url>
    cd aws_pentest
    ```  
2. Install dependencies:  
    ```sh
    pip install -r requirements.txt
    ```  
3. Configure AWS credentials in `config/accounts.json`.  

## **Usage**  

### **Run Security Assessment**  
```sh
python aws_pentest.py
```  

## **Code Overview**  

- **`aws_pentest.py`** – Main script for running security checks, generating reports, and detecting anomalies.  
- **`app.py`** – Flask-based web interface for running security tests via a browser.  
- **`ai_module.py`** – Machine learning-based log anomaly detection.  
- **`report_generator.py`** – Generates **PDF reports** with security findings.  
- **`utils.py`** – Utility functions for logging and AWS session management.
