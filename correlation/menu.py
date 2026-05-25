import subprocess
import os
import sys

os.system('clear')

data = {
    1: 'st_mass',
    2: 'st_teff',
    3: 'st_lum',
    4: 'st_rad',
    5: 'st_met',
    6: 'st_logg',
    7: 'st_rotp'
}

print("""
main menu -> correlation menu | what stellar parameter should we correlate to stellar age?
1. Mass
2. Effective Temperature
3. Luminosity
4. Radius
5. Stellar Metallicity
6. Log Surface Gravity
7. Stellar Rotation Period
8. Back
""")

while True:
    try:
        choice = int(input('Choose a number: '))
        
        if 1 <= choice <= 7:
            run = data.get(choice)
            subprocess.run(['python', 'correlation/correlation-to-age.py', run])
            sys.exit()
        elif choice == 8:
            subprocess.run(['python', 'main.py'])
            sys.exit()
        else:
            print('[ERROR] Invalid input. Choose between 1 - 8 only.')
    except ValueError:
        print('[ERROR] Enter a valid integer.')
