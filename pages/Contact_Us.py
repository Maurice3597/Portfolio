import streamlit as st
from Contact_fxn import send_mail,topic

st.title("Contact Our 24/7 Available Customer Service")
st.write("Fill in the form and submit")
with st.form(key='form'):
    user_email = st.text_input("Your email here:")
    subject = st.selectbox("Select the email Subject here: ",
                           options=topic())
    raw_message = st.text_area("Type your message here:")
    message = f"""\
Subject: {subject}\n
Sent from: {user_email}\n
{raw_message}
"""
    button = st.form_submit_button("Submit")

if button:
    message = message# + user_email
    send_mail(message)

st.write("OR \nCall us on phone via\t+237 (0)7017427977")