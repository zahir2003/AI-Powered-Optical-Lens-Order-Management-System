import os
import smtplib
from dotenv import load_dotenv
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

load_dotenv()

SENDER_EMAIL = os.getenv("SENDER_EMAIL")
APP_PASSWORD = os.getenv("APP_PASSWORD")
RECEIVER_EMAIL = os.getenv("RECEIVER_EMAIL")


def send_alert_email(order, confidence):

    subject = f"🚨 High Risk Order Alert - Order #{order.id}"

    body = f"""
AI-Powered Order Management System

High Risk Order Detected

Order ID: {order.id}
Customer: {order.customer_name}
Status: {order.status}

Confidence: {confidence}%
SLA Hours: {order.sla_hours}
Elapsed Hours: {order.elapsed_hours}

Immediate attention required.
"""

    msg = MIMEMultipart()
    msg["From"] = SENDER_EMAIL
    msg["To"] = RECEIVER_EMAIL
    msg["Subject"] = subject

    msg.attach(MIMEText(body, "plain"))

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(SENDER_EMAIL, APP_PASSWORD)
    server.send_message(msg)
    server.quit()
