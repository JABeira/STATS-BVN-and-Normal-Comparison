import matplotlib.pyplot as plt
import numpy as np

def RVScatterPlot (title:str, colour:str, X:np.array=None,  Y:np.array=None, XY:np.array=None, pointName:str=None) -> None:
    if(XY is not None):
        X=np.array(XY)[:,0]
        Y=np.array(XY)[:,1]
        plt.scatter(X, Y, color=colour, marker='o', label= pointName or "Simulated result", s=1)
    elif(X is not None and Y is not None):
        plt.scatter(X, Y, color=colour, marker='o', label= pointName or "Simulated result", s=1)

    # Add labels and title
    plt.xlabel("X Outcomes")
    plt.ylabel("Y Outcomes")
    plt.title("Scatter Plot: "+title)
    plt.legend()



def ShowPlot():
    plt.show()
