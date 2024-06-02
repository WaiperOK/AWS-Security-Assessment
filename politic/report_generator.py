# report_generator.py
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import datetime


def generate_pdf_report(filename, log_messages):
    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter
    c.drawString(100, height - 100, "AWS Pentest Report")
    c.drawString(100, height - 120, f"Date: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    y = height - 150
    for message in log_messages:
        c.drawString(100, y, message)
        y -= 20
        if y < 50:
            c.showPage()
            y = height - 50

    c.save()


# Пример использования
log_messages = [
    "Security Group sg-0123456789abcdef0 allows access from anywhere.",
    "Recommendation: Review and update the security group rules to restrict access.",
    "S3 Bucket my-bucket is publicly accessible.",
    "Recommendation: Update the bucket ACL to restrict public access.",
    "IAM User admin has overly permissive policy: AdminAccess.",
    "Recommendation: Review and update the IAM policy to follow the principle of least privilege.",
    # Добавьте другие сообщения логов
]

generate_pdf_report("aws_pentest_report.pdf", log_messages)
