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
    I am a skilled and motivated Software Engineer with a strong foundation in Computer Science and *`5 years of professional experience`*
    in building elegant and effective multi-platform solutions. My expertise spans a variety of technologies, including \
    *`Boomi, Python, PostgreSQL, React, Docker.`* I have successfully led development of large scale EDI implementations \
    utilizing both *`RESTful APIs and legacy endpoints.`*\n
    Through this experience coupled with my academic work and current projects, I aim to transition into a position where I can \
    utilize my commitment to innovation to create meaningful differences in users lives.
    """
    with st.container(border = True):
        st.markdown(f"{content}")