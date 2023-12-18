import requests
import streamlit as st


with st.form(key = "log-in", clear_on_submit = True):
    st.subheader(":green[Log-In]")
        
    email = st.text_input(":blue[Email Id]", placeholder = "Enter your email")
    password = st.text_input(":blue[Password]", placeholder = "Password", type = "password")
        
        
    if st.form_submit_button("Submit"):
        url = "http://127.0.0.1:5000/login"
        data = {
            "email": email, "password": password
        }
        response = requests.post(url, json = data)
        result = response.json()
        st.warning(result['text'])
        
    
            