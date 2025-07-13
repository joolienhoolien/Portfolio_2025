import pandas
import streamlit as st


def about_me():
    df = pandas.read_csv("data.csv", sep=';')
    prof_df, pers_df, edu_df = [], [], [] #TODO: Would make more sense as a dictionary
    for index, row in df.iterrows():
        if row["context"] == "professional_title":
            prof_df.append(row)
        elif row["context"] == "professional_project":
            prof_df.append(row)
        elif row["context"] == "personal":
            pers_df.append(row)
        elif row["context"] == "education":
            edu_df.append(row)

    #About Me section
    st.markdown("## What would you like to know about me?")
    tab_prof, tab_pers, tab_edu = st.tabs(["PROFESSIONAL EXPERIENCE", "PROJECTS", "EDUCATION & CERTIFICATION"])
    with tab_prof:
        for index, row in pandas.read_csv("prof_exp.csv").iterrows():
            col1, col2 = st.columns([1,4], vertical_alignment="top")
            with col1:
                col1.markdown(f"{row["date"]}")
            with col2:
                col2.title(f"{row["company"]}")
                col2.markdown(f"##### {row["title"]}")
                for proj_index, proj_row in pandas.read_csv("prof_proj.csv").iterrows():
                    if proj_row["company_code"] == row["company_code"]:
                        col2.markdown(f"""
                        #### {proj_row["company"]}
                        **{proj_row["role"]}**\n
                        {proj_row["description"]}
                        """)
            st.divider()


    with tab_pers:
        df = pandas.read_csv("data.csv", sep=';')
        left_col, right_col = st.columns(2)
        for index, row in df.iterrows():
            if row["context"] == "personal":
                if not index % 2:
                    with left_col:
                        st.header(row["title"])
                        st.write(row["description"])
                        st.image("images/" + row["image"])
                        st.write("[Source Code]("+ row["url"] + ")")
                else:
                    with right_col:
                        st.header(row["title"])
                        st.write(row["description"])
                        st.image("images/" + row["image"])
                        st.write("[Source Code]("+ row["url"] + ")")


    with tab_edu:
        df = pandas.read_csv("data.csv", sep=';')
        for index, row in df.iterrows():
            if row["context"] == "education":
                st.header(row["title"])