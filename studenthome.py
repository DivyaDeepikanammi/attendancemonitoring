import streamlit as st

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
    # Dummy data for demonstration
    attendance_data = {
        "Class": ["Math", "Physics", "Chemistry"],
        "Attendance": ["Present", "Absent", "Present"]
    }
    st.title("Attendance Dashboard")
    st.write(attendance_data)

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
