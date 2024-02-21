import streamlit as st

# Sample student and admin credentials (for demonstration)
student_credentials = {"student1": "password1", "student2": "password2"}
admin_credentials = {"admin": "adminpass"}

def student_login():
    st.subheader("Student Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if username in student_credentials and student_credentials[username] == password:
            return True
        else:
            st.error("Invalid username or password")
            return False

def admin_login():
    st.subheader("Admin Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if username in admin_credentials and admin_credentials[username] == password:
            return True
        else:
            st.error("Invalid username or password")
            return False

def mark_attendance(class_name):
    if st.button("Mark Attendance"):
        # Implement attendance marking logic here
        st.success(f"Attendance marked for {class_name}")

def view_attendance():
    # Dummy data for demonstration
    attendance_data = {
        "Class": ["Math", "Physics", "Chemistry"],
        "Attendance": ["Present", "Absent", "Present"]
    }
    st.subheader("Attendance Dashboard")
    st.write(attendance_data)

def main():
    st.title("Student Attendance System")

    # Authentication
    if st.sidebar.radio("Login", ("Student", "Admin")) == "Student":
        if student_login():
            st.sidebar.success("Logged in as Student")
            class_name = st.selectbox("Select Class", ["Math", "Physics", "Chemistry"])
            mark_attendance(class_name)
    else:
        if admin_login():
            st.sidebar.success("Logged in as Admin")
            view_attendance()

if __name__ == "__main__":
    main()
