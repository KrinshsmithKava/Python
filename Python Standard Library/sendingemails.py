from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

message = MIMEMultipart()
message["from"] = "Krinshsmith Kava"
message["to"] = "krinshkava2407@gmail.com"
message["subject"] = "This is a test"
message.attach(MIMEText("Body"))

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("krinshsmith.nivzen@gmail.com", "ghed cezv qkns gjli")
    smtp.send_message(message)
    print("Sent...")
