import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from config import ADDRESS, PASSWORD

def send_msg(sender, to, subject, body):
    msg = MIMEMultipart()
    msg['From']=sender
    msg['To']=to
    msg['Subject']=subject
    msg.attach(MIMEText(body, 'plain'))
    s.send_message(msg)

if __name__ == '__main__':
    s = smtplib.SMTP(host='smtp.gmail.com', port=587)
    s.starttls()
    s.login(ADDRESS, PASSWORD)

    send_msg(ADDRESS,
            'albertgregoryvader@protonmail.com',
            'testing',
            'This is the body of the message.')

    s.quit()