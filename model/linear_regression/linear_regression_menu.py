import subprocess
import os
import sys

os.system('clear')

x_select = {
    1: ['st_teff', 'st_mass', 'st_lum', 'st_rad', 'st_met', 'st_logg','st_rotp'],
    2: ['st_teff', 'st_mass', 'st_lum', 'st_rad', 'st_met', 'st_logg'],
    3: ['st_teff', 'st_mass', 'st_rad', 'st_met', 'st_logg']
}
x_data = {
    1: 'data/data_1.csv',
    2: 'data/data_2.csv',
    3: 'data/data_3.csv'
}

print("""
main menu -> linear regression menu
1. Experiment 1
2. Experiment 2
3. Experiment 3
4. Back
""")

while True:
    try:
        choice = int(input('Choose to continue: '))
            
        if 1 <= choice <= 3:
            args = ['python', 'model/linear_regression/linear_regression.py']
            args += x_select.get(choice)
            args += [x_data.get(choice)]
            subprocess.run(args)
            sys.exit()
        elif choice == 4:
            subprocess.run(['python', 'main.py'])
            sys.exit()
        else:
            print('[ERROR] Invalid input. Choose between 1 - 4 only.')
    except ValueError:
        print('[ERROR] Enter a valid integer.')
        
