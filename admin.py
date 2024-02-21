import streamlit as st
import pandas as pd

# Updated student and admin credentials
student_credentials = {"user1": "user1"}
admin_credentials = {"admin": "admin"}

# Dummy attendance data for demonstration
attendance_data = {
    "Subject": ["Math", "Physics", "Chemistry"],
    "Day": ["Monday", "Tuesday", "Wednesday"],
    "Time": ["9:00 AM", "10:00 AM", "11:00 AM"],
    "Student1": ["Present", "Absent", "Present"],
    "Student2": ["Absent", "Present", "Present"],
    "Student3": ["Present", "Present", "Absent"]
}

def student_login():
    st.subheader("Student Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if username in student_credentials and student_credentials[username] == password:
            st.success("Logged in successfully!")
            st.sidebar.success("Logged in as Student")
            student_dashboard(username)  # Redirect to student dashboard
        else:
            st.error("Invalid username or password")

def student_dashboard(username):
    st.title("Student Dashboard")
    st.write(f"Welcome, {username}!")

    # Display subjects
    st.subheader("Your Subjects:")
    subjects = ["Math", "Physics", "Chemistry"]  # Example subjects, you can replace with your own
    selected_subject = st.selectbox("Select Subject", subjects)

    # Button to mark attendance
    if st.button("Mark Attendance"):
        # Logic to mark attendance for the selected subject
        st.success(f"Attendance marked for {selected_subject}")

def admin_login():
    st.subheader("Admin Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if username in admin_credentials and admin_credentials[username] == password:
            st.success("Logged in successfully!")
            st.sidebar.success("Logged in as Admin")
            admin_dashboard()  # Redirect to admin dashboard
        else:
            st.error("Invalid username or password")

def admin_dashboard():
    st.title("Admin Dashboard")
    st.subheader("Subjects and Attendance")

    # Display all subjects
    subjects = ["Math", "Physics", "Chemistry"]  # Example subjects, you can replace with your own
    selected_subject = st.selectbox("Select Subject", subjects)

    # Year-wise selection
    year = st.selectbox("Select Year", ["Year 1", "Year 2", "Year 3"])

    # Display attendance table for selected subject, day, and time
    st.subheader(f"Attendance for {selected_subject} - {year}")
    df = pd.DataFrame(attendance_data)
    filtered_df = df[(df['Subject'] == selected_subject) & (df['Year'] == year)]
    st.dataframe(filtered_df)

    # Allow admin to edit attendance
    st.subheader("Edit Attendance")
    st.write("You can edit the attendance table here.")

def main():
    st.title("Student Attendance System")

    # Authentication
    login_option = st.sidebar.radio("Login", ("Student", "Admin"))
    if login_option == "Student":
        student_login()
    else:
        admin_login()

if __name__ == "__main__":
    main()
