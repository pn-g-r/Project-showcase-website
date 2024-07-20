import streamlit as st

st.set_page_config(layout='wide')

col1, col2 = st.columns(2)

with col1:
    st.image("Images/photo.png")

with col2:
    st.title("Ardit Sulce")
    content = """
    I'am a python programmer
    """
    st.info(content)

content2 = """
below you can find python apps U built
"""

st.write(content2)