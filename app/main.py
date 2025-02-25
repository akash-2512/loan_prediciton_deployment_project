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
    features = [input_data.numerical_features + input_data.categorical_features]
    prediction = model.predict(features)
    return {"prediction": int(prediction[0])}