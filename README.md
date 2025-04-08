
# Ad Click Prediction - ML Model + Cloud Deployment

This project predicts whether a user will click on an ad based on their profile (age, income, gender, etc.). It includes a complete ML pipeline with a deployed REST API using FastAPI, Docker, and Google Cloud Run.

---

## What It Does
- Predicts ad click behavior from user data
- Trained using a Random Forest classifier
- Deployed with FastAPI as a REST API
- Containerized using Docker
- Hosted publicly on Google Cloud Run

---

## ML Pipeline Summary
- Preprocessed features: age, income, gender, location, device, interest
- Label encoded categorical variables
- Trained and evaluated multiple models:
  - Logistic Regression (~49% accuracy)
  - Neural Network with Keras (~49%)
  - Random Forest Classifier (~53%) chosen for balance between performance and interpretability
- Focused on production-readiness over raw accuracy

---

## DevOps & Deployment
- Created a FastAPI backend exposing a `/predict` endpoint
- Dockerized the application with pinned dependencies (`scikit-learn`, `numpy`)
- Built and deployed the container using Google Cloud Build and Cloud Run
- Auto-scaled and publicly accessible with REST API

---

## How to Run Locally
1. Install requirements
```bash
pip install -r requirements.txt
```

2. Run the API locally
```bash
uvicorn main:app --reload
```

3. Run the frontend (Streamlit)
```bash
streamlit run app.py
```

---

## Cloud Endpoint
The deployed API is accessible via Cloud Run at:
```
https://your-cloud-run-url.a.run.app/predict
```
Test it in your browser:
```
https://your-cloud-run-url.a.run.app/docs
```

---

## Next Steps
- Deploy Streamlit frontend to Streamlit Cloud or Render
- Add authentication or analytics

---

## Built With
- Python
- FastAPI
- scikit-learn
- Docker
- Google Cloud Run
- Streamlit
