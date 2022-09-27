import smtplib, ssl, os
import dotenv

dotenv.load_dotenv()
gmail = os.getenv('GMAIL')
gmail_password = os.getenv('GMAIL_PASSWORD')
# pythontoday
port = 587  # For starttls
smtp_server = "smtp.gmail.com"
sender_email = gmail
receiver_email = gmail
password = gmail_password
message = """
Subject: Hi there

This message is sent from Python."""

context = ssl.create_default_context()
with smtplib.SMTP(smtp_server, port) as server:
    server.ehlo()  # Can be omitted
    server.starttls(context=context)
    server.ehlo()  # Can be omitted
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)