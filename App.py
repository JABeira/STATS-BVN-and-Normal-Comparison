import json
import numpy as np

from src.Plotter import RVScatterPlot
from src.Normal_Gen import generateNormalSimulations


#Reading Constants file
try:
    with open('constants.json') as f:
        constants = json.load(f)
except (FileNotFoundError) as e:
    print("Failed to load constants file")
    exit()

print("Running simulation with the following parameters:", constants)


x = generateNormalSimulations(constants["ux"], constants["sx"], constants["samples"]) 
y = generateNormalSimulations(constants["uy"], constants["sy"], constants["samples"]) 

RVScatterPlot("X,Y Normals","red",x,y)