import streamlit as st
import account


def connect_to_db():
    connection = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="",
                    database="shelfiedb"
                )
    # st.success("Connected to the database successfully!")
    return connection


def app():
    st.title("Dashboard")

    if 'username' not in st.session_state:
        st.session_state.username = ''

    st.write(f"Welcome, {st.session_state.username}")

    def search_books(query):
        conn = sqlite3.connect('books.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM books WHERE title LIKE ?", ('%' + query + '%',))
        results = cursor.fetchall()
        conn.close()
        return results

    search_query = st.text_input("Search for a book:")
    if search_query:
        books = search_books(search_query)
        if books:
            for book in books:
                st.write(f"Title: {book[1]}, Author: {book[2]}")
        else:
            st.write("No books found.")

