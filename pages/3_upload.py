import streamlit as st
import requests


if st.session_state["user"] == "None":
    st.header("Log-In first to get access for this page")

elif st.session_state["user"] == "Operation":
    st.subheader("Upload your file here!")
    uploaded_file = st.file_uploader(" ", type = ["pdf", "docs", "html", "xlsx", "png", "csv", "jpg", "jpeg", "csv", "txt"])

    if uploaded_file:
        
        byte_value = uploaded_file.getvalue()
        byte_string = str(byte_value, encoding = "latin-1")
        # byte_string = byte_value.decode("utf-8")
        
        url = "http://127.0.0.1:5000/upload" 
        data = {
            "file_name": uploaded_file.name, 
            "file_type": uploaded_file.type,
            "uploaded_file": byte_string
        }
        response = requests.post(url, json = data)
        
        result = response.json()
        st.write(result["message"])

else:
    st.header("You are logged in as a Client User, So you are unable to upload any files")