import numpy as np

def generateNormalSimulations(u, s, samples:int) -> np.array:
    normal = np.random.normal(u,s,samples)
    return normal