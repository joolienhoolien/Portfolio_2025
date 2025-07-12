import smtplib
import ssl
import os
import streamlit as st


def send_email(user_message):
    host = "smtp.gmail.com"
    port = 465
    username = st.secrets["PORTFOLIO_EMAIL"]
    password = st.secrets["PORTFOLIO_PW"]
    receiver_email = st.secrets["PORTFOLIO_EMAIL"]
    context = ssl.create_default_context()
    message = user_message
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver_email, message)