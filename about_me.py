import pandas
import streamlit as st


def project_block(row):
    with st.container(border = False):
        st.markdown(f"##### [{row["title"]}]({row["url"]})")
        with st.container(border = True, height = 400):
            st.markdown(row["description"])
            st.image("images/" + row["image"], width=300)

def professional_tab():
    for index, row in pandas.read_csv("prof_exp.csv").iterrows():
        col1, col2 = st.columns([1, 4], vertical_alignment="top")
        with col1:
            col1.markdown(f"{row["date"]}")
        with col2:
            col2.title(f"{row["company"]}")
            col2.markdown(f"#### `>>> {row["title"]}`")
            col2.markdown(f"{row["description"]}")
            for proj_index, proj_row in pandas.read_csv("prof_proj.csv").iterrows():
                if proj_row["company_code"] == row["company_code"]:
                    col2.markdown(f"### Client: [{proj_row["company"]}]({proj_row["url"]})")
                    col2.markdown(f"###### *`>>> {proj_row["role"]}`*")
                    col2.markdown(f"{proj_row["description"]}")
        st.divider()

def personal_tab():
    df = pandas.read_csv("pers_proj.csv", sep=';')
    col1, col2 = st.columns(2)
    count = 0
    for index, row in df.iterrows():
        if count % 2 == 0 and row["complete"] == True:
            with col1:
                project_block(row)
                count += 1
        elif count % 2 == 1 and row["complete"] == True:
            with col2:
                project_block(row)
                count += 1

def education_tab():
    df = pandas.read_csv("educ.csv")
    for index, row in df.iterrows():
        col1, col2 = st.columns([1, 4], vertical_alignment="top")
        with col1:
            col1.markdown(f"{row["date"]}")
        with col2:
            col2.title(f"{row["title"]}")
            col2.image("images/" + row["image"], width=300)
        st.divider()

def about_me():
    #About Me section
    tab_prof, tab_pers, tab_edu = st.tabs(["PROFESSIONAL EXPERIENCE", "PROJECTS", "EDUCATION & CERTIFICATION"])
    with tab_prof:
        professional_tab()
    with tab_pers:
        personal_tab()
    with tab_edu:
        education_tab()