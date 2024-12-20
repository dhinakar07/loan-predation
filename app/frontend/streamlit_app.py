import streamlit as st
import requests

# FastAPI URL
API_URL = "http://backend:8000/predict/"  # Replace with your actual API URL if deployed elsewhere

# Streamlit UI
st.title("Loan Default Prediction")

st.header("Enter Applicant Details")

# Input fields
person_age = st.number_input("Person Age", min_value=18, max_value=100, value=21)
person_gender = st.selectbox("Person Gender", ["male", "female"])
person_education = st.selectbox("Person Education", ["High School", "Bachelor", "Master", "PhD", "Other"])
person_income = st.number_input("Person Income", min_value=0, value=12282)
person_emp_exp = st.number_input("Employment Experience (Years)", min_value=0, value=0)
person_home_ownership = st.selectbox("Home Ownership", ["OWN", "RENT", "MORTGAGE", "OTHER"])
loan_amnt = st.number_input("Loan Amount", min_value=0, value=1000)
loan_intent = st.selectbox("Loan Intent", ["PERSONAL", "EDUCATION", "HOMEIMPROVEMENT", "VENTURE", "DEBTCONSOLIDATION", "MEDICAL"])
loan_int_rate = st.number_input("Loan Interest Rate (%)", min_value=0.0, value=11.14)
loan_percent_income = st.number_input("Loan Percent of Income", min_value=0.0, value=0.08)
cb_person_cred_hist_length = st.number_input("Credit History Length (Years)", min_value=0, value=2)
credit_score = st.number_input("Credit Score", min_value=300, max_value=850, value=504)
previous_loan_defaults_on_file = st.selectbox("Previous Loan Defaults on File", ["Yes", "No"])

# Submit button
if st.button("Predict"):
    # Prepare input payload
    payload = {
        "person_age": person_age,
        "person_gender": person_gender,
        "person_education": person_education,
        "person_income": person_income,
        "person_emp_exp": person_emp_exp,
        "person_home_ownership": person_home_ownership,
        "loan_amnt": loan_amnt,
        "loan_intent": loan_intent,
        "loan_int_rate": loan_int_rate,
        "loan_percent_income": loan_percent_income,
        "cb_person_cred_hist_length": cb_person_cred_hist_length,
        "credit_score": credit_score,
        "previous_loan_defaults_on_file": previous_loan_defaults_on_file,
    }

    try:
        # Send POST request to FastAPI
        response = requests.post(API_URL, json=payload)
        response_data = response.json()

        if response.status_code == 200:
            # Display prediction result
            #st.success(f"Loan Status: {response_data['prediction']}")
            if response_data['prediction']==1:
                st.success("loan is approved")
            else:
                st.info("loan is not approved")
        else:
            # Display error message
            st.error(f"Error: {response_data['detail']}")
    except Exception as e:
        st.error(f"Failed to connect to API. Error: {e}")