"""
this module to train the model
"""

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
import joblib

# Load resume file 
df = pd.read_csv("data/resumes.csv")

# Train Test Split data
X_train, X_test, y_train, y_test = train_test_split(
    df["text"], df["label"], test_size=0.2, random_state=42
)

# Pipeline to load tfidf vectorizer and apply logistic regressions model
model = Pipeline([("tfidf", TfidfVectorizer()), ("clf", LogisticRegression())])

# Fit the model on training data 
model.fit(X_train, y_train)

# Save model to models folder 
joblib.dump(model, "models/resume_classifier.pkl")
