import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png", width = 500)

with col2:
    st.title("M V SIVAKUMAR")
    content = """
    This is M V SIVAKUMAR doing some python competency building,  Did MTech Embedded Systems
    and Experienced in Project Management Activity. Doing the Web Application building Python
    Programming Language, Planning IOT product development.
    """
    #st.write(content)
    st.info(content)

content2 = """
Below you can find apps that I have built
"""
st.write(content2)

col3, col4 = st.columns(2)

df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index,row in df[:10].iterrows():
        st.header(row["title"])

with col4:
    for index,row in df[10:].iterrows():
        st.header(row["title"])



