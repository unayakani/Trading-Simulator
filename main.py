import sqlite3
import streamlit as st
import sys
import time

user_db = sqlite3.connect("user_database.db")
user_db_cursor = user_db.cursor()
user_db_cursor.execute("CREATE TABLE IF NOT EXISTS user_data (username TEXT NOT NULL, password TEXT NOT NULL, balance REAL)")

st.image("./media/logo.png")
login_signup = st.radio(
        "Choose one option: ",
        ["Login", "Signup"],
        )
form = st.form("signup_login")
username_local = form.text_input("Username: ")
password_local = form.text_input("Password: ")
form.form_submit_button("Submit")
