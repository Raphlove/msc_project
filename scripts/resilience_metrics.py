import numpy as np
import pandas as pd
from sklearn.metrics import confusion_matrix

def calculate_false_positives(y_true, y_pred):
    try:
        tn, fp, fn, tp = confusion_matrix(y_true, y_pred).ravel()
        return fp  # False Positives
    except ValueError as e:
        print(f"Error calculating false positives: {e}")
        return None

def calculate_metrics(df):
    try:
        # Ensure 'Anomaly Scores' is numeric
        df['Anomaly Scores'] = pd.to_numeric(df['Anomaly Scores'], errors='coerce')
        print("Anomaly Scores column after conversion:", df['Anomaly Scores'].head())
        
        # Drop rows where 'Anomaly Scores' is NaN
        df = df.dropna(subset=['Anomaly Scores'])
        print("Data after dropping NaNs in Anomaly Scores:", df.head())

        # Example metrics calculations
        metrics = {
            'Mean Time to Detect (MTTD)': df['Anomaly Scores'].mean(),
            'Mean Time to Respond (MTTR)': df['Anomaly Scores'].median(),
            'Mean Time to Recover (MTTR)': np.percentile(df['Anomaly Scores'], 90),
        }
        print("Calculated metrics so far:", metrics)

        # Calculate False Positives
        y_true = (df['Malware Indicators'].notna()).astype(int)
        y_pred = (df['Anomaly Scores'] > 1.5).astype(int)  # Example threshold
        print("True labels:", y_true.head())
        print("Predicted labels:", y_pred.head())

        metrics['False Positives'] = calculate_false_positives(y_true, y_pred)
        print("Final metrics including False Positives:", metrics)

    except Exception as e:
        # Handle errors and print a message
        print(f"Error calculating metrics: {e}")
        metrics = {}

    return metrics

if __name__ == "__main__":
    from data_preprocessing import preprocess_data
    from data_collection import load_data
    
    file_path = 'data/cybersecurity_attacks.csv'
    data = load_data(file_path)
    processed_data = preprocess_data(data)
    metrics = calculate_metrics(processed_data)
    print(metrics)
