
"""
# 🧠 Resume NLP Classifier API

![CI](https://github.com/yourusername/resume-nlp-classifier/actions/workflows/python-ci.yml/badge.svg)

A machine learning-powered resume classifier that predicts the job role based on resume text. Built using **FastAPI**, **Scikit-learn**, and **Streamlit**. Deployed with **Render** and tested via **GitHub Actions**.

---

## 🚀 Features
- Predicts job roles from resume content (e.g., Data Scientist, Backend Dev)
- FastAPI-powered REST API
- Streamlit frontend for quick testing
- Automated testing with GitHub Actions
- Deploy-ready via Render.com

---

## 🌐 Live Demo
- 🖥️ [Streamlit Frontend] (streamlit run app_ui.py)
- 🔌 [FastAPI API Endpoint](https://resume-api-ed9k.onrender.com/docs)


## 🧪 Run Locally
```bash
# Backend
uvicorn app.main:app --reload

# Frontend
streamlit run app_ui.py
```

## 🧠 Author
**Gargi Udasi**  

<!-- create venv -->
python -m venv venv
.\venv\Scripts\activate

<!-- install modules -->
pip install -r requirements.txt

<!-- run to create modle pkl file -->
python .\generate_train\generate_data.py
python .\generate_train\train_model.py

<!-- run app -->
uvicorn app.main:app --reload 