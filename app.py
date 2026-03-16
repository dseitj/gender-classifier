import streamlit as st
import pandas as pd
import joblib

model = joblib.load("model.joblib")

st.title("Gender Classification App")

st.write("Enter facial features to predict gender")

long_hair = st.checkbox("Long Hair")

forehead_width = st.number_input("Forehead Width (cm)", min_value=10.0, max_value=20.0)
forehead_height = st.number_input("Forehead Height (cm)", min_value=3.0, max_value=10.0)

nose_wide = st.checkbox("Wide Nose")
nose_long = st.checkbox("Long Nose")
lips_thin = st.checkbox("Thin Lips")
distance_long = st.checkbox("Long Distance Nose to Lip")

if st.button("Predict"):

    data = pd.DataFrame([[
    int(long_hair),
    forehead_width,
    forehead_height,
    int(nose_wide),
    int(nose_long),
    int(lips_thin),
    int(distance_long)
]], columns=[
    "long_hair",
    "forehead_width_cm",
    "forehead_height_cm",
    "nose_wide",
    "nose_long",
    "lips_thin",
    "distance_nose_to_lip_long"
])

    prediction = model.predict(data)

    st.subheader("Prediction")

    if prediction[0] == "Male":
        st.success("Male")
    else:
        st.success("Female")