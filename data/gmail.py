import smtplib, os, dotenv
from email.mime.text import MIMEText

def send_email(user_id):
    message = f'Заявка на сделку от агента с id: {user_id}'
    dotenv.load_dotenv()
    gmail = os.getenv('GMAIL')
    gmail_password = os.getenv('PASSWORD_APP_GMAIL')
    # pythontoday
    port = 587  # For starttls
    smtp_server = "smtp.gmail.com"
    sender = gmail
    password = gmail_password
    
    server = smtplib.SMTP(smtp_server, port)
    server.starttls()
    try:
        server.login(sender, password)
        msg = MIMEText(message)
        msg['Subject'] = 'Уведомление о сделке!'
        server.sendmail(sender, sender, msg.as_string())
        return True
    except Exception as e:
        return e
