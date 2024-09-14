import streamlit as st
import pandas

st.set_page_config(layout='wide')
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

col1, empty_col1, col2, empty_col2, col3 = st.columns([2.5, 0.5, 2.5, 0.3, 2.5])

# Load the data
data = pandas.read_csv('pages/datas.csv', sep=',')

# Preview the data and check for issues
st.write(data.columns)  # Check column names
st.write(data.head())   # Preview the first few rows

# Iterate through rows and display names
with col1:
    for index, row in data[:4].iterrows():
        first_name = row.get('firstname', 'Unknown')
        last_name = row.get('lastname', 'Unknown')
        st.subheader(f"{first_name} {last_name}")
        st.write(row['role'])
        st.image('photos.zip/' + row['image'])

with col2:
    for index, row in data[4:8].iterrows():
        first_name = row.get('firstname', 'Unknown')
        last_name = row.get('lastname', 'Unknown')
        st.subheader(f"{first_name} {last_name}")
        st.write(row['role'])


with col3:
    for index, row in data[8:].iterrows():
        first_name = row.get('firstname', 'Unknown')
        last_name = row.get('lastname', 'Unknown')
        st.subheader(f"{first_name} {last_name}")
        st.write(row['role'])
