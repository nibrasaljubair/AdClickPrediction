from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

# Loaded the trained Model
model = joblib.load("rf_model.pkl")

# Bucketing logic for the new inputs to match the featured category
def bucket_age(age):
    if age <= 25: return 0
    elif age <= 40: return 1
    elif age <= 60: return 2
    else: return 3

def bucket_income(income):
    if income <= 40000: return 0
    elif income <= 80000: return 1
    elif income <= 120000: return 2
    else: return 3

# FastAPI app
app = FastAPI()

# JSON Class
class UserInput(BaseModel):
    age: int
    income: int
    gender: int       # 0 = Female, 1 = Male
    location: int     # 0 = Rural, 1 = Urban
    device: int       # 0 = Desktop, 1 = Mobile
    interest: int     # (Encoded interest category)

@app.get("/")
def home():
    return {"message": "Welcome to the Ad Click Prediction API! Go to /docs to try it out."}


# Prediction endpoint
@app.post("/predict")
def predict(user: UserInput):
    # Apply bucketing to age and income
    age_group = bucket_age(user.age)
    income_level = bucket_income(user.income)

    input_data = np.array([[age_group, income_level, user.gender, user.location, user.device, user.interest]])

    # Final Prediction
    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][1]

    return {
        "prediction": int(prediction),
        "probability": round(probability, 4),
        "message": "✅ User is likely to CLICK the ad" if prediction == 1 else "❌ User is unlikely to click the ad"
    }
