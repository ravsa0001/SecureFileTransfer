import streamlit as st
from pymongo import MongoClient

client = MongoClient("mongodb://127.0.0.1:27017")

datab = client.ez
file_storage = datab.files_storage

def uploaded():
    st.subheader(":green[Uploaded files]")
    files_list = ["File Name","File Link" "Download key"]
    for files in file_storage.find():
        files_list.append(files["file name"], files["file link"], files["download key"])        
    
    st.table(files_list)

# st.subheader("hello")