import subprocess
import sys
import os

os.system('clear')

files = {
    1: 'model/random_forest/rf_orig.py',
    2: 'model/random_forest/rf_with_gridsearchcv.py',
    3: 'model/random_forest/test_check.py'
}

print("""
1. Create RF model (w/ feature importance, permutation importance, and Mutual Information | Hypertuned, RepeatedKFold, Best Model)
2. Create RF model (GridSearchCV | may take longer)
3. RF test check
4. Back
""")

choice = int(input("Choose to continue: "))

while True:
    try:
        if 1 <= choice <= 3:
            run = files.get(choice)
            subprocess.run(['python', f'{run}'])
            sys.exit()
        elif choice == 4:
            subprocess.run(['python', 'main.py'])
            sys.exit()
        else:
            print('[ERROR] Invalid input. Choose between 1 - 4 only.')
    except ValueError:
            print('[ERROR] Enter a valid integer.')
    
