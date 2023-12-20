import requests
import streamlit as st
import re
from next_page import nav_page
from cryptography.fernet import Fernet

def validate_email(email):
    pattern = "^[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+$"
    
    if re.match(pattern, email):
        return True
    return False

with st.form(key = "sign-up", clear_on_submit = True):
    st.subheader(":green[Sign-Up]")

    user_name = st.text_input(":blue[Name]", placeholder = "Enter your name")
    email = st.text_input(":blue[Email]", placeholder = "Enter your email")
    if email != "":    
        if validate_email(email):
            pass
        else:
            st.error("Invalid email address")
        
    password1 = st.text_input(":blue[Password]", placeholder = "Password", type = "password")
    password2 = st.text_input(":blue[Confirm Password]", placeholder = "Password", type = "password")  
    if password1 != "" and len(password1) >= 6:
        if password1 != password2:
            st.error(":red[Password must be same]")
    elif password1 != ""and len(password1) < 6:
        st.error("password is too short")
                   
    if password1 != password2:
        st.warning(":red[Password must be same]")
    
    user_options = ["Client", "Operation"]
    user = st.selectbox("Register as ", user_options, index = 0)
        
    if st.form_submit_button("Submit"):
        if user == "Operation":
            key = Fernet.generate_key()
            str_key = str(key, encoding = "utf-8")
            
            url = "http://127.0.0.1:5000/signup_operation"
            data= {
                "username": user_name,
                "email":email,
                "password":password1,
                "password2":password2,
                "user": user,
                "key": str_key
            }
            response = requests.post(url,json = data)

            result = response.json()
            st.write(result["text"])
            
            # nav_page("logIn")
            
        
        if user == "Client":
            url = "http://127.0.0.1:5000/signup_client"
            data = {
                "username": user_name, 
                "email":email,
                "password":password1,
                "password2":password2,
                "user": user
            }   
            response = requests.post(url, json = data)
            # print(response)
            result = response.json()
            st.write(result["message"])
            
        