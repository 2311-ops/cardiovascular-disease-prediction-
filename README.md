🫀 Cardiovascular Disease Prediction App

Live Demo: https://cardio--app.streamlit.app/

Overview

The Cardiovascular Disease Prediction App is an interactive web application built with Streamlit that predicts cardiovascular disease risk using a machine learning model (Logistic Regression). Users can input their health and lifestyle information, and the app instantly provides predictions along with actionable insights.

This tool is designed to help users better understand their cardiovascular health and encourage proactive health management.

Features

📝 User-friendly form: Enter age, gender, BMI, blood pressure, cholesterol, glucose, and lifestyle habits.

🔄 Real-time predictions: Get instant cardiovascular disease risk assessment.

⚙️ Automated preprocessing: Inputs are scaled and encoded for accurate predictions.

📊 Informative feedback: Clear, easy-to-understand results with recommendations.

Technology Stack

Frontend & Deployment: Streamlit

Machine Learning: Logistic Regression (scikit-learn)

Deep Learning: TensorFlow (Neural Network in separate notebook project1 nn.ipynb)

Data Processing: Pandas, NumPy

Serialization: Pickle for model and preprocessing objects

How It Works

Users enter health and lifestyle data into the form.

Categorical features are encoded, and numerical features are scaled using pre-trained preprocessing objects.

The Logistic Regression model predicts the likelihood of cardiovascular disease.

The app displays instant, easy-to-understand results with actionable recommendations.

A separate notebook (project1_nn.ipynb) explores a deep learning neural network built with TensorFlow and optimized with Keras Tuner, which achieved higher validation accuracy than logistic regression.
