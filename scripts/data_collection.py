import pandas as pd

def load_data(file_path):
    # Load the dataset
    df = pd.read_csv(file_path)

    # Convert Timestamp to datetime
    df['Timestamp'] = pd.to_datetime(df['Timestamp'])

    # Handle missing values (basic imputation)
    df['Malware Indicators'].fillna('No Indicator', inplace=True)
    df['Anomaly Scores'].fillna(df['Anomaly Scores'].mean(), inplace=True)
    df.fillna('Unknown', inplace=True)  # Fill other NaNs with 'Unknown'
    
    return df

if __name__ == "__main__":
    file_path = 'data/cybersecurity_attacks.csv'
    data = load_data(file_path)
    print(data.head())
