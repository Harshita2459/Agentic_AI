# # frontend/app.py

import streamlit as st
import requests

st.title("AI Agent Bot")

# Academic Query Section
st.header("Ask an Academic Query")
query = st.text_input("Enter your query:")
if st.button("Get Answer"):
    response = requests.get(f"http://127.0.0.1:5000/academic_query?query={query}")
    if response.status_code == 200:
        st.write(response.json()["response"])
    else:
        st.error("Failed to get a response!")

# Certificate Generation Section
st.header("Generate Certificate")
name_cert = st.text_input("Enter your name:")
cert_type = st.selectbox("Select Certificate Type", ["Bonafide", "Experience", "Graduation", "Internship"])
if st.button("Generate Certificate"):
    if name_cert:
        payload = {"user_id": name_cert.lower(), "certificate_type": cert_type, "name": name_cert}
        response = requests.post("http://127.0.0.1:5000/generate_certificate", json=payload)
        if response.status_code == 200:
            st.success(response.json()["message"])
        else:
            st.error("Failed to generate certificate!")
    else:
        st.warning("Please enter your name.")

# Apply Leave Section
st.header("Apply for Leave")
name_leave = st.text_input("Enter your name for leave:")
employee_id = st.text_input("Enter Employee ID:")
leave_type = st.selectbox("Select Leave Type", ["Sick Leave", "Casual Leave", "Paid Leave"])
start_date = st.date_input("Start Date")
end_date = st.date_input("End Date")
if st.button("Apply Leave"):
    if name_leave and employee_id:
        payload = {
            "employee_id": employee_id,
            "leave_type": leave_type,
            "start_date": str(start_date),
            "end_date": str(end_date),
            "name": name_leave
        }
        response = requests.post("http://127.0.0.1:5000/apply_leave", json=payload)
        if response.status_code == 200:
            st.success(response.json()["message"])
        else:
            st.error("Failed to apply for leave!")
    else:
        st.warning("Please enter your name and Employee ID.")
