import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png", width = 400)

with col2:
    st.title("M V SIVAKUMAR")
    content = """
    This is M V SIVAKUMAR doing some python competency building
    """
    #st.write(content)
    st.info(content)

