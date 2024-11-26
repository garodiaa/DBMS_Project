import streamlit as st
import mysql.connector

def connect_to_db():
    connection = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="",
                    database="noticedb"
                )
    st.success("Connected to the database successfully!")
    return connection

def app():
    st.title("Account")
    st.write("👤")

    choice = st.selectbox('Login/Signup', ['Login', 'Signup'])
    if choice == 'Login':
        st.write("Login to your account")

        student_id = st.text_input("Student ID")
        password = st.text_input("Password")
        if st.button("Login"):
            connection = connect_to_db()
            try:
                mycursor = connection.cursor()
                mycursor.execute("""
                                 SELECT name 
                                 FROM students 
                                 WHERE student_id = %s AND password = %s
                                 """, (student_id, password))
                result = mycursor.fetchone()
                if result:
                    st.success(f"Logged in successfully! Welcome, {result[0]}")
                else:
                    st.error("Invalid Student ID or Password")
            finally:
                connection.close()

    else:
        st.write("Signup for a new account")
        username = st.text_input("Username")
        password = st.text_input("Password", type='password')
        conf_password = st.text_input("Confirm Password", type='password')

        if password != conf_password:
            st.write("Passwords do not match")
        else:
            if st.button("Signup"):
                connection = connect_to_db()
                try:
                    mycursor = connection.cursor()
                    mycursor.execute("""
                                     INSERT INTO students (student_id, password)
                                     VALUES (%s, %s)
                                     """, (username, password))
                    connection.commit()
                    st.write("Account created successfully")
                    st.write("You can now login to your account")
                    st.button("Login")
                finally:
                    connection.close()