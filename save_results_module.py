import os
from datetime import datetime

def save_results(scan_type, data):
    os.makedirs("outputs", exist_ok=True)
    filename = f"outputs/{scan_type}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    with open(filename, "w") as f:
        f.write(data)
    return filename
