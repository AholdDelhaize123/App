import streamlit as st
import pandas as pd
from src.agents.policy_agent import check_policy
from src.utils.wfh_tracker import calculate_wfh_usage

st.title("Manager Approval Dashboard")

requests = pd.read_csv("data/requests.csv")

pending_requests = requests[requests["status"] == "Pending"]

for index, row in pending_requests.iterrows():

    st.subheader(f"Request ID: {row['request_id']}")

    st.write("Employee:", row["employee_name"])

    policy = check_policy(row["reason"])

    if policy:

        policy_name = policy["policy_name"]
        max_days = policy["max_days"]

        st.write("Policy:", policy_name)

        usage = calculate_wfh_usage(row["employee_id"], max_days)

        remaining_days = usage["remaining_days"]

        # AUTO REJECT
        if remaining_days == 0:

            requests.loc[index, "status"] = "Rejected"
            requests.to_csv("data/requests.csv", index=False)

            st.error("Auto Rejected (WFH limit exceeded)")
            st.divider()
            continue

    col1, col2 = st.columns(2)

    if col1.button(f"Approve {row['request_id']}"):

        requests.loc[index, "status"] = "Approved"
        requests.to_csv("data/requests.csv", index=False)

        st.success("Approved")

    if col2.button(f"Reject {row['request_id']}"):

        requests.loc[index, "status"] = "Rejected"
        requests.to_csv("data/requests.csv", index=False)

        st.error("Rejected")

    st.divider()