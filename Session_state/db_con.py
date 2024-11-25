import streamlit as st
import pandas as pd

import mysql.connector

# Function to create a connection to the MySQL database
def create_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root@localhost",
        password="",
        database="shelfie"
    )

# Function to fetch data from a table
def fetch_data(connection, query):
    cursor = connection.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]
    return pd.DataFrame(data, columns=columns)

# Streamlit app
def main():
    st.title("MySQL Database Viewer")

    # Connect to the database
    connection = create_connection()
    print("Connected to the database")

    # Query to fetch data from a table
    # query = "SELECT * FROM your_table"

    # # Fetch data
    # data = fetch_data(connection, query)

    # # Display data in Streamlit
    # st.write(data)

    # # Close the connection
    # connection.close()

if __name__ == "__main__":
    main()