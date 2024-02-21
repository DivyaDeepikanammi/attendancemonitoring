import streamlit as st
import gspread
from google.oauth2 import service_account
import pandas as pd

# Load Google Sheets credentials
credentials = service_account.Credentials.from_service_account_info(
    st.secrets["gcp_service_account"]
)

# Function to authenticate with Google Sheets
def authenticate_google_sheets():
    gc = gspread.authorize(credentials)
    return gc

# Function to mark attendance in Google Sheets
def mark_attendance(student_name, year, subject, attended):
    gc = authenticate_google_sheets()
    sheet = gc.open_by_key("1q7jJEbUj47fJ9oEQnPxrf61QVYlsmKBzaAeJnRXjfuo")  # Replace with your Google Sheet key
    worksheet = sheet.worksheet("Attendance")  # Assuming attendance data is in a worksheet named "Attendance"
    student_records = worksheet.get_all_records()

    # Iterate through each record and find the matching record to update attendance
    for index, record in enumerate(student_records, start=2):  # Assuming data starts from row 2
        if (record['Student Name'] == student_name and
            record['Year'] == year and
            record['Subject'] == subject):
            worksheet.update_cell(index, student_records[0].index('Attended') + 1, attended)
            st.success("Attendance marked successfully!")
            return

    # If no matching record is found
    st.error("Student record not found or attendance not marked.")

# Student login function
def student_login():
    # Implement student login logic here
    pass

# Main function
def main():
    st.title("Student Attendance System")

    # Authentication
    login_option = st.sidebar.radio("Login", ("Student", "Admin"))
    if login_option == "Student":
        student_login()
    else:
        # Implement admin login logic
        pass

    # Once logged in, display subjects based on the student's year
    # Allow students to mark attendance
    # Update Google Sheet with attendance data

    # Sample usage of the mark_attendance() function
    mark_attendance("John Doe", 1, "Mathematics", "Yes")

if __name__ == "__main__":
    main()
