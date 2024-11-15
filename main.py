import sqlite3
import streamlit as st
import sys
import time

user_db = sqlite3.connect("user_database.db")
user_db_cursor = user_db.cursor()
user_db_cursor.execute("""
                  CREATE TABLE IF NOT EXISTS user_data (username TEXT NOT NULL, password TEXT NOT NULL, balance REAL)
                  """)

st.image("./media/logo.png")
st.success("Welcome to The Trading Simulator!")

st.text("Login?")
if st.checkbox("Yes, I want to login"):
    username_local = st.text_input("Enter username: ")
    time.sleep(5)
    user_db_cursor.execute("SELECT EXISTS(SELECT 1 FROM user_data WHERE username = ?)", (username_local,))
    username_in_database = user_db_cursor.fetchone()[0]
    if username_in_database:
        st.text_input("Password: ")
        user_db_cursor.execute("SELECT password FROM user_data WHERE username = ?", (username_local,))
        password_correct = user_db_cursor.fetchone()
        if password_correct:
            st.success("Login successful.")
        else:
            st.error("Incorrect password")
            sys.exit()
    else:
        st.error("Sorry, you have not signed up yet!")
        sys.exit()
elif st.checkbox("No, I don't want to login"):
    st.text("Sign up?")
    if st.checkbox("Yes"):
        username_local = str(st.text_input("Enter username: ")).replace("\n", "")
        user_db_cursor.execute("SELECT EXISTS(SELECT 1 FROM user_data WHERE username = ?)", (username_local,))
        username_in_database = user_db_cursor.fetchone()[0]
        if username_in_database:
            print("Username taken")
            sys.exit()
        else:
            password_local = str(st.text_input("Enter password: ")).replace("\n", "")
            user_db_cursor.execute("INSERT INTO user_data(username, password, balance) VALUES (?, ?, ?)", (username_local, password_local, 2000.00))
            user_db_cursor.execute("DELETE FROM user_data WHERE username=''")
            user_db_cursor.execute("DELETE FROM user_data WHERE password=''")
            user_db_cursor.execute("DELETE FROM user_data WHERE balance=''")

user_db.commit()
user_db.close()

bot_db = sqlite3.connect("bot_database.db")
bot_db_cursor = bot_db.cursor()

bot_db.commit()
bot_db.close()
