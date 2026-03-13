import streamlit as st
import pandas as pd
import uuid
from datetime import datetime
from src.agents.justification_agent import generate_justification

st.title("AI Flexible Work Request Portal")

employees = pd.read_csv("data/employees.csv")

employee_id = st.text_input("Enter Employee ID")
reason = st.text_area("Enter reason for WFH request")

if st.button("Submit Request"):

    if employee_id and reason:

        employee = employees[employees["employee_id"] == employee_id]

        if not employee.empty:

            name = employee.iloc[0]["name"]
            manager = employee.iloc[0]["manager"]

            justification = generate_justification(reason, name, manager)

            request_id = str(uuid.uuid4())[:8]

            request_date = datetime.today().strftime("%Y-%m-%d")

            try:
                requests = pd.read_csv("data/requests.csv")
            except:
                requests = pd.DataFrame(columns=[
                    "request_id",
                    "employee_id",
                    "employee_name",
                    "manager",
                    "status",
                    "request_date",
                    "reason"
                ])

            new_request = {
                "request_id": request_id,
                "employee_id": employee_id,
                "employee_name": name,
                "manager": manager,
                "status": "Pending",
                "request_date": request_date,
                "reason": reason
            }

            requests = pd.concat(
                [requests, pd.DataFrame([new_request])],
                ignore_index=True
            )

            requests.to_csv("data/requests.csv", index=False)

            st.success("Request Submitted")

            st.subheader("Generated Justification")

            st.text_area("Email Preview", justification, height=250)

        else:
            st.error("Employee not found")