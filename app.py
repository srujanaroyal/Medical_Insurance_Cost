import streamlit as st
import pickle
import numpy as np

model = pickle.load(open("insurance_model.pkl","rb"))

st.title("Insurance Cost Prediction")

age = st.number_input("Age")
bmi = st.number_input("BMI")
children = st.number_input("Children")
smoker = st.selectbox("Smoker",["yes","no"])

smoker_num = 1 if smoker=="yes" else 0

input_data = np.array([[age, bmi, children, smoker_num]])

if st.button("Predict"):
    prediction = model.predict(input_data)
    st.write("Predicted Insurance Charges:", prediction[0])