from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

message = MIMEMultipart()
message["from"] = "Krinshsmith Kava"
message["to"] = "testuser@codewithmosh.com"
message["subject"] = "This is a test"
message.attach(MIMEText("Body"))

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("krinshsmithkava3@gmail.com", "krinshsmith@2407")
    smtp.send_message(message)
    print("Sent...")
