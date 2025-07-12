import streamlit as st

st.set_page_config(layout="wide")

#Personal projects, education etc
col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

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
    st.link_button("Github", "https://github.com/joolienhoolien")
    st.link_button("Linkedin", "https://www.linkedin.com/in/julien-pecquet/")

st.markdown("## What would you like to know about me?")

expand_professional = st.expander("Professional Experience", icon=":material/info:")
long_text = "Lorem ipsum. " * 1000
with expand_professional:
    with st.container(height=300):
        st.markdown(long_text)
        expand_professional.write("Inside the expander.")

expand_projects = st.expander("Personal Projects", icon=":material/info:")
expand_projects.write("Inside the expander.")

expand_education = st.expander("Education & Certificates", icon=":material/info:")
expand_education.write("Inside the expander.")