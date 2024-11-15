#import random
#import matplotlib.pyplot as plt
#import numpy
import sqlite3
import streamlit as st

user_db = sqlite3.connect("user_database.db")
user_db_cursor = user_db.cursor()
user_db_cursor.execute("""
                  CREATE TABLE IF NOT EXISTS user_data (username TEXT NOT NULL, password TEXT NOT NULL, balance REAL)
                  """)
user_db.commit()

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
        user_db_cursor.execute("INSERT INTO user_data(username, password, balance) VALUES (?, ?, ?)", (username_local, password_local, 2000.00))
        user_db_cursor.execute("DELETE FROM user_data WHERE username=''")
        user_db_cursor.execute("DELETE FROM user_data WHERE password=''")
        user_db_cursor.execute("DELETE FROM user_data WHERE balance=''")
        user_db.commit()

user_db.close()

bot_db = sqlite3.connect("bot_database.db")
bot_db_cursor = bot_db.cursor()
bot_db_cursor.execute("""
                      CREATE TABLE IF NOT EXISTS bot_data (botindex INT NOT NULL, balance REAL)
                      """)
bot_db_cursor.execute("""
                      INSERT INTO bot_data (botindex, balance) VALUES (?, ?)
                      """, (1, 2000.00))
bot_db_cursor.execute("""
                      INSERT INTO bot_data (botindex, balance) VALUES (?, ?)
                      """, (2, 2000.00))
bot_db_cursor.execute("""
                      INSERT INTO bot_data (botindex, balance) VALUES (?, ?)
                      """, (3, 2000.00))
bot_db_cursor.execute("""
                      INSERT INTO bot_data (botindex, balance) VALUES (?, ?)
                      """, (4, 2000.00))
bot_db_cursor.execute("""
                      INSERT INTO bot_data (botindex, balance) VALUES (?, ?)
                      """, (5, 2000.00))
bot_db_cursor.execute("""
                      INSERT INTO bot_data (botindex, balance) VALUES (?, ?)
                      """, (6, 2000.00))
bot_db_cursor.execute("""
                      INSERT INTO bot_data (botindex, balance) VALUES (?, ?)
                      """, (7, 2000.00))
bot_db_cursor.execute("""
                      INSERT INTO bot_data (botindex, balance) VALUES (?, ?)
                      """, (8, 2000.00))
bot_db_cursor.execute("""
                      INSERT INTO bot_data (botindex, balance) VALUES (?, ?)
                      """, (9, 2000.00))
bot_db_cursor.execute("""
                      INSERT INTO bot_data (botindex, balance) VALUES (?, ?)
                      """, (10, 2000.00))

bot_db.commit()
bot_db.close()
