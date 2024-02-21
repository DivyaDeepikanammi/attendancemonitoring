# Import necessary libraries
import streamlit as st
import sqlite3
from datetime import datetime

# Create or connect to SQLite database
conn = sqlite3.connect('attendance.db')
c = conn.cursor()

# Create table for users
c.execute('''CREATE TABLE IF NOT EXISTS users
             (username TEXT PRIMARY KEY, password TEXT, role TEXT)''')

# Create table for attendance
c.execute('''CREATE TABLE IF NOT EXISTS attendance
             (id INTEGER PRIMARY KEY, username TEXT, subject TEXT, date TEXT)''')

# Function to add a new user
def add_user(username, password, role):
    c.execute("INSERT INTO users (username, password, role) VALUES (?, ?, ?)", (username, password, role))
    conn.commit()

# Function to check credentials
def authenticate(username, password):
    c.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
    return c.fetchone()

# Function to mark attendance
def mark_attendance(username, subject):
    date = datetime.now().strftime("%Y-%m-%d")
    c.execute("INSERT INTO attendance (username, subject, date) VALUES (?, ?, ?)", (username, subject, date))
    conn.commit()

# Function to retrieve attendance
def get_attendance():
    c.execute("SELECT * FROM attendance")
    return c.fetchall()

# Streamlit UI
def main():
    st.title("Student Attendance Management System")
    page = st.sidebar.selectbox("Choose a page", ["Login", "Admin"])

    if page == "Login":
        st.subheader("Login")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        if st.button("Login"):
            user = authenticate(username, password)
            if user:
                st.success("Logged in successfully!")
                if user[2] == 'student':
                    st.write("Welcome, Student!")
                    subject = st.text_input("Enter Subject")
                    if st.button("Mark Attendance"):
                        mark_attendance(username, subject)
                        st.success("Attendance marked successfully!")
                else:
                    st.write("Welcome, Admin!")
            else:
                st.error("Invalid username or password")

    elif page == "Admin":
        st.subheader("Admin Panel")
        attendance_data = get_attendance()
        st.write("Attendance Data")
        st.table(attendance_data)

if __name__ == "__main__":
    main()
