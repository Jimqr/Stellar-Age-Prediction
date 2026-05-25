import numpy as np
import pandas as pd
import time
import subprocess

try:
    file = pd.read_csv('data/data.csv')
    
    select = [
        'st_teff',
        'st_mass',
        'st_rad',
        'pl_name',
        'st_age'
        ]
        
    filtered = file[select]
    
    mask = filtered[['st_teff', 'st_mass', 'st_rad']].notna().all(axis=1) & filtered['st_age'].isna()
    
    age_nan_only = filtered[mask]
    
    age_nan_only.to_csv("product/csv/unknown_age.csv", index=False)
    
    print("[SUCCESS] Filtered successfully")
    print("[INFO] File location: product/csv/unknown_age.csv")
except FileNotFoundError:
        print("[ERROR] Directory not found: data/data.csv")
        print("[INFO] Make sure you run this from main.py")

for i in range(5, 0, -1):
    u = 'seconds' if i > 1 else 'second'
    print(f'Returning to main menu in {i} {u}', end='\r')
    time.sleep(1)
subprocess.run(['python', 'main.py'])