from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split, cross_val_score 
import pandas as pd
import numpy as np
from sklearn.ensemble import GradientBoostingRegressor
import os

os.system('clear')

print('main menu -> xgboost')

try:
    df = pd.read_csv('data/data_3.csv')
    
    df['temp_rad_interaction'] = (df['st_teff'] * df['st_rad'])
    df['mass_rad_ratio'] = (df['st_mass'] / (df['st_rad'] ** 2 + 1e-6))
    
    X = df[['st_teff', 'st_mass',
            'st_rad', 'st_met', 'st_logg', 'mass_rad_ratio', 'temp_rad_interaction']]
    
    y = df['st_age']
    
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.3,
        random_state=100
    )
    
    gb_model = GradientBoostingRegressor(
        n_estimators=300,
        learning_rate=0.05,
        max_depth=4,
        random_state=42
    )
    
    gb_model.fit(X_train, y_train)
    
    y_pred = gb_model.predict(X_test)
    
    print("Prediction for test set:")
    print(y_pred)
    
    rf_model_diff = pd.DataFrame({
        'Actual value': y_test,
        'Predicted value': y_pred
    })
    
    print(rf_model_diff.head())
    
    mae = mean_absolute_error(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse)
    r2 = r2_score(y_test, y_pred)
    
    print("R²:", r2)
    print("Mean Absolute Error:", mae)
    print("Mean Square Error:", mse)
    print("Root Mean Square Error:", rmse)
    
    importance = gb_model.feature_importances_
    
    for feature, score in zip(X.columns, importance):
        print(feature, score)
        
    train_score = gb_model.score(X_train, y_train)
    test_score = gb_model.score(X_test, y_test)
    
    print("Train R²:", train_score)
    print("Test R²:", test_score)
    
    scores = cross_val_score(
        gb_model,
        X,
        y,
        cv=5,
        scoring='r2'
    )
    
    print(scores)
    print("Average R²:", scores.mean())
except FileNotFoundError:
        print("[ERROR] Directory not found: data/data_3.csv")
        print("[INFO] Make sure you run this from main.py")
