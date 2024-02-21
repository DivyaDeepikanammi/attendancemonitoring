import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Access Google Sheet without authentication
def get_google_sheet_data(sheet_url, sheet_name):
    gc = gspread.models
    worksheet = gc.open_by_url(sheet_url).worksheet(sheet_name)
    data = worksheet.get_all_values()
    return data

def main():
    st.title('Google Sheet Data Viewer')

    # Input Google Sheet URL and Sheet Name
    sheet_url = st.text_input('Enter Google Sheet URL')
    sheet_name = st.text_input('Enter Sheet Name')

    if sheet_url and sheet_name:
        try:
            sheet_data = get_google_sheet_data(sheet_url, sheet_name)
            st.write('Data from Google Sheet:')
            st.write(sheet_data)
        except Exception as e:
            st.error(f"Error fetching data: {str(e)}")

if __name__ == "__main__":
    main()
