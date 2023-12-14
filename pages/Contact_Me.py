import streamlit as st
from send_email import send_mail

with st.form(key='contact_form'):
    username = st.text_input(label="Enter your mail address")
    option = st.selectbox("what topics you want to discuss?", ['Job inquiries', 'Project','loki'])
    raw_message = st.text_area(label="Enter Your Message")

    message = f"""\
Subject: New Mail From {username}

Mail ID: {username}
Topic : {option}
{raw_message}
"""
    button = st.form_submit_button("Submit")
    if button:
        send_mail(message)
        st.info("Your Mail Was Sent Successfully")
