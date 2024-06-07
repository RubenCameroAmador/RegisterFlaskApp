import smtplib
import os
from dotenv import load_dotenv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class MailSend():
    def __init__(self):
        load_dotenv()
        self.sender = os.getenv('EMAIL_USER')
        self.password = os.getenv('EMAIL_PASSWORD')
    
    def send_email(self, email_recipient, otp_code):

        try:
            subject = 'DOMI: Confirm the OTP code'
            msg = MIMEMultipart()
            msg['Subject'] = subject
            msg['From'] = self.sender
            msg['To'] = email_recipient

            #with open('../Templates/email.html','r') as archivo:
            #    html = archivo.read()
            html = f"<html>Su código OTP es: {otp_code}</html>"

            msg.attach(MIMEText(html, 'html'))

            server = smtplib.SMTP('smtp.gmail.com',587)
            server.starttls()
            server.login(self.sender, self.password)

            server.sendmail(self.sender,
                            email_recipient,
                            msg.as_string())
            server.quit()
        except Exception as e:
            print(f"Error al enviar el correo electrónico: {e}")
