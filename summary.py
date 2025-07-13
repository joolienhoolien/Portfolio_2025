import pandas
import streamlit as st

def summary():
    # Summary section
    col1, col2 = st.columns([1, 2], vertical_alignment="top")
    with col1:
        st.image(width=300, image="images/photo.png")

    with col2:
        st.markdown("# Julien Pecquet")
        st.markdown("##### `>>> Data Integrator -> Software Engineer`")
    content = """
    Results-driven data integrations lead with 5 years experience in designing, developing and supporting performant 
    systems now seeking software engineering roles. \n
    Proven ability to design, build and operate scalable solutions from conception to go-live. 
    Eager to apply a strong foundation in object-oriented programming to build high-quality applications.
    """
    with st.container(border = True):
        st.markdown(content)