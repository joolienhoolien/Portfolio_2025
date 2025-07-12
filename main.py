import streamlit as st

st.set_page_config(layout="wide")

#Personal projects, education etc
col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Julien Pecquet")
    content = """
    Results-driven data integrations lead with 5 years experience in designing, developing and supporting performant 
    systems now seeking software engineering roles. 
    Proven ability to design, build and operate scalable solutions from conception to go-live. 
    Eager to apply a strong foundation in object-oriented programming to build high-quality applications.
    """
    st.info(content)