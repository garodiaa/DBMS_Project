import streamlit as st

import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="noticedb"
)
cursor = connection.cursor()

print("Connected to the database")

# Streamlit app
def main():
    st.title("MySQL Database Viewer")

    st.subheader("View Data")
    cursor.execute("SELECT * FROM students")
    data = cursor.fetchall()
    st.write(data)

if __name__ == "__main__":
    main()