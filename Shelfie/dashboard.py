import streamlit as st
import mysql.connector
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
        connection = connect_to_db()
        try:
            mycursor = connection.cursor()
            mycursor.execute("SELECT * FROM books WHERE title LIKE %s", ('%' + query + '%',))
            result = mycursor.fetchall()
            connection.close()
            return result
        finally:
            connection.close()

    def add_book(title, author, genre, publication_year, description):
        connection = connect_to_db()
        try:
            mycursor = connection.cursor()
            mycursor.execute("INSERT INTO books (title, author, genre, publication_year, description) VALUES (%s, %s,%s,%s,%s)", (title, author, genre, publication_year, description))
            connection.commit()
        finally:
            connection.close()

    def update_book(book_id, new_title, new_author):
        connection = connect_to_db()
        try:
            mycursor = connection.cursor()
            mycursor.execute("UPDATE books SET title = %s, author = %s WHERE id = %s", (new_title, new_author, book_id))
            connection.commit()
        finally:
            connection.close()

    def remove_book(book_id):
        connection = connect_to_db()
        try:
            mycursor = connection.cursor()
            mycursor.execute("DELETE FROM books WHERE id = %s", (book_id,))
            connection.commit()
        finally:
            connection.close()

    if 'add_book' not in st.session_state:
        st.session_state.add_book = False
    if 'update_book' not in st.session_state:
        st.session_state.update_book = False
    if 'remove_book' not in st.session_state:
        st.session_state.remove_book = False

    if st.button("Add Book"):
        st.session_state.add_book = True
        st.session_state.update_book = False
        st.session_state.remove_book = False

    if st.session_state.add_book:
        title = st.text_input("Enter book title:")
        author = st.text_input("Enter book author:")
        genre = st.text_input("Enter book genre:")
        publication_year = st.text_input("Enter book publication year:")
        description = st.text_input("Enter book description:")
        if st.button("Submit"):
            add_book(title, author, genre, publication_year, description)
            st.success("Book added successfully!")
            st.session_state.add_book = False

    if st.button("Update Book"):
        st.session_state.update_book = True
        st.session_state.add_book = False
        st.session_state.remove_book = False

    if st.session_state.update_book:
        update_query = st.text_input("Search for a book to update:")
        if update_query:
            books = search_books(update_query)
            if books:
                for book in books:
                    st.write(f"Title: {book[1]}, Author: {book[2]}")
                    if st.button(f"Update {book[1]}"):
                        new_title = st.text_input("Enter new title:", value=book[1])
                        new_author = st.text_input("Enter new author:", value=book[2])
                        new_genre = st.text_input("Enter new genre:", value=book[3])
                        new_publication_year = st.text_input("Enter new publication year:", value=book[4])
                        new_description = st.text_input("Enter new description:", value=book[5])
                        if st.button("Submit"):
                            update_book(book[0], new_title, new_author, new_genre, new_publication_year, new_description)
                            st.success("Book updated successfully!")
                            st.session_state.update_book = False
            else:
                st.write("No books found.")

    if st.button("Remove Book"):
        st.session_state.remove_book = True
        st.session_state.add_book = False
        st.session_state.update_book = False

    if st.session_state.remove_book:
        remove_query = st.text_input("Search for a book to remove:")
        if remove_query:
            books = search_books(remove_query)
            if books:
                for book in books:
                    st.write(f"Book ID: {book[0]}, Title: {book[1]}, Author: {book[2]}, Genre: {book[3]}, Publication Year: {book[4]}, Description: {book[5]}")
                    if st.button(f"Remove '{book[1]}'"):
                        remove_book(book[0])
                        st.success("Book removed successfully!")
                        st.session_state.remove_book = False
            else:
                st.write("No books found.")



