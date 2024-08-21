import pandas as pd
import numpy as np

def simulate_attack(df, attack_type, severity_level):
    """ Simulate attacks based on the specified attack type and severity level. """
    simulated_df = df.copy()
    
    # Define behaviors for different attack types
    if attack_type == "DDoS":
        simulated_df['Anomaly Scores'] += severity_level * np.random.uniform(1.5, 2.5, size=len(simulated_df))
        simulated_df['Traffic Type'] = 'High-Volume Traffic'
    elif attack_type == "Malware Infiltration":
        simulated_df['Anomaly Scores'] += severity_level * np.random.uniform(2.0, 3.0, size=len(simulated_df))
        simulated_df['Packet Type'] = 'Suspicious Payload'
    
    # Set severity level explicitly
    simulated_df['Severity Level'] = severity_level
    
    return simulated_df

def run_simulation(df):
    # Simulate DDoS attack with high severity
    ddos_attack = simulate_attack(df, attack_type="DDoS", severity_level=3)
    # Simulate Malware Infiltration with medium severity
    malware_attack = simulate_attack(df, attack_type="Malware Infiltration", severity_level=2)
    
    # Combine attacks for overall simulation
    simulated_df = pd.concat([ddos_attack, malware_attack])
    
    # Example evaluation metric
    attack_summary = {
        'Total Simulated Attacks': len(simulated_df),
        'Average Anomaly Score during Attacks': simulated_df['Anomaly Scores'].mean(),
        'Severity Level Distribution': simulated_df['Severity Level'].value_counts().to_dict()
    }
    
    return attack_summary

if __name__ == "__main__":
    from data_preprocessing import preprocess_data
    from data_collection import load_data
    
    file_path = 'data/cybersecurity_attacks.csv'
    data = load_data(file_path)
    processed_data = preprocess_data(data)
    simulation_results = run_simulation(processed_data)
    print(simulation_results)
