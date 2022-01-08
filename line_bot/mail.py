import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email import encoders

def send_mail():
    email_user = "andy258741@gmail.com"
    email_password = "jchsmxnqvoxpxoiy"
    email_send = "andy258741@gmail.com"

    subject = "Test email from pi"

    msg = MIMEMultipart()
    msg["From"] = "andy258741@gmail.com"
    msg["To"] = "andy2587412gmail.com"
    msg["Subject"] = "subject"

    body = MIMEText("success feeding!!")
    msg.attach(body)
    
    body=MIMEApplication(open("/home/a108403045/Desktop/image.jpg",'rb').read())
    body.add_header('Content-Disposition','attachment',filename='test.jpg')
    msg.attach(body)

    text = msg.as_string()
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login(email_user,email_password)


    server.sendmail(email_user,email_send,text)
    server.quit()
