#age checker:
import  streamlit as st
st.title("Age checker")
age = st.number_input("enter your age",min_value=0, step=1)
if st.button("check"):
    if age < 18:
        st.warning("you are a minor.")
    else:
        st.success("you are an adult.") 
               