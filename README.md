🫀 Cardiovascular Disease Prediction App

Live Demo: https://cardio--app.streamlit.app/

Overview

The Cardiovascular Disease Prediction App is an interactive web application built with Streamlit that uses a machine learning model (Logistic Regression) to assess cardiovascular risk. Users can input their health and lifestyle information, and the app provides instant predictions along with actionable insights.

This tool is designed to help users understand their cardiovascular health and encourage proactive health management.

Features

📝 User-friendly form: Enter age, gender, BMI, blood pressure category, cholesterol, glucose, and lifestyle habits.

🔄 Real-time predictions: Instantly predicts cardiovascular disease risk based on your inputs.

⚙️ Data preprocessing: Inputs are scaled and encoded automatically for accurate predictions.

📊 Informative feedback: Clear results indicating likelihood of cardiovascular disease.

Technology Stack

Frontend & Deployment: Streamlit

Machine Learning: Logistic Regression (scikit-learn)

Data Processing: Pandas, NumPy

Serialization: Pickle for model and preprocessing objects

How It Works

Users fill out their health and lifestyle data in the form.

Categorical features are encoded, and numerical features are scaled using pre-trained preprocessing objects.

The machine learning model predicts the likelihood of cardiovascular disease.

The app displays an instant, easy-to-understand result with recommendations.
