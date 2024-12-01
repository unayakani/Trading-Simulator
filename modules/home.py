import streamlit as st
import time

def main(state, user):
    placeholder = st.empty()
    with placeholder.container():
        t = st.title("Welcome to Trade Simulator")
        h = st.header("You are now logged in")

        st.sidebar.image("./media/logo.png")
        st.sidebar.title("Navigation Bar")

        page = st.sidebar.selectbox("", ["Choose a page", "Profile", "Trade", "Status"])

        if page == "Profile":
            t.empty()
            h.empty()
            import profile_page 
            profile_page.main(user)

        if page == "Trade":
            t.empty()
            h.empty()
            import trade_page 
            trade_page.main(user)

        if page == "Status":
            t.empty()
            h.empty()
            import status_page 
            status_page.main(user)

        st.sidebar.success("Feel Free to Navigate")
            
        if st.sidebar.button("Logout"):
            state = 'Logged Out'
            st.write("Logging out...")
            time.sleep(2)
            return state