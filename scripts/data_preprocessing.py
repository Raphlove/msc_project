from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import pandas as pd

def preprocess_data(df):
    # Select numeric columns for normalization
    numeric_cols = ['Source Port', 'Destination Port', 'Packet Length', 'Anomaly Scores']
    
    # Normalize the numeric columns
    scaler = StandardScaler()
    df[numeric_cols] = scaler.fit_transform(df[numeric_cols])
    
    # Apply PCA for dimensionality reduction
    pca = PCA(n_components=3)
    principal_components = pca.fit_transform(df[numeric_cols])
    df_pca = pd.DataFrame(data=principal_components, columns=['PC1', 'PC2', 'PC3'])
    
    # Concatenate the PCA columns with the original dataframe
    df = pd.concat([df, df_pca], axis=1)
    
    return df

if __name__ == "__main__":
    from data_collection import load_data
    
    file_path = 'data/cybersecurity_attacks.csv'
    data = load_data(file_path)
    processed_data = preprocess_data(data)
    print(processed_data.head())
