import streamlit as st
import pandas as pd
import joblib

# Load your trained model
model = joblib.load('Model.h5')

st.title("🚀 Employee Promotion Prediction App")
st.markdown("Fill out employee info below to predict if they'll be promoted.")

# Manual Encoding Maps — must match training!
dept_map = {
    'Analytics': 0, 'Finance': 1, 'HR': 2, 'Legal': 3,
    'Operations': 4, 'Procurement': 5, 'R&D': 6,
    'Sales & Marketing': 7, 'Technology': 8
}

region_map = {
    'region_1': 0, 'region_2': 1, 'region_3': 2, 'region_4': 3,
    'region_5': 4, 'region_6': 5, 'region_7': 6, 'region_8': 7, 'region_9': 8
}

edu_map = {
    'Below Secondary': 0, "Bachelor’s": 1, "Master’s & above": 2
}

gender_map = {
    'Male': 0, 'Female': 1, 'Other': 2
}

channel_map = {
    'sourcing': 0, 'referred': 1, 'other': 2
}

# User Inputs
department = st.selectbox("Department", list(dept_map.keys()))
region = st.selectbox("Region", list(region_map.keys()))
education = st.selectbox("Education Level", list(edu_map.keys()))
gender = st.radio("Gender", list(gender_map.keys()))
recruitment_channel = st.selectbox("Recruitment Channel", list(channel_map.keys()))
no_of_trainings = st.slider("Number of Trainings", 0, 10, 1)
age = st.slider("Age", 18, 60, 30)
previous_year_rating = st.selectbox("Previous Year Rating", [1, 2, 3, 4, 5])
length_of_service = st.slider("Length of Service (Years)", 0, 40, 5)
kpi_met = st.radio("KPIs Met > 80%", [1, 0], format_func=lambda x: "Yes" if x == 1 else "No")
awards_won = st.radio("Awards Won Last Year?", [1, 0], format_func=lambda x: "Yes" if x == 1 else "No")
avg_training_score = st.slider("Avg Training Score", 40, 100, 70)

# Encode using manual maps
department_enc = dept_map[department]
region_enc = region_map[region]
education_enc = edu_map[education]
gender_enc = gender_map[gender]
recruitment_enc = channel_map[recruitment_channel]

# Create DataFrame for prediction
input_df = pd.DataFrame({
    'department': [department_enc],
    'region': [region_enc],
    'education': [education_enc],
    'gender': [gender_enc],
    'recruitment_channel': [recruitment_enc],
    'no_of_trainings': [no_of_trainings],
    'age': [age],
    'previous_year_rating': [previous_year_rating],
    'length_of_service': [length_of_service],
    'KPIs_met >80%': [kpi_met],
    'awards_won?': [awards_won],
    'avg_training_score': [avg_training_score]
})

# Predict
if st.button("🔍 Predict"):
    prediction = model.predict(input_df)[0]
    
    if prediction == 1:
        st.success("🎉 This employee is likely to be PROMOTED!")
    else:
        st.error("⚠️ This employee is NOT likely to be promoted.")