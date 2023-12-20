import streamlit as st
from pymongo import MongoClient
import requests


client = MongoClient("mongodb://127.0.0.1:27017")

datab = client.ez
file_storage = datab.files_storage

if st.session_state["user"] == "None":
    st.header("Log-In first to get acces for this page")

def click():
    for keys in st.session_state:
        if keys.startswith("But"):
            if st.session_state[keys]:
                name_key = int(keys[-1])
                url = "http://127.0.0.1:5000/uploaded_files"
                data = {"index": name_key}
                
                response = requests.post(url, json = data)
                result = response.json()

                filedata = result["filedata"]
                uploaded_file = bytes(filedata, "utf-8")
                file_name = result["file_name"]
                
                with col3:      
                        st.download_button(f"Downlaod {file_name}", uploaded_file, file_name = file_name)

if st.session_state["user"] != "None":
    st.header("All files")

    col1, col2, col3 = st.columns(3)

    with col1:
        for files in file_storage.find():
            names = files["file name"]
            st.subheader(names, divider = True)
            
    with col2:
        names_list = []
        for files in file_storage.find():
            names = files["file name"]
            names_list.append(names)
        
        for i in range(0, len(names_list)):
            st.button("Click here", key = f"Button{i}", on_click =  click)
            st.write(" ")
        
    
