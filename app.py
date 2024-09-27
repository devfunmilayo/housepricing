import streamlit as st
import joblib
import numpy as np

# Load the trained model
model = joblib.load('house_price_model.pkl')

# Streamlit app
st.title('House Price Prediction')

# Get user input
sq_ft = st.number_input('Enter the size of the house (in sq ft):', min_value=500, max_value=5000, step=100)

# Predict house price when user clicks the button
if st.button('Predict'):
    prediction = model.predict(np.array([[sq_ft]]))
    st.write(f'Predicted House Price: ${prediction[0]:,.2f}')
