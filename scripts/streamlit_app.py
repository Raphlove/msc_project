import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
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

    plt.figure(figsize=(10, 6))
    plt.hist(preprocessed_data['Anomaly Scores'], bins=50, alpha=0.7, color='blue')
    plt.title('Distribution of Anomaly Scores')
    plt.xlabel('Anomaly Score')
    plt.ylabel('Frequency')
    st.pyplot(plt)  # Display the histogram in Streamlit

    # Severity Level Distribution Pie Chart
    severity_counts = preprocessed_data['Severity Level'].value_counts()
    plt.figure(figsize=(8, 8))
    plt.pie(severity_counts, labels=severity_counts.index, autopct='%1.1f%%', colors=['#ff9999','#66b3ff','#99ff99'])
    plt.title('Severity Level Distribution')
    st.pyplot(plt)  # Display the pie chart in Streamlit
