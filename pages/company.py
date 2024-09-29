import streamlit as st
import pandas

st.title("GO-CITY GLOBAL")
st.header("ABOUT GO-CITY GLOBAL")
info = """
GO-CITY GLOBAL is a dynamic tech company specializing in bespoke programming solutions,
website development, and application creation for businesses and individuals.
Our team of skilled developers and designers is dedicated to bringing ideas to life
through innovative and user-friendly digital experiences.
We pride ourselves on understanding our clients' unique needs, ensuring that every
project we undertake is tailored to deliver maximum impact and functionality.
Whether you’re looking to launch a new website, develop a custom app, or enhance your
digital presence, GO-CITY GLOBAL is your trusted partner in navigating the ever-evolving
tech landscape. Together, we are empowering businesses to thrive in the digital age.
"""
st.info(info)
st.subheader("Our Team")

col1, empty_col1, col2, empty_col2, col3 = st.columns([1.2, 0.2, 1.2, 0.2, 1.2])

data = pandas.read_csv('pages/Data.csv', sep=',')

with col1:
    for index, row in data[:3].iterrows():
        st.subheader(f"{row['First_name']} {row['Last_name']}")
        st.write(row['Role'])
        st.image(f"pages/photo/{row['Image']}")

with col2:
    for index, row in data[3:6].iterrows():
        st.subheader(f"{row['First_name']} {row['Last_name']}")
        st.write(row['Role'])
        st.image(f"pages/photo/{row['Image']}")
        st.write(3*"\n")


with col3:
    for index, row in data[6:].iterrows():
        st.subheader(f"{row['First_name']} {row['Last_name']}")
        st.write(row['Role'])
        st.image(f"pages/photo/{row['Image']}")

