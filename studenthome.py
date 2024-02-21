import streamlit as st
import pandas as pd

# Updated student and admin credentials
student_credentials = {"user1": "user1"}
admin_credentials = {"admin": "admin"}

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
            view_attendance()  # Redirect to admin view attendance page
        else:
            st.error("Invalid username or password")

def view_attendance():
    # Display form to input attendance data
    st.subheader("Enter Attendance Data")
    student_name = st.text_input("Student Name")
    roll_id = st.text_input("Roll ID")
    subject = st.selectbox("Subject", ["Math", "Physics", "Chemistry"])
    day = st.selectbox("Day", ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"])
    time = st.text_input("Time")
    attendance_status = st.selectbox("Attendance Status", ["Present", "Absent"])

    if st.button("Submit"):
        # Append data to dataframe and export to Excel
        data = {"Student Name": [student_name],
                "Roll ID": [roll_id],
                "Subject": [subject],
                "Day": [day],
                "Time": [time],
                "Attendance": [attendance_status]}
        df = pd.DataFrame(data)
        export_to_excel(df)

def export_to_excel(df):
    # Export dataframe to Excel
    df.to_excel("attendance_data.xlsx", index=False)
    st.success("Attendance data exported to Excel!")

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
