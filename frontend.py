import streamlit as st
import re
import requests


def validate_email(email):
    pattern = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$ "
    
    if re.match(pattern, email):
        return True
    return False
    

def signUp():
    with st.form(key = "sign-up", clear_on_submit = True):
        st.subheader(":green[Sign-Up]")

        user_name = st.text_input(":blue[Name]", placeholder = "Enter your name")
        email = st.text_input(":blue[Email]", placeholder = "Enter your email")
        # if validate_email(email):
        #     pass
        # else:
        #     st.warning("Invalid email address")
        
        password1 = st.text_input(":blue[Password]", placeholder = "Password", type = "password")
        password2 = st.text_input(":blue[Confirm Password]", placeholder = "Password", type = "password")  
        if len(password1) >= 6:
            if password1 != password2:
                st.warning(":red[Password must be same]")
        else: 
            st.warning("password is too short")
                    
        sel = ["Client", "Operation"]
        selection = st.selectbox("Select", sel, index = 0)
        
        if st.form_submit_button("Submit"):
            url = "http://127.0.0.1:5000/signup"
            data={
                "username": user_name,
                "email":email,
                "password":password1,
                "password2":password2,
                "user": selection
            }
            response = requests.post(url,json=data)
            result = response.json()
            st.warning(result["text"])

def uploaded():
    st.subheader(":green[Uploaded files]")
    
def upload():
    st.subheader("Upload you file here!")
    file = st.file_uploader("")
    if file:
        url = "http://127.0.0.1:5000/upload"
        data = {
            "file_name" : file
        }
        response = requests.post(url, json = data)
        result = response.json()
        st.warning(result["message"])

def logIn():
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
            
            if result["user"] == "client":
                uploaded()
                
            elif result["user"] == "operation":
                upload()