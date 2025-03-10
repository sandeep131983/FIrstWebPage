import streamlit as st
import sendemail

st.header("Contact Me")
with st.form(key="contactme"):
    textinput=st.text_input("Enter your email")
    desc=st.text_area("Descrption",key="desc")
    button=st.form_submit_button("Submit")

message=f"""\
Subject:"Email from web page"

From:{textinput}
{desc}
"""
if button:
    sendemail.email(message)





