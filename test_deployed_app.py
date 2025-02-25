import joblib
import numpy as np
import pandas as pd
import requests


# Define sample data
numerical_features = [21.0, 12282.0, 0, 1000.0, 11.14, 0.08, 3.0, 504]
categorical_features = ["female", "High School", "OWN", "EDUCATION", "Yes"]

# Convert into DataFrame format for local model
columns = [
    "person_age", "person_income", "person_emp_exp", "loan_amnt", "loan_int_rate",
    "loan_percent_income", "cb_person_cred_hist_length", "credit_score",
    "person_gender", "person_education", "person_home_ownership", 
    "loan_intent", "previous_loan_defaults_on_file"
]
sample_data = pd.DataFrame([numerical_features + categorical_features], columns=columns)


# Test deployed API
url = "https://loan-prediciton-deployment-project.onrender.com/predict/"
data = {"numerical_features": numerical_features, "categorical_features": categorical_features}

try:
    response = requests.post(url, json=data)
    response.raise_for_status()  # Raise an error for bad responses (4xx, 5xx)
    api_prediction = response.json()
    print("API Prediction:", api_prediction)
except requests.exceptions.RequestException as e:
    print("API Error:", e)
