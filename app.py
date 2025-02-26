import streamlit as st
import requests
import pandas as pd

# API URL
API_URL = "https://loan-prediciton-deployment-project.onrender.com/predict/"

# Streamlit UI
st.title("Loan Approval Prediction App")
st.write("Fill in the details below to check your loan approval prediction.")

# user input fields
person_age = st.number_input("Age", min_value=18, max_value=120, value=25)
person_income = st.number_input("Income ($)", min_value=0, value=30000)
person_emp_exp = st.number_input("Employment Experience (years)", min_value=0, max_value=100, value=3)
loan_amnt = st.number_input("Loan Amount ($)", min_value=100, max_value=50000, value=5000)
loan_int_rate = st.number_input("Interest Rate (%)", min_value=0.0, max_value=50.0, value=10.0, step=0.1)
loan_percent_income = st.number_input("Loan Percentage of Income", min_value=0.01, max_value=1.0, value=0.1, step=0.01)
cb_person_cred_hist_length = st.number_input("Credit History Length (years)", min_value=1, max_value=30, value=5)
credit_score = st.number_input("Credit Score", min_value=0, max_value=1000, value=500)

# Categorical inputs
person_gender = st.selectbox("Gender", ["male", "female"])
person_education = st.selectbox("Education Level", ['Master', 'High School', 'Bachelor', 'Associate', 'Doctorate'])
person_home_ownership = st.selectbox("Home Ownership", ['RENT', 'OWN', 'MORTGAGE', 'OTHER'])
loan_intent = st.selectbox("Loan Intent", ['PERSONAL', 'EDUCATION', 'MEDICAL', 'VENTURE', 'HOMEIMPROVEMENT','DEBTCONSOLIDATION'])
previous_loan_defaults_on_file = st.selectbox("Previous Loan Defaults", ["Yes", "No"])

# Make predictions
if st.button("Predict Loan Approval"):
    data={
        "numerical_features": [person_age, person_income, person_emp_exp, loan_amnt, 
                               loan_int_rate,loan_percent_income, 
                               cb_person_cred_hist_length, credit_score],
        "categorical_features": [person_gender, person_education, person_home_ownership,
                                 loan_intent, previous_loan_defaults_on_file
        ]
    }

    # API call
    try:
        response = requests.post(API_URL, json=data)
        response.raise_for_status()
        prediction = response.json()
        st.success(f"Loan Approval Prediction: {'Approved' if prediction['prediction'] == 1 else 'Rejected'}")
    except requests.exceptions.RequestExceptoin as e:
        st.error(f"Error: {e}")
