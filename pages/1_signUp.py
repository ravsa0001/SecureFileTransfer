import requests
import streamlit as st
import re

def validate_email(email):
    pattern = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$ "
    
    if re.match(pattern, email):
        return True
    return False


user_options = ["Client", "Operation"]
user = st.sidebar.selectbox("Regiester as: ", user_options, index = 0)

with st.form(key = "sign-up", clear_on_submit = True):
    st.subheader(":green[Sign-Up]")

    user_name = st.text_input(":blue[Name]", placeholder = "Enter your name")
    email = st.text_input(":blue[Email]", placeholder = "Enter your email")
    if email != "":    
        if validate_email(email):
            pass
        else:
            st.warning("Invalid email address")
        
    password1 = st.text_input(":blue[Password]", placeholder = "Password", type = "password")
    password2 = st.text_input(":blue[Confirm Password]", placeholder = "Password", type = "password")  
    if len(password1) >= 6:
        if password1 != password2:
            st.warning(":red[Password must be same]")
    else: 
        st.warning("password is too short")
                   
    if password1 != password2:
        st.warning(":red[Password must be same]")
    
    # sel = ["Client", "Operation"]
    # user = st.selectbox("Select", sel, index = 0)
        
    if st.form_submit_button("Submit"):
        if user == "Operation":
            url = "http://127.0.0.1:5000/signup_operation"
            data= {
                "username": user_name,
                "email":email,
                "password":password1,
                "password2":password2,
                "user": selection
            }
            response = requests.post(url,json = data)

            result = response.json()
            st.warning(result["text"])
        
        if user == "Client":
            url = "http://127.0.0.1:5000/signup_client"
            data = {
                "username": user_name, 
                "email":email,
                "password":password1,
                "password2":password2,
                "user": selection
            }
            response = requests.post(url, json = data)
            
            result = response.json()
            st.warning(result["message"])
            
            