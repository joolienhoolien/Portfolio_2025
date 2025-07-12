import streamlit as st

def menu():
    st.sidebar.page_link("home.py", label="Home")
    st.sidebar.page_link("https://www.linkedin.com/in/julien-pecquet/", label="Linkedin")
    st.sidebar.page_link("https://github.com/joolienhoolien", label="Github")
    st.sidebar.page_link("pages/contact_me.py", label="Contact Me")