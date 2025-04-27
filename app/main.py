"""
create apis with fastapi
"""

import os
import joblib

import uvicorn
from fastapi import FastAPI, Form

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


if __name__ == "__main__":
    # Use os.getenv to get the $PORT variable, default to '8000' if not set
    port = int(os.getenv("PORT", 8000))  # Convert to integer after getting the value
    print(os.getenv("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
