import pickle
import streamlit as st
import numpy as np
import pandas as pd

# Load model and preprocessing objects
loaded_model = pickle.load(open('streamlit_cardio_model.sav', 'rb'))
scaler = pickle.load(open('streamlit_scaler.pkl', 'rb'))
encoder = pickle.load(open('streamlit_encoder.pkl', 'rb'))
feature_names = pickle.load(open('streamlit_feature_names.pkl', 'rb'))

# Get allowed categories for bPCategories
allowed_bPCategories = list(encoder.classes_)

# BMI category mapping
bmi_mapping = {'Underweight': 0, 'Normal': 1, 'Overweight': 2, 'Obese': 3}

st.title("Cardiovascular Disease Prediction")

with st.form("cardio_form"):
    age = st.number_input("Age", min_value=1, max_value=120, value=55)
    gender = st.selectbox("Gender", options=[1, 2], format_func=lambda x: "Female" if x == 1 else "Male")
    cholesterol = st.selectbox(
        "Cholesterol",
        options=[1, 2, 3],
        format_func=lambda x: {1: "Normal", 2: "Above Normal", 3: "Well Above Normal"}[x]
    )
    gluc = st.selectbox(
        "Glucose",
        options=[1, 2, 3],
        format_func=lambda x: {1: "Normal", 2: "Above Normal", 3: "Well Above Normal"}[x]
    )
    smoke = st.selectbox(
        "Smoker",
        options=[0, 1],
        format_func=lambda x: "No" if x == 0 else "Yes"
    )
    alco = st.selectbox(
        "Alcohol Intake",
        options=[0, 1],
        format_func=lambda x: "No" if x == 0 else "Yes"
    )
    active = st.selectbox(
        "Physically Active",
        options=[0, 1],
        format_func=lambda x: "No" if x == 0 else "Yes"
    )
    bmi = st.number_input("BMI", min_value=10.0, max_value=60.0, value=25.0)
    bPCategories = st.selectbox("Blood Pressure Category", options=allowed_bPCategories)
    BMI_category = st.selectbox("BMI Category", options=list(bmi_mapping.keys()))

    submitted = st.form_submit_button("Predict")

    if submitted:
        # Prepare input data
        input_data = {
            'age': age,
            'gender': gender,
            'cholesterol': cholesterol,
            'gluc': gluc,
            'smoke': smoke,
            'alco': alco,
            'active': active,
            'bmi': bmi,
            'bPCategories': bPCategories,
            'BMI_category': BMI_category,
            'age_cholesterol_interaction': age * cholesterol,
            'age_gluc_interaction': age * gluc,
            'age_bmi_interaction': age * bmi
        }
        input_df = pd.DataFrame([input_data])

        # Encode categorical features
        input_df['bPCategories'] = encoder.transform(input_df['bPCategories'])
        input_df['BMI_category'] = input_df['BMI_category'].map(bmi_mapping)

        # Select features and scale
        input_features = input_df[feature_names].values
        input_scaled = scaler.transform(input_features)

        # Predict
        prediction = loaded_model.predict(input_scaled)
        if prediction[0] == 1:
            st.success("Prediction: This individual is likely to have cardiovascular disease.")
        else:
            st.info("Prediction: This individual is not likely to have cardiovascular disease.")
