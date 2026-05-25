import pandas as pd
from scipy.stats import pearsonr, spearmanr
import numpy as np
from rich import print as pri
from rich.table import Table
import sys
import os
import time
import subprocess

os.system('clear')

np.seterr(all='ignore')

cor = sys.argv[1]
cor_title = None
cor_short = None

infos = [
    ("st_mass", "Stellar Mass", "mass"),
    ("st_teff", "Stellar Effective Temperature", "teff"),
    ("st_lum", "Stellar Luminosity", "lum"),
    ("st_rad", "Stellar Radius", "rad"),
    ("st_met", "Stellar Metallicity", "met"),
    ("st_logg", "Stellar Log Surface Gravity", "logg"),
    ("st_rotp", "Stellar Rotation Period", "rotp")
]

for info in infos:
    if info[0] == cor:
        cor_title = info[1]
        cor_short = info[2]
        
table = Table(title=f"Correlation of {cor_title} and Stellar Age")

table.add_column("Feature")
table.add_column("Pearson's R")
table.add_column("Spearman's R")

best_feature_pr = None
best_feature_sr = None
best_pr = 0
best_sr = 0

try:
    file = pd.read_csv("data/data.csv")
    
    select = [
                f"st_{cor_short}",
                "st_age"
    ]
    
    filtered = file[select].dropna()
    
    filtered.to_csv(f"correlation/csv/{cor_short}-age.csv", index=False)
    
    df = pd.read_csv(f"correlation/csv/{cor_short}-age.csv")
    
    inde_data = df[f"st_{cor_short}"]
    age = df["st_age"]

    transformations = {
        f"{cor_short}": inde_data,
        f"{cor_short}^2": inde_data ** 2,
        f"{cor_short}^3": inde_data ** 3,
        f"{cor_short}^4": inde_data ** 4,
        f"sqrt({cor_short})": np.sqrt(inde_data),
        f"1/{cor_short}": 1 / inde_data,
        f"1/{cor_short}^2": 1 / (inde_data ** 2),
        f"1/{cor_short}^3": 1 / (inde_data ** 3),
        f"log({cor_short})": np.log(inde_data)
    }

    for name, feature in transformations.items():
        
        pr = pearsonr(feature, age)
        rho, p_value = spearmanr(feature, age)
        if not np.isnan(pr.statistic) and not np.isnan(rho):
            table.add_row(
                name, 
                str(round(pr.statistic, 5)), 
                str(round(rho, 5))
                )
        if abs(pr.statistic) > abs(best_pr):
            best_pr = pr.statistic
            best_feature_pr = name
        if abs(rho) > abs(best_sr):
            best_sr = rho
            best_feature_sr = name

    pri(table)
    print(f"""
    Best Pearson Correlation: {round(best_pr, 5)} 
    Feature: {best_feature_pr}
    
    Spearman Correlation: {round(best_sr, 5)}
    Feature: {best_feature_sr}
    """)
except FileNotFoundError:
        print("[ERROR] Directory not found: data/data.csv")
        print("[INFO] Request a data from NASA Exoplanet Archive | main menu => [1]")
        print("[INFO] Make sure you run this from main.py")
        for i in range(5, 0, -1):
            u = 'seconds' if i > 1 else 'second'
            print(f'Returning to main menu in {i} {u}', end='\r')
            time.sleep(1)
        subprocess.run(['python', 'main.py'])
