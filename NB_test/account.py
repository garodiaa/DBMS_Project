import streamlit as st
import mysql.connector

def connect_to_db():
    connection = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password=" ",
                    database="shelfie"
                )

    mycursor = connection.cursor()
    st.warning("Connected to the database successfully!")

def app():

    # connect_to_db()
    st.title("Account")
    st.write("👤")

    choice = st.selectbox('Login/Signup', ['Login', 'Signup'])
    if choice == 'Login':
        st.write("Login to your account")

        username = st.text_input("Username")
        password = st.text_input("Password", type='password')
        st.button("Login")

    else:
        st.write("Signup for a new account")
        username = st.text_input("Username")
        password = st.text_input("Password", type='password')
        conf_password = st.text_input("Confirm Password", type='password')

        if password != conf_password:
            st.write("Passwords do not match")
        else:
            if st.button("Signup"):

                st.write("Account created successfully")
                st.write("You can now login to your account")
                st.button("Login")