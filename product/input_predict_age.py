import joblib
import pandas as pd
import warnings

warnings.filterwarnings("ignore", category=UserWarning)

model = joblib.load('product/random_forest_exoplanet.pkl')

st_teff = float(input('Stellar Effective Temperature (st_teff): '))
st_mass = float(input('Stellar Mass (st_mass): '))
st_rad = float(input('Stellar Radius (st_rad): '))

mass_rad_ratio = st_mass / (st_rad ** 2 + 1e-6)

X_new = [[st_teff, st_mass, st_rad, mass_rad_ratio]]

prediction = model.predict(X_new)
print('Predicted Stellar Age:', prediction[0]) 