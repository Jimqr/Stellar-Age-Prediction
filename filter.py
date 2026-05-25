import numpy as np
import pandas as pd
import time
import subprocess

try:
    file = pd.read_csv('data/data.csv')
    
    select = [
        'st_teff',
        'st_mass',
        'st_lum',
        'st_rad',
        'st_met',
        'st_logg',
        'st_rotp',
        'st_age'
        ]
        
    select_2 = [
        'st_teff',
        'st_mass',
        'st_lum',
        'st_rad',
        'st_met',
        'st_logg',
        'st_age'
        ]
        
    select_3 = [
        'st_teff',
        'st_mass',
        'st_rad',
        'st_met',
        'st_logg',
        'st_age'
        ]
        
    filtered = file[select].dropna()
    filtered_2 = file[select_2].dropna()
    filtered_3 = file[select_3].dropna()

    filtered.to_csv("data/data_1.csv", index=False)
    filtered_2.to_csv("data/data_2.csv", index=False)
    filtered_3.to_csv("data/data_3.csv", index=False)
    
    print("[SUCCESS] Filtered successfully")
    print("[INFO] File location: data/data_...")
except FileNotFoundError:
        print("[ERROR] Directory not found: data/data.csv")
        print("[INFO] Request a data from NASA Exoplanet Archive | main menu => [1]")
        print("[INFO] Make sure you run this from main.py")


for i in range(5, 0, -1):
    u = 'seconds' if i > 1 else 'second'
    print(f'Returning to main menu in {i} {u}', end='\r')
    time.sleep(1)
subprocess.run(['python', 'main.py'])