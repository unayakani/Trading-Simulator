import sys
import os
import time
import streamlit as st

# Add the Modules folder to the system path
sys.path.append(os.path.join(os.path.dirname(__file__), 'modules'))

import login # type: ignore
import home # type: ignore

def main():
    st.set_page_config(
            page_title="Trade Simulator",
            page_icon="./media/icon.png",
        )
    
    Img = st.image("./media/logo.png")

    state = 'Logged Out'

    if state == 'Logged Out':
        user = login.main()
        if user:
            state = 'Logged In'

    if state == 'Logged In':
        Img.empty()
        state = home.main(state, user)
        

if __name__ == "__main__":
    main()    