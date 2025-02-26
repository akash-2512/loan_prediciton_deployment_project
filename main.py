from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

# load trained model
model = joblib.load("model.pkl")

# define request body schema
class ModelInput(BaseModel):
    numerical_features: list[float]
    categorical_features: list[str]

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Weldome to my First Logistic Regression Model API"}

@app.post("/predict/")
def predict(input_data: ModelInput):
    import pandas as pd  # Ensure Pandas is available
    
    # Combine numerical and categorical features
    feature_values = input_data.numerical_features + input_data.categorical_features
    
    # Convert input into a DataFrame with proper column names
    columns = [
        "person_age", "person_income", "person_emp_exp", "loan_amnt", "loan_int_rate",
        "loan_percent_income", "cb_person_cred_hist_length", "credit_score",
        "person_gender", "person_education", "person_home_ownership", 
        "loan_intent", "previous_loan_defaults_on_file"
    ]
    input_df = pd.DataFrame([feature_values], columns=columns)  # Convert list to DataFrame

    # Make a prediction
    prediction = model.predict(input_df)  # Now it's a DataFrame

    return {"prediction": int(prediction[0])}
