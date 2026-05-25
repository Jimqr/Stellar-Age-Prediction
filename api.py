import requests
from io import StringIO
import pandas as pd
import url
import os
import subprocess
import time

os.system('clear')

def checking_status():
    print('[INFO] Connecting to NASA Exoplanet Archive...', end='\r')
    
    try:
        result = requests.get(url.url)
        
        status_messages = {
            200: "[SUCCESS] Connection established successfully.",
            403: "[ERROR] Access forbidden (403).",
            404: "[ERROR] Resource not found (404).",
            500: "[ERROR] Internal server error (500)."
}
        
        message = status_messages.get(
            result.status_code,
            f"[E] Something went wrong. Please try again later. {result.status_code}")
        print(message)
        
        try:
            os.makedirs("data", exist_ok=True)
            
            if result.status_code == 200:
                df = pd.read_csv(StringIO(result.text))
                
                if df.empty:
                    print("[WARNING] Dataset is empty")
                df.to_csv('data/data.csv', index=False)
                print("[SUCCESS] Dataset saved successfully.")
                print("[INFO] File location: data/data.csv")
        except FileNotFoundError:
            print("[ERROR] Directory not found.")
        except PermissionError:
            print("[ERROR] Permission denied while saving file.")
        except pd.errors.ParserError:
            print("[ERROR] Failed to parse CSV data.")
        except Exception as e:
            print(f"[E] Unexpected error: {e}")
    except requests.exceptions.RequestException as e:
        print(f"[E] Connection failed: {e}")
    
checking_status()

for i in range(5, 0, -1):
    u = 'seconds' if i > 1 else 'second'
    print(f'Returning to main menu in {i} {u}', end='\r')
    time.sleep(1)
subprocess.run(['python', 'main.py'])