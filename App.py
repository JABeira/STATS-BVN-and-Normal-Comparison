import json
import numpy as np

import src.Plotter as Plot

#Reading Constants file
try:
    with open('constants.json') as f:
        constants = json.load(f)
except (FileNotFoundError) as e:
    print("Failed to load constants file")
    exit()

print("Running simulation with the following parameters:", constants)


x = np.random.rand(50)  
y = np.random.rand(50)