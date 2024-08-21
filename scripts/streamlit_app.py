import streamlit as st
import pandas as pd
from data_preprocessing import preprocess_data
from resilience_metrics import calculate_metrics
from simulation import run_simulation

st.title("Cyber Resilience Evaluation")

# Upload CSV
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file:
    data = pd.read_csv(uploaded_file)
    
    st.write("Data Preview:", data.head())
    
    # Preprocess Data
    preprocessed_data = preprocess_data(data)
    st.write("Preprocessed Data Preview:", preprocessed_data.head())

    # Calculate Metrics
    metrics = calculate_metrics(preprocessed_data)
    st.write("Resilience Metrics:", metrics)

    # Run Simulations
    simulation_results = run_simulation(preprocessed_data)
    st.write("Simulation Results:", simulation_results)

    # Display charts
    st.line_chart(preprocessed_data[['Timestamp', 'Anomaly Scores']].set_index('Timestamp'))
