import subprocess
import os
import sys

os.system('clear')

files = {
    1: 'product/filter_unknown_age.py',
    2: 'product/predict_age.py',
    3: 'product/input_predict_age.py'
}

print("""
main menu -> prediction menu
1. Filter with unknown age (filter_unknown_age.py)
2. Predict Stellar Age with CSV file
3. Predict Stellar Age (manual)
4. Back
""")

while True:
    try:
        choice = int(input("Choose a number: "))
        
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


