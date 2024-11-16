import sqlite3 as sq
import bcrypt
import streamlit as st

# Functions
def db_connect():
    db = sq.connect("database.db")
    db_cursor = db.cursor()
    db_cursor.execute("CREATE TABLE IF NOT EXISTS user_data (username TEXT NOT NULL, password_hash TEXT NOT NULL, balance REAL)") 
    return db, db_cursor

def signup_form():
    with st.form("signup_form"):
        username = st.text_input("Username: ")
        new_password = st.text_input("Password: ", type="password")
        confirm_password = st.text_input("Confirm Password: ", type="password")
        submit_button = st.form_submit_button("Submit")
    return username, new_password, confirm_password, submit_button

def login_form():
    with st.form("login_form"):
        username = st.text_input("Username: ")
        password = st.text_input("Password: ", type="password")
        submit_button = st.form_submit_button("Submit")
    return username, password, submit_button


def main():
    db, db_cursor = db_connect()

    st.image("./media/logo.png")
    login_signup = st.selectbox(
        "Choose one option: ",
        ["Choose an option", "Login", "Signup"]
    )

    if login_signup == "Signup":
        username, new_password, confirm_password, submit_button = signup_form()
        if submit_button:
            db_cursor.execute("SELECT username FROM user_data WHERE username = ?", (username,))
            existing_user = db_cursor.fetchone()

            if new_password != confirm_password:
                st.error("Passwords do not match")

            elif existing_user:
                st.error("Username already exists")

            elif len(username) < 4:
                st.error("Username must be at least 4 characters long")
            
            elif len(new_password) < 8:
                st.error("Password must be at least 8 characters long")
                
            else:
                salt = bcrypt.gensalt()
                password_hash = bcrypt.hashpw(new_password.encode('utf-8'), salt)

                db_cursor.execute("INSERT INTO user_data (username, password_hash, balance) VALUES (?, ?, ?)", (username, password_hash, 0.0))
                db.commit()
                
                st.success("User registered successfully!")

    elif login_signup == "Login":
        username, password, submit_button = login_form()
        if submit_button:
            db_cursor.execute("SELECT password_hash FROM user_data WHERE username = ?", (username,))
            result = db_cursor.fetchone()

            if result and bcrypt.checkpw(password.encode('utf-8'), result[0]):
                st.success("Login successful!")

            else:
                st.error("Invalid username or password")
    
    elif login_signup == "Choose an option":
        pass
    
    else:
        st.error("Program Bugged")

    db.close()

if __name__ == "__main__":
    main()
