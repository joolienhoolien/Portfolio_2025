import streamlit as st
import pandas


st.set_page_config(page_title="Julien Pecquet Portfolio", layout="centered")

#Personal projects, education etc
col1, col2 = st.columns([1,2],vertical_alignment="top")

with col1:
    st.image(width=300, image="images/photo.png")
    with st.container():
        social_col1, social_col2 = st.columns(2, gap=None)
        with social_col1:
            st.link_button("Github", "https://github.com/joolienhoolien")
        with social_col2:
            st.link_button("Linkedin", "https://www.linkedin.com/in/julien-pecquet/")

with col2:
    st.title("Julien Pecquet")
    st.markdown("##### Data Integrator -> Full-Stack Developer")
    content = """
    Results-driven data integrations lead with 5 years experience in designing, developing and supporting performant 
    systems now seeking software engineering roles. 
    Proven ability to design, build and operate scalable solutions from conception to go-live. 
    Eager to apply a strong foundation in object-oriented programming to build high-quality applications.
    """
    st.info(content)

st.divider()
st.markdown("## What would you like to know about me?")

expand_professional = st.expander("Professional Experience", icon=":material/info:")
with expand_professional:
    expand_professional.write("Inside the expander.")
    with st.container(height=300):
        #long_text = "Lorem ipsum. " * 1000
        #st.markdown(long_text)
        df = pandas.read_csv("data.csv", sep=';')
        for index, row in df.iterrows():
            if row["context"] == "professional":
                st.header(row["title"])

#TODO: Add area for tech stack
#TODO: Allow pill buttons to filter list by tech

expand_projects = st.expander("Personal Projects", icon=":material/info:")
with expand_projects:
    expand_projects.write("Inside the expander.")
    with st.container(height=300):
        #long_text = "Lorem ipsum. " * 1000
        #st.markdown(long_text)
        df = pandas.read_csv("data.csv", sep=';')
        for index, row in df.iterrows():
            if row["context"] == "personal":
                st.header(row["title"])

expand_education = st.expander("Education & Certificates", icon=":material/info:")
with expand_education:
    expand_education.write("Inside the expander.")
    with st.container(height=300):
        #long_text = "Lorem ipsum. " * 1000
        #st.markdown(long_text)
        df = pandas.read_csv("data.csv", sep=';')
        for index, row in df.iterrows():
            if row["context"] == "education":
                st.header(row["title"])