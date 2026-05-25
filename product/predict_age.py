import joblib
import pandas as pd

try:
    model = joblib.load('product/random_forest_exoplanet.pkl')
    
    try:
        df_new = pd.read_csv('product/csv/unknown_age.csv')

        df_new['mass_rad_ratio'] = df_new['st_mass'] / (df_new['st_rad'] ** 2 + 1e-6)
        
        X_new = df_new[['st_teff', 'st_mass', 'st_rad', 'mass_rad_ratio']]
        
        df_new['predicted_st_age'] = model.predict(X_new)
        
        df_new[['pl_name', 'predicted_st_age']].to_csv('product/csv/predictions.csv', index=False)
        
        print("[SUCCESS]")
        print("[INFO] File location: product/csv/predictions.csv")
    except FileNotFoundError:
        print("[ERROR] Directory not found: product/csv/unknown_age.csv")
        print("[INFO] Make sure you run this from main.py")
except FileNotFoundError:
    print("[ERROR] Directory not found: product/random_forest_exoplanet.pkl")
    print("[INFO] Make sure you run this from main.py")