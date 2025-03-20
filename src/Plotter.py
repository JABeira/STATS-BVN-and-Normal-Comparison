import matplotlib.pyplot as plt
import numpy as np

def RVScatterPlot (title:str, colour:str, X:np.array,  Y:np.array) -> None:
    plt.scatter(X, Y, color=colour, marker='o', label='Simulated Results', s=1)

    # Add labels and title
    plt.xlabel("X Outcomes")
    plt.ylabel("Y Outcomes")
    plt.title("Scatter Plot: "+title)
    plt.legend()
    
    # Show the plot
    plt.show()

