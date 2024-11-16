#import random
#import matplotlib.pyplot as plt
#import numpy
import sqlite3
import streamlit as st

db = sqlite3.connect("database.db")
db_cursor = db.cursor()
db_cursor.execute("""
                  CREATE TABLE IF NOT EXISTS user_data (username TEXT NOT NULL, password TEXT NOT NULL, balance REAL)
                  """)
db.commit()

st.image("./media/logo.png")
st.success("Welcome to The Trading Simulator!")
st.text("Login?")
if st.checkbox("Yes, I want to login"):
    username = st.text_input("Enter username: ")
elif st.checkbox("No, I don't want to login"):
    st.text("Sign up?")
    if st.checkbox("Yes"):
        username_local = str(st.text_input("Enter username: ")).replace("\n", "")
        password_local = str(st.text_input("Enter password: ")).replace("\n", "")
        db_cursor.execute("INSERT INTO user_data(username, password) VALUES (?, ?)", (username_local, password_local))
        db_cursor.execute("DELETE FROM user_data WHERE username=''")
        db_cursor.execute("DELETE FROM user_data WHERE password=''")
        db.commit()

db.close()
