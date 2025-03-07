import streamlit as st
import pandas

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

context2="I have listed all the apps that can be use later, you can use any app once everything is developed"

st.write(context2)

col3,empty,col4=st.columns([1.5,0.5,1.5])
list1=pandas.read_csv("data.csv",sep=";")
with col3:
    for index,list2 in list1[0:10].iterrows():
        st.header(list2["title"])
        st.write(list2["description"])
        st.image("images/" + list2['image'] )
        st.write(f"[App Link]({list2['url']})")
with col4:
    for index,list2 in list1[10:20].iterrows():
        st.header(list2["title"])
        st.write(list2["description"])
        st.image("images/" + list2['image'])
        st.write(f"[App Link]({list2['url']})")

