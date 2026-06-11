import os
import smtplib

from email.message import EmailMessage

def send_email(text):

    email = os.environ[
        "EMAIL_ADDRESS"
    ]

    password = os.environ[
        "EMAIL_PASSWORD"
    ]

    msg = EmailMessage()

    msg["Subject"] = (
        "Morning Brief"
    )

    msg["From"] = email

    msg["To"] = email

    msg.set_content(text)

    with smtplib.SMTP_SSL(
        "smtp.gmail.com",
        465
    ) as smtp:

        smtp.login(
            email,
            password
        )

        smtp.send_message(msg)
