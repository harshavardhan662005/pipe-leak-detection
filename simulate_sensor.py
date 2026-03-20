import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# 1. Setup Parameters (100 minutes of data)
num_readings = 100
start_time = datetime.now()
pipe_id = "PIPE_001"
data = []

print("Starting simulation...")

# 2. Generate the data loop
for i in range(num_readings):
    current_time = start_time + timedelta(minutes=i)
    
    # Normal operating conditions (Pressure around 50, Vibration low)
    pressure = np.random.uniform(45, 55)  
    vibration = np.random.uniform(0.1, 0.5) 
    
    # THE BURST: Force a drop at reading #75
    if i >= 75:
        pressure = np.random.uniform(5, 15)   # Pressure crashes
        vibration = np.random.uniform(2.0, 5.0) # Vibration spikes
        
    data.append([current_time, pipe_id, pressure, vibration])

# 3. Create the Spreadsheet (CSV)
df = pd.DataFrame(data, columns=['Time', 'Pipe_ID', 'Water_Pressure', 'Acoustic_Vibration'])
df.to_csv('sensor_data.csv', index=False)

print("Success! File created: sensor_data.csv")