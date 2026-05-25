from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.inspection import permutation_importance
from sklearn.feature_selection import mutual_info_regression
from sklearn.model_selection import RepeatedKFold

import pandas as pd
import numpy as np

from rich import print as pr
from rich.table import Table

import joblib
import os

os.system('clear')

print('main menu -> random forest menu -> [1] | this would takes some moment')

table = Table(title=f"Importance feature of Random Forest Model")

table.add_column("Feature")
table.add_column("Importance")

try:
    df = pd.read_csv('data/data_3.csv')
    
    df['mass_rad_ratio'] = (df['st_mass'] / (df['st_rad'] ** 2 + 1e-6))
    
    X = df[['st_teff', 'st_mass', 'st_rad',
             'mass_rad_ratio']] 
    
    y = df['st_age']
    
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.3,
        random_state=100
    )
    
    mi_scores = mutual_info_regression(
    X,
    y,
    random_state=42)
    
    best_model = RandomForestRegressor(
    n_estimators=500,
    max_depth=None,
    min_samples_split=2,
    max_features='sqrt',
    random_state=42,
    n_jobs=-1)

    best_model.fit(X_train, y_train)

    y_pred = best_model.predict(X_test)
    
    cv_scores = cross_val_score(
    best_model,
    X,
    y,
    cv = RepeatedKFold(n_splits=5, n_repeats=3, random_state=42),
    scoring='r2')
    
    print("Cross Validation R² Scores:", cv_scores)
    print("Mean CV R²:", np.mean(cv_scores))
    print("CV Standard Deviation:", np.std(cv_scores))
    
    print("Prediction for test set:")
    print(y_pred)
    
    grid_diff = pd.DataFrame({
        'Actual value': y_test,
        'Predicted value': y_pred
    })
    
    print(grid_diff.head())
    
    mae = mean_absolute_error(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse)
    r2 = r2_score(y_test, y_pred)
    
    print("R²:", r2)
    print("Mean Absolute Error:", mae)
    print("Mean Square Error:", mse)
    print("Root Mean Square Error:", rmse)
    
    importance = best_model.feature_importances_
    
    for feature, score in zip(X.columns, importance):
        table.add_row(
                feature, 
                str(round(score, 5)))
    pr(table)
    
    perm_importance = permutation_importance(
    best_model,
    X_test,
    y_test,
    n_repeats=10,
    random_state=42)

    perm_table = Table(title="Permutation Importance")

    perm_table.add_column("Feature")
    perm_table.add_column("Importance")

    for i in perm_importance.importances_mean.argsort()[::-1]:
        perm_table.add_row(
            X.columns[i],
            str(round(
                perm_importance.importances_mean[i],
                5
            ))
        )

    pr(perm_table)    

    mi_table = Table(title="Mutual Information Scores")

    mi_table.add_column("Feature")
    mi_table.add_column("MI Score")

    for feature, score in zip(X.columns, mi_scores):
        mi_table.add_row(
            feature,
            str(round(score, 5))
        )

    pr(mi_table)

    joblib.dump(best_model, 'random_forest_exoplanet.pkl')
    print("Model saved as random_forest_exoplanet.pkl")
except FileNotFoundError:
        print("[ERROR] Directory not found: data/data_3.csv")
        print("[INFO] Make sure you run this from main.py")

