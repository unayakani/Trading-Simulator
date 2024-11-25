import sys
import os
import streamlit as st

# Add the Modules folder to the system path
sys.path.append(os.path.join(os.path.dirname(__file__), 'modules'))

import login # type: ignore
import home # type: ignore

def main():
    Img = st.image("./media/logo.png")

    user = login.main()
    home.main(user)

if __name__ == "__main__":
    main()    