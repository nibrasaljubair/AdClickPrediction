import streamlit as st
import requests

st.title("🎯 Ad Click Prediction")

st.markdown("""
Enter a user's information below to predict whether they are likely to click on the ad.
""")

# Labels for the interest variable
interest_labels = {
    0: "Travel",
    1: "Food",
    2: "Technology",
    3: "Fashion",
    4: "Sports",
    5: "Education"
}

# Invert to match dropdown display
interest_options = [f"{v} ({k})" for k, v in interest_labels.items()]
interest_values = list(interest_labels.keys())

# Form fields
age = st.number_input("Age", min_value=10, max_value=100, value=25)
income = st.number_input("Income", min_value=0, value=50000)
gender = st.selectbox("Gender", options=[("Male", 1), ("Female", 0)])
location = st.selectbox("Location", options=[("Urban", 1), ("Rural", 0)])
device = st.selectbox("Device", options=[("Mobile", 1), ("Desktop", 0)])

# to show interest with the labels
interest_display = st.selectbox("Interest Category", options=interest_options)
interest = int(interest_display.split("(")[-1].replace(")", ""))

# Predict
if st.button("Predict"):
    data = {
        "age": age,
        "income": income,
        "gender": gender[1],
        "location": location[1],
        "device": device[1],
        "interest": interest
    }

    try:
        response = requests.post("https://ad-click-api-323446887587.us-central1.run.app/predict", json=data)

        if response.status_code == 200:
            result = response.json()
            st.success(result["message"])
            st.metric(label="Click Probability", value=f"{result['probability'] * 100:.2f}%")
        else:
            st.error("❌ Prediction failed. Check your FastAPI backend.")
    except:
        st.error("❌ Could not connect to FastAPI. Is it running?")
