import streamlit as st
import pandas

st.set_page_config(layout='wide')

col1, col2 = st.columns(2)

with col1:
    st.image("Images/photo.png")

with col2:
    st.title("Ardit Sulce")
    content = """
    I'am a python programmer. Python's syntax is clean and easy to understand, 
    making it perfect for beginners and experts alike. 
    This simplicity allows me to focus on solving problems rather than deciphering the programming language itself. 
    It's like writing out my thoughts directly into code.
    """
    st.info(content)

content2 = """
below you can find python apps U built
"""

st.write(content2)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("Images/" + row["image"])
        st.write(f"[Source code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("Images/" + row["image"])
        st.write(f"[Source code]({row['url']})")