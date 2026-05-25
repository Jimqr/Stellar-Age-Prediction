import subprocess
import os
import sys

os.system('clear')

files = {
    1: 'api.py',
    2: 'filter.py',
    3: 'correlation/menu.py',
    4: 'model/linear_regression/linear_regression_menu.py',
    5: 'model/random_forest/rf_menu.py',
    6: 'model/xgboost/test2.py',
    7: 'product/menu.py'
}

print("""
1. Request data from NASA Exoplanet Archive
2. Filter the data (check filter.py)
3. Correlation
4. Linear Regression
5. Random Forest (with GridSearchCV)
6. XGBoost
7. Predict Stellar Age (Random Forest Model is used from No. 5)
""")

while True:
    try:
        choice = int(input('Choose to continue: '))
            
        if 1 <= choice <= 7:
            run = files.get(choice)
            subprocess.run(['python', f'{run}'])
            sys.exit()
        else:
            print('[ERROR] Invalid input. Choose between 1 - 7 only.')
    except ValueError:
        print('[ERROR] Enter a valid integer.')
    
