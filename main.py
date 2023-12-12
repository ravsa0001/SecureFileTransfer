import streamlit as st
from streamlit_option_menu import option_menu
from frontend import signUp
from frontend import logIn


placeholder = st.empty()

with placeholder.container():
    st.title("HOme - FileSafe")

    btn1, btn2 = st.columns([1, 2])
    btn1 = st.button("Sign-Up")
    btn2 = st.button("Log-In")

    if btn1:
        placeholder.empty()
        st.write("Raghav")

    elif btn2:
        placeholder.empty()
        st.write("Saini")



# st.write(file)

# placeholder = st.empty()

# with placeholder.container():
#     st.title("Home- FileSafe")
    
#     btn1, btn2 = st.columns([1, 2])
#     btn1 = st.button("Sign-Up")
#     btn2 = st.button("Log-In")
    
#     if btn1:
#         placeholder.empty()
#         st.write("Sign-Up")
#         # signUp()
#     elif btn2:
#         placeholder.empty()
#         logIn()








# # st.button("Submit",on_click=nextpage,disabled=(st.session_state.page > 3))

# st.header(":green[Home - FileSafe]")

# if st.session_state.page == 0:
#     # select = st.selectbox("", ["Sign-Up", "Log-In"])
#     # if select == "Sign-Up":
#     #     signUp()
#     # elif select == "Login-In":
#     signUp()    
    
# elif st.session_state.page == 1:
#     logIn()
    
# else:
#     pass





# with st.sidebar:
#     st.header("Home")
    
#     select = st.sidebar.selectbox("", ["Sign-Up", "Log-In"], index = 0)

# if select == "Sign-Up":
#     signUp()
# if select == "Log-In":
#     logIn()  
    
# elif selected == "Upload":
#     st.title("Total files uploaded")
    
