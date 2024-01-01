import streamlit as st
from next_page import nav_page


st.session_state["user"] = "None"

st.title("FileSafe")

col1, col2, col3, col4, col5, col6, col7 = st.columns(7)
with col6:
    if st.button("Register"):
        nav_page("signUp")
    
with col7:
    if st.button("LogIn"):
        nav_page("logIn")

st.subheader("Here, this application is like a vault for securing your files")
st.image("/photos/vault.png")
