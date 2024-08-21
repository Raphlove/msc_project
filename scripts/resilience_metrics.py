import numpy as np

def calculate_metrics(df):
    # Example metrics calculations
    metrics = {
        'Mean Time to Detect (MTTD)': df['Anomaly Scores'].mean(),
        'Mean Time to Respond (MTTR)': df['Anomaly Scores'].median(),
        'Mean Time to Recover (MTTR)': np.percentile(df['Anomaly Scores'], 90)
    }
    
    return metrics

if __name__ == "__main__":
    from data_preprocessing import preprocess_data
    from data_collection import load_data
    
    file_path = 'data/cybersecurity_attacks.csv'
    data = load_data(file_path)
    processed_data = preprocess_data(data)
    metrics = calculate_metrics(processed_data)
    print(metrics)
