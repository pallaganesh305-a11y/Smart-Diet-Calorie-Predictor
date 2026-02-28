import streamlit as st
import pandas as pd
import joblib

model = joblib.load("diet_model.pkl")

st.set_page_config(page_title="Smart Diet Calorie Predictor", layout="centered")

st.title("🍎 Smart Diet Calorie Predictor")
st.write("Enter your nutritional values and select your goal")

# Goal Selection
goal = st.selectbox(
    "Select Your Goal",
    ["Weight Loss 🔥", "Muscle Gain 💪", "Maintenance ⚖"]
)

# Inputs
st.sidebar.header("Enter Nutritional Values")

protein = st.sidebar.number_input("Protein (g)", min_value=0.0)
carbs = st.sidebar.number_input("Carbohydrates (g)", min_value=0.0)
fat = st.sidebar.number_input("Fat (g)", min_value=0.0)
fiber = st.sidebar.number_input("Fiber (g)", min_value=0.0)
sugar = st.sidebar.number_input("Sugars (g)", min_value=0.0)
sodium = st.sidebar.number_input("Sodium (mg)", min_value=0.0)
cholesterol = st.sidebar.number_input("Cholesterol (mg)", min_value=0.0)
water = st.sidebar.number_input("Water intake", min_value=0.0)

if st.button("Predict Calories"):

    input_data = pd.DataFrame(
        [[protein, carbs, fat, fiber, sugar,
          sodium, cholesterol, water]],
        columns=[
            "Protein (g)",
            "Carbohydrates (g)",
            "Fat (g)",
            "Fiber (g)",
            "Sugars (g)",
            "Sodium (mg)",
            "Cholesterol (mg)",
            "Water intake"
        ]
    )

    prediction = model.predict(input_data)
    calories = prediction[0]

    st.success(f"Estimated Calories: {calories:.2f} kcal")

    # Advice Logic
    st.subheader("📋 Recommendation")

    if "Weight Loss" in goal:
        target = calories - 300
        st.info(f"For weight loss, try maintaining around **{target:.0f} kcal/day** (calorie deficit).")

    elif "Muscle Gain" in goal:
        target = calories + 300
        st.info(f"For muscle gain, aim for around **{target:.0f} kcal/day** (calorie surplus).")

    else:
        st.info(f"For maintenance, stay around **{calories:.0f} kcal/day**.")