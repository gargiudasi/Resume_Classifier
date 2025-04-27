"""
This is created so as to see app in Ui using streamlit and render url
"""

import streamlit as st
import requests

st.set_page_config(page_title="Resume Classifier", layout="centered")
st.title("📄 Resume Classifier")

text = st.text_area("Paste your resume text here:", height=200)

if st.button("Predict Job Role"):
    if text:
        try:
            response = requests.post(
                "https://resume-api-ed9k.onrender.com/predict/", data={"text": text}
            )
            result = response.json()
            st.success(f"🧠 Predicted Role: {result['prediction']}")
        except Exception as e:
            st.error("⚠️ Could not connect to API. Please check your deployment.")
    else:
        st.warning("Please paste some resume text to get started.")
