import os
from email.message import EmailMessage
import ssl
import smtplib


email_sender = 'ashumg760@gmail.com'
email_password = 'ybxztycxzqixkbuj'
email_receiver = 'ashumg01@gmail.com'

subject = 'TEST JENKINS'
body = "Service XYZ has planned maintenance on Saturday from 14:00 till 17:00 CE"

em = EmailMessage()
em['FROM'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
 smtp.login(email_sender, email_password)
 smtp.sendmail(email_sender, email_receiver, em.as_string())