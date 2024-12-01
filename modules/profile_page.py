import streamlit as st

def main(user):
    placeholder = st.empty()
    with placeholder.container():
        st.title("Profile")
        st.header(user)
    