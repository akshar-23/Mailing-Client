import smtplib, ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender_mail = "my@gmail.com" #email that you want to send emails from.
reciever_mail = "your@gmail.com" #email that you want to send emails to.
password = input("Enter Password: ")
smtp_server = "smtp.gmail.com" #gmail has the following SMTP server.
port = 465 #port number for ssl service

subject = "email with attachment"
body = "This is as email sent through python. It also contains an attachment"

message = MIMEMultipart()
message['To'] = reciever_mail
message['From'] = sender_mail
message['Subject'] = subject

message.attach(MIMEText(body, 'plain'))

filename = "ironman.jpg" #file path for the attachment you want to upload
with open(filename, 'rb') as attachment:
    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())

encoders.encode_base64(part)

part.add_header("Content-Disposition", f"attachment; filename= {filename}")

message.attach(part)
text = message.as_string()

context = ssl.create_default_context()

with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_mail, password)
    server.sendmail(sender_mail,reciever_mail,text)