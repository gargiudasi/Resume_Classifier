"""
create apis with fastapi
"""

import os
from fastapi import FastAPI, Form
import joblib
import gdown

app = FastAPI()
# Load pkl file stored in model folder
MODEL_PATH = "models/resume_classifier.pkl"

model = joblib.load(MODEL_PATH)

@app.get("/")
def message():
    """
    to verify if app is launched successfully
    """
    return {"message": "you have successfully lauched the app"}


@app.post("/predict/")
def predict(text: str = Form(...)):
    """
    predict the output for given input
    """
    return {"prediction": model.predict([text])[0]}
