from sklearn import linear_model, metrics
from sklearn.linear_model import LinearRegression
from sklearn import metrics
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split, cross_val_score
import pandas as pd
import seaborn as sns
import numpy as np
import sys

x_select = sys.argv[1:-1]
x_data = sys.argv[-1]

df = pd.read_csv(x_data)

X = df[x_select]

y = df['st_age']

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.3,
    random_state=100
)

reg_model = linear_model.LinearRegression()
reg_model.fit(X_train, y_train)

y_pred= reg_model.predict(X_test)  
x_pred= reg_model.predict(X_train)

print("Prediction for test set: {}".format(y_pred))

reg_model_diff = pd.DataFrame({'Actual value': y_test, 'Predicted value': y_pred})
reg_model_diff

mae = metrics.mean_absolute_error(y_test, y_pred)
mse = metrics.mean_squared_error(y_test, y_pred)
r2 = np.sqrt(metrics.mean_squared_error(y_test, y_pred))
r23 = r2_score(y_test, y_pred)

print("R²:", r23)
print('Mean Absolute Error:', mae)
print('Mean Square Error:', mse)
print('Root Mean Square Error:', r2)
