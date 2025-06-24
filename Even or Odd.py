#Even or odd checker:
import streamlit as st
st.title("Even or Odd checker")
num = st.number_input("Enter an interger", step=1, format=%d")
if st.button("check"):
    if int(num) % 2 == 0:
        st.success("Even Number")
    else:
        st.warning("Odd Number")