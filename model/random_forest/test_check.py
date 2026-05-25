from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split, cross_val_score 
import pandas as pd
import numpy as np
import os

os.system('clear')

print('main menu -> random forest -> [3]')

df = pd.read_csv('data/data_3.csv')

df['mass_rad_ratio'] = (df['st_mass'] / (df['st_rad'] ** 2 + 1e-6))

X = df[['st_teff', 'st_mass', 'st_rad', 'mass_rad_ratio']]
y = df['st_age']

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.3,
    random_state=100
)

rf_model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

rf_model.fit(X_train, y_train)

y_pred = rf_model.predict(X_test)

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

importance = rf_model.feature_importances_

for feature, score in zip(X.columns, importance):
    print(feature, score)
    
train_score = rf_model.score(X_train, y_train)
test_score = rf_model.score(X_test, y_test)

print("Train R²:", train_score)
print("Test R²:", test_score)

scores = cross_val_score(
    rf_model,
    X,
    y,
    cv=5,
    scoring='r2'
)

print(scores)
print("Average R²:", scores.mean())