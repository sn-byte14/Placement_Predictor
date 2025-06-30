import streamlit as st
import numpy as np
import joblib

# Load model (simplified)
model = joblib.load("placement_model.pkl")

# UI settings
st.set_page_config(page_title="Placement Predictor", page_icon="🎯")
st.title("🎓 Placement Predictor")

st.markdown("Enter your academic and skill details below:")

# Input fields
cgpa = st.slider("📚 CGPA (out of 10)", 4.0, 10.0, 7.0, step=0.01)
iq = st.number_input("🧠 IQ Score", min_value=80, max_value=160, value=110, step=1)
comm = st.slider("🗣️ Communication Skills (1–10)", 1, 10, 7)
tech = st.slider("💻 Technical Skills (1–10)", 1, 10, 8)
projects = st.slider("📁 Number of Projects", 0, 10, 3)
intern = st.radio("📄 Internship Experience", ["Yes", "No"])
resume = st.slider("📃 Resume Score (1–10)", 1, 10, 7)

# Convert internship to numeric
intern_val = 1 if intern == "Yes" else 0

# Predict
if st.button("🔍 Predict Placement"):
    features = np.array([[cgpa, iq, comm, tech, projects, intern_val, resume]])
    prediction = model.predict(features)[0]

    if prediction == 1:
        st.success("🎉 You are likely to be Placed!")
    else:
        st.warning("😔 You may not get placed. Improve your skills and try again.")