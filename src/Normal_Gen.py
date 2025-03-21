import numpy as np

def generateNormalSimulations(u, s, samples:int) -> np.array:
    normal = np.random.normal(u,s,samples)
    return normal

def generateBivariantNormalSimulations(ux, sx, uy, sy, cov, samples:int) -> np.array:
    BivariantNormal = np.random.multivariate_normal([ux,uy], [[sx**2,cov],[cov,sy**2]], samples)
    return BivariantNormal
