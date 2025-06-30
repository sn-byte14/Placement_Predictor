import streamlit as st
import numpy as np
import joblib

# Load the model
model = joblib.load("D:\placement_predictor\placement_model.pkl")

# Streamlit UI
st.set_page_config(page_title="Placement Predictor", page_icon="🎓")
st.title("🎓 Placement Prediction App")

st.markdown("""
Enter your academic details below:

- 🆔 Student ID (any number, e.g., 1001)  
- 📚 CGPA (scale 4.0 to 10.0)  
- 🧠 IQ Score (e.g., 80–160)
""")

# Input fields
student_id = st.number_input("Student ID", min_value=1, max_value=9999, value=1001)
cgpa = st.slider("CGPA", 4.0, 10.0, 7.0)
iq = st.number_input("IQ Score", min_value=60, max_value=200, value=100)

# Predict button
if st.button("Predict Placement"):
    try:
        features = np.array([[student_id, cgpa, iq]])
        prediction = model.predict(features)[0]
        if prediction == 1:
            st.success("🎉 You are likely to be Placed!")
        else:
            st.warning("😔 You may not get placed. Improve your profile and try again.")
    except Exception as e:
        st.error(f"⚠️ Error during prediction: {e}")