import streamlit as st

# Function to register a new student
def register_student():
    st.subheader("Student Registration")
    name = st.text_input("Name")
    student_id = st.text_input("ID")
    year = st.selectbox("Year", ["1st Year", "2nd Year", "3rd Year", "4th Year"])
    subjects = st.text_input("Subjects (comma-separated)", help="Enter 3 subjects separated by commas")
    password = st.text_input("Password", type="password")
    if st.button("Register"):
        # Add your code here to handle student registration
        st.success("Registration successful!")

# Function for student login
def student_login():
    st.subheader("Student Login")
    student_id = st.text_input("ID")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        # Add your code here to authenticate student login
        st.success("Login successful!")
        # Redirect to student dashboard

# Main function
def main():
    st.title("Attendance Management System")
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Register", "Login"])

    if page == "Register":
        register_student()
    elif page == "Login":
        student_login()

if __name__ == "__main__":
    main()
