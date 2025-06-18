import streamlit as st
import datetime

#Check Marks
marks = st.number_input("Enter Marks: ", min_value=0, max_value=100, value=0, step=1)

if marks >= 80 :
    st.write("Excellent")
elif marks >= 50 and marks <= 79 :
    st.write("Good")
elif marks < 50 :
    st.write("Fail")

#Voting
x = datetime.datetime.now()
current_year = x.year

birth_year = st.number_input("Enter Year of Birth: ", min_value=1900, max_value=2025, value=2000, step=1)
age = current_year - birth_year

st.write(f"Your age is: {age}")

if age >= 18 :
    st.write("You are allowed to vote")
else:
    st.write("You are not allowed to vote")