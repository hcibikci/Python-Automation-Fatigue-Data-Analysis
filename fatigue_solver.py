import pandas as pd
import numpy as np

"""
@Author: Hatice Çıbıkçı
@Description: Automated Fatigue Damage Calculator based on Palmgren-Miner Rule.
              Replaces manual Excel-based summation for large datasets.
"""

def calculate_fatigue_damage(data_path, sn_slope, intercept):
    """
    Calculates cumulative damage index (D) from a spectrum load file.
    
    Args:
        data_path (str): Path to the CSV file containing cycle counts and stress amplitudes.
        sn_slope (float): The slope (b) of the Basquin's equation (Material Property).
        intercept (float): The fatigue strength coefficient (Sf') or intercept at 1 cycle.
        
    Returns:
        float: Total Cumulative Damage (D). If D > 1.0, failure is predicted.
    """
    
    # Simulating data loading (In real scenario: pd.read_csv(data_path))
    # Creating a dummy dataframe for demonstration purposes on GitHub
    data = {
        'Stress_Amplitude_MPa': [150, 200, 250, 300, 120],
        'Cycle_Count': [100000, 5000, 2000, 500, 500000]
    }
    df = pd.DataFrame(data)
    
    print(f"--- Processing Data: {len(df)} load cases loaded ---")
    
    total_damage = 0.0
    
    # Vectorized calculation for performance (faster than for-loops)
    # Basquin's Equation: S = A * N^b  =>  N = (S/A)^(1/b)
    # Rearranged log form: Log(N) = Intercept - Slope * Log(S)
    
    for index, row in df.iterrows():
        stress = row['Stress_Amplitude_MPa']
        cycles = row['Cycle_Count']
        
        # Calculate Fatigue Life (N_f) for this stress level
        # Note: This is a simplified S-N approach for demonstration
        fatigue_life = 10 ** (intercept - sn_slope * np.log10(stress))
        
        # Palmgren-Miner Rule: D = sum(n_i / N_i)
        damage_fraction = cycles / fatigue_life
        total_damage += damage_fraction
        
    return total_damage

if __name__ == "__main__":
    # Example Material: Aluminum 7075-T6 approximation
    # Slope (b) and Intercept are illustrative constants
    damage_result = calculate_fatigue_damage("dummy_path.csv", sn_slope=9.0, intercept=25.0)
    
    print(f"Calculated Cumulative Damage Index: {damage_result:.5f}")
    
    if damage_result >= 1.0:
        print("RESULT: CRITICAL FAILURE PREDICTED ❌")
    else:
        print(f"RESULT: Design Safe (Margin of Safety: {(1-damage_result)*100:.2f}%) ✅")
