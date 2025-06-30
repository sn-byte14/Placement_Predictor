# 🎯 Placement Predictor 

An intelligent, interactive web application that predicts whether a student is likely to be placed in a job based on academic performance, technical ability, and soft skills. This project was designed to mimic real-world placement screening by including more than just CGPA — it takes a holistic view of a student’s profile.

The model is trained on a synthetic dataset simulating real college placement conditions, with inputs like CGPA, IQ, communication skills, technical knowledge, number of projects, resume quality, and internship experience.

The frontend is built using Streamlit, making it simple, fast, and interactive. The backend uses a Random Forest Classifier, chosen for its accuracy and ability to handle multiple features with ease. The trained model is exported using Joblib and loaded in real-time for predictions.

Whether you're a student preparing for placements, or a teacher looking to demonstrate machine learning in action — this app provides a realistic and educational insight into how AI can support career forecasting.


🌐 Live Demo
 access here: https://placementpredictor-nnckdi3a3kfmdhbrpzhuqy.streamlit.app/


## 🧠 What's New in This Version

✅ Real-world inspired dataset with multiple key features:
- 📚 CGPA (out of 10)
- 🧠 IQ Score
- 🗣️ Communication Skills (1–10)
- 💻 Technical Skills (1–10)
- 📁 Number of Projects
- 📝 Resume Score (1–10)
- 📄 Internship Experience (Yes/No)

---

## 💻 Tech Stack

- Python
- Pandas + NumPy
- Scikit-learn (Random Forest)
- Streamlit (Web UI)
- Joblib (Model serialization)



📁 Project Structure

placement-predictor/
├── app.py                  # Streamlit app
├── placement_model.pkl     # Trained model file
├── placement_dataset.csv   # (optional) Dataset used for training
├── requirements.txt        # Python dependencies
└── README.md               # Documentation




