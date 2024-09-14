import streamlit as st
from Contact_fxn import send_mail,topic

with st.form(key='form'):
    user_email = st.text_input("Your email here:")
    subject = st.selectbox("Select the email Subject here: ",
                           options=topic())
    raw_message = st.text_area("Type your message here:")
    message = f"""\
Subject: {subject}

{raw_message}
"""
    button = st.form_submit_button("Submit")

if button:
    message = message + user_email
    send_mail(message, user_email)