import streamlit as st
import pickle
import numpy as np

def load_model():
    with open('saved_steps.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

data = load_model()

regressor = data['predicted']
Order_type_A = data["Order_type_A"]
Order_type_B = data["Order_type_B"]
Order_type_C = data['Order_type_C']

def show_predicted_page():
    st.title("Cargo Goods Prediction by Categories")
