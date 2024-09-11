import streamlit as st
import pandas

st.set_page_config(layout='wide')
col1, col2 = st.columns(2)
with col1:
    st.image('images/photo.jpg', width=200)

with col2:
    st.header("Maurice Tchouncha")
    about = """I am an Electronics engineering student from the university of Uyo, Nigeria.
    I am an upcoming data science engineer in python.
     I love programming in python and also love building applications with python"""
    st.info(about)

info = """Below are some apps I have build with python
Feel free to contact me for further enquiries"""
st.write(info)
