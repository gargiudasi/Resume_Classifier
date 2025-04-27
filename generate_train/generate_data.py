"""
generate and clean data after loading from hugging face
"""

import os
from datasets import load_dataset

# `huggingface-cli login` to access this dataset
ds = load_dataset("NxtGenIntern/job_titles_and_descriptions")

# STEP 1: Setup paths and folders
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
data_dir = os.path.join(BASE_DIR, "data")
models_dir = os.path.join(BASE_DIR, "models")

# create folder if not exists to store model and data
os.makedirs(data_dir, exist_ok=True)
os.makedirs(models_dir, exist_ok=True)

csv_path = os.path.join(data_dir, "resumes.csv")
model_path = os.path.join(models_dir, "resume_classifier.pkl")

# Convert to pandas
df = ds["train"].to_pandas()
df.drop(columns="Job Description", inplace=True)
df = df.rename(columns={"Skills": "text", "Job Title": "label"})

# Preprocessing: Lowercase all text in both columns
df["text"] = df["text"].str.lower()
df["label"] = df["label"].str.lower()

# store resumes.csv file to data folder
df.to_csv("data/resumes.csv", index=False, columns=["text", "label"])

csv_path = "/tmp/mydata.csv"
