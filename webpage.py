import streamlit as st


col1,col2=st.columns(2)
with col1:
    st.image("images/photo.png")
with col2:
    st.header("My First Web page")
    content="""My Name is Sandeep and this is my first webpage ,
    and i am learning Python and i will have to cmplete by end of
    april and do more apps by then"""
    st.write(content)
###Alternate Method to write text on webpage as below
##st.text("I have listed examples below which can be vieweed later")"""

context2="I have listed examples below which can be vieweed later"

st.write(context2)

