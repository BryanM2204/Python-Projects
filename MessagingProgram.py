import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(recipient, subject, body):
    port = 465
    smtp_server = "smtp.gmail.com"
    sender_email = "bryan.m.bot@gmail.com"
    password = 'vwhmmiuailrduzxp'
    
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['Subject'] = subject
    
    body = MIMEText(body)
    msg.attach(body)

    server = smtplib.SMTP_SSL(smtp_server, port)
    server.login(sender_email, password)
    server.sendmail(sender_email, recipient, msg.as_string())
    server.quit()

recipient = input('Recipient:\n')
subject = input('Subject:\n')
body = input('Body:\n')

send_email(recipient, subject, body)