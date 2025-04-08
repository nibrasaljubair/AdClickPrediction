FROM python:3.10
WORKDIR /app
COPY main.py .
COPY rf_model.pkl .
RUN pip install fastapi uvicorn scikit-learn==1.3.0 numpy==1.23.5 joblib
EXPOSE 8080
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
