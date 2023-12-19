import streamlit as st
import requests

st.subheader("Upload you file here!")
uploaded_file = st.file_uploader(" ", type = ["pdf", "docs", "html", "xlsx", "png", "csv", "jpg", "jpeg", "csv", "txt"])

if uploaded_file:
    # print("Inside file loaded *********************************************************************************g")
    # with open('test.png', 'wb') as f:
    #     f.write(uploaded_file.getvalue())
    
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
    