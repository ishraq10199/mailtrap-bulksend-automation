#!/usr/bin/env python

import os
import time
import mailtrap as mt
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()
API_TOKEN = os.getenv("MAILTRAP_API_TOKEN")
MAIL_SUBJECT = os.getenv("MAIL_SUBJECT")
FROM_EMAIL = os.getenv("FROM_EMAIL")
FROM_NAME = os.getenv("FROM_NAME")

with open("template.html", "r", encoding="utf-8") as f:
    html_body = f.read()

with open("plaintext.txt", "r", encoding="utf-8") as f:
    plain_text_body = f.read()

with open("emails.txt", "r", encoding="utf-8") as f:
    emails = [line.strip() for line in f if line.strip()]

os.makedirs("logs", exist_ok=True)
log_filename = f"logs/send_log_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"

client = mt.MailtrapClient(token=API_TOKEN)

with open(log_filename, "w", encoding="utf-8") as log_file:
    for email in emails:
        if email.strip() == "":
            continue
        mail = mt.Mail(
            sender=mt.Address(email=FROM_EMAIL, name=FROM_NAME),
            to=[mt.Address(email=email)],
            subject=MAIL_SUBJECT,
            text=plain_text_body,
            html=html_body,
            category="Integration Test",
        )

        try:
            response = client.send(mail)
            log_file.write(f"✅ {email} -> {response}\n")
        except Exception as e:
            log_file.write(f"❌ {email} -> {e}\n")

        log_file.flush()
        time.sleep(1)  # small delay between sends

print(f"Done. Log saved to {log_filename}")