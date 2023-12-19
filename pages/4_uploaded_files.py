import streamlit as st
from pymongo import MongoClient

client = MongoClient("mongodb://127.0.0.1:27017")

datab = client.ez
file_storage = datab.files_storage

st.header("All files")

col1, col2, col3 = st.columns(3)

with col1:
    for files in file_storage.find():
        # st.write(files["file name"])
        names = files["file name"]
        # st.markdown("""<style> .big-font { font-size:15px !important;}
        #     </style> """, unsafe_allow_html=True)
        # st.markdown(f'<p class="big-font">{names} </p>', unsafe_allow_html=True)
        st.subheader(names, divider = True)
        # pass
    
with col2:
    for files in file_storage.find():
        path = files["file link"]
        file_name = files["file name"]
        with open(path, "rb") as f:
            st.download_button("Download", path, file_name = file_name)
            st.write(" ")



# st.subheader(":green[Uploaded files]")
# files_list = ["File Name","Download key"]
# for files in file_storage.find():
#     files_list.append(files["file name"])        
#     files_list.append(files["download key"])
    
# st.table(files_list)

# for files in file_storage.find():
#     name = files["file name"]
#     st.download_button(f"To download file {name}", file_name = files)
    
    
    
    
# st.subheader("hello")