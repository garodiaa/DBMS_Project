import mysql.connector

try:
    notice_con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="noticedb"
    )
    cursor = notice_con.cursor()
    print("Connected to the database")

    cursor.execute("SELECT * FROM students")
    data = cursor.fetchall()
    print(data)

except mysql.connector.Error as e:
    print(f"Database error: {e}")

finally:
    if 'notice_con' in locals() and notice_con.is_connected():
        cursor.close()
        notice_con.close()
