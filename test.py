import joblib
import numpy as np
import pandas as pd

# Load the trained model
model = joblib.load("model.pkl")

sample_data = pd.DataFrame([{
    "person_age": 21.0,
    "person_gender": "female",
    "person_education": "High School",
    "person_income": 12282.0,
    "person_emp_exp": 0,
    "person_home_ownership": "OWN",
    "loan_amnt": 1000.0,
    "loan_intent": "EDUCATION",
    "loan_int_rate": 11.14,
    "loan_percent_income": 0.08,
    "cb_person_cred_hist_length": 2.0,
    "credit_score": 504.0,
    "previous_loan_defaults_on_file": "Yes"
}])

# Make prediction
prediction = model.predict(sample_data)

# Output result
print("Predicted Value:", int(prediction[0]))