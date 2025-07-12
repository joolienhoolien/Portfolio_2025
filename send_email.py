import smtplib
import ssl
import os


def send_email(user_message):
    host = "smtp.gmail.com"
    port = 465
    username = os.getenv("PORTFOLIO_EMAIL")
    password = os.getenv("PORTFOLIO_PW")
    receiver_email = os.getenv("PORTFOLIO_EMAIL")
    context = ssl.create_default_context()
    message = user_message
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver_email, message)