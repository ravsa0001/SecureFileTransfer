import streamlit as st
import requests
import json 

st.subheader("Upload you file here!")
file = st.file_uploader("")
json.dumps(file)

if file:
    url = "http://127.0.0.1:5000/upload"
    response = requests.post(url, )
    
    data = {
        "file_name" : filename
    }
    response = requests.post(url, json = data)
    
    result = response.json()
    st.warning(result["message"])