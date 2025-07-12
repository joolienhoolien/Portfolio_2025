import streamlit as st
from menu import menu
from send_email import send_email

menu()

st.header("Contact Me")
with st.form(key = "email_form"):
    user_email = st.text_input("Your email address...")
    email_body = st.text_area("Enter your email body...")
    message = f"""\
Subject: New Email from {user_email} on Portfolio Website

From: {user_email}

{email_body}
    """
    submit_button = st.form_submit_button("Submit")
    if submit_button:
        send_email(message)
        st.info("Email sent!")