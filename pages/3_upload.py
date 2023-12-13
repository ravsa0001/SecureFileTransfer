import streamlit as st
import requests

st.subheader("Upload you file here!")
file = st.file_uploader("")
if file:
    filename = file
    url = "http://127.0.0.1:5000/upload"
    data = {
        "file_name" : filename
    }
    response = requests.post(url, json = data)
    
    result = response.json()
    st.warning(result["message"])