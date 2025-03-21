import json
import numpy as np

from src.Plotter import (RVScatterPlot, ShowPlot)
from src.Normal_Gen import (generateNormalSimulations, generateBivariantNormalSimulations)


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

RVScatterPlot("X,Y Bivariant Normal","red",X=x,Y=y, pointName="X,Y IDP. Normal")

xy = generateBivariantNormalSimulations(constants["ux"], constants["sx"], constants["uy"], constants["sy"], constants["covariance"], constants["samples"])

RVScatterPlot("X,Y Bivariant Normal" ,"blue", XY=xy, pointName="BVN Cov = "+str(constants["covariance"]))

ShowPlot()