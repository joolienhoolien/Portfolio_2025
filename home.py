import streamlit as st
import pandas
from menu import menu
from about_me import about_me
from summary import summary
#TODO: Add area for tech stack
#TODO: Allow pill buttons to filter list by tech
#TODO: Make the images smaller
#TODO: Add data and some previous apps
    #TODO: Add gifs and maybe source code for games
    #TODO: How do I add work experience?
#TODO: Update pfp
#TODO: Featured projects
#TODO: new .csv for education, and projects separated from work titles
#TODO: how to make certain text the stylesheets highlighted color
#TODO: clean code

#Page set up
st.set_page_config(page_title="Julien Pecquet Portfolio", layout="centered")

#Page
with open("style.css") as css:
    st.markdown(f'<style>{css.read()}</style>', unsafe_allow_html=True)
    menu()

    #Construct page
    summary()
    about_me()