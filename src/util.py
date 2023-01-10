import os
import pandas as pd
import numpy as np
from pathlib import Path
from scipy.spatial.distance import euclidean

def load_dataset(filename):
    return pd.read_pickle(os.path.join(Path.cwd().resolve(), 'data', 'processed', filename))

def shannon_diversity(data):
    n = data
    N = sum(data)
    p = n/N
    H = -sum(p*np.log(p))
    evenness = H/np.log(len(data))
    return evenness

def compute_similarity(W):
    similarity_map = []
    
    for i in range(W.shape[-1]):
        sim = []
        for j in range(W.shape[-1]):
            sim.append(euclidean(W[:, :, i].flatten().reshape(-1, 1), W[:, :, j].flatten().reshape(-1, 1)))
        similarity_map.append(sim)
    
    return similarity_map

def calculate_map_size(data, lattice='rectangular'):
    """
    Source: https://github.com/sevamoo/SOMPY/blob/master/sompy/sompy.py
    Calculates the optimal map size given a dataset using eigenvalues and eigenvectors. Matlab ported
    :lattice: 'rect' or 'hex'
    :return: map sizes
    """
    D = data.copy()
    dlen = D.shape[0]
    dim = D.shape[1]
    munits = np.ceil(5 * (dlen ** 0.5))
    A = np.ndarray(shape=[dim, dim]) + np.Inf

    for i in range(dim):
        D[:, i] = D[:, i] - np.mean(D[np.isfinite(D[:, i]), i])

    for i in range(dim):
        for j in range(dim):
            c = D[:, i] * D[:, j]
            c = c[np.isfinite(c)]
            A[i, j] = sum(c) / len(c)
            A[j, i] = A[i, j]

    VS = np.linalg.eig(A)
    eigval = sorted(np.linalg.eig(A)[0])
    if eigval[-1] == 0 or eigval[-2] * munits < eigval[-1]:
        ratio = 1
    else:
        ratio = np.sqrt(eigval[-1] / eigval[-2])

    if lattice == "rect":
        size1 = min(munits, round(np.sqrt(munits / ratio)))
    else:
        size1 = min(munits, round(np.sqrt(munits / ratio*np.sqrt(0.75))))

    size2 = round(munits / size1)

    return [int(size1), int(size2)]