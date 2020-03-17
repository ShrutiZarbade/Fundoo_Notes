import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
from dotenv import load_dotenv
load_dotenv()


class SmtpSendMail:

    # @staticmethod
    def send_mail(self, user_email, message):

        msg = MIMEMultipart()
        message = message

        password = os.getenv('password')
        msg['From'] = os.getenv('email_from')
        msg['To'] = user_email
        msg['Subject'] = "Link"

        msg.attach(MIMEText(message, 'plain'))

        server = smtplib.SMTP('smtp.gmail.com: 587')

        server.starttls()

        server.login(msg['From'], password)

        server.sendmail(msg['From'], msg['To'], msg.as_string())

        server.quit()
        print("successfully send mail")


