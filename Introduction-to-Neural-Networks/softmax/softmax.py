import numpy as np

def softmax(L):
    exp_i = np.exp(L)
    return np.divide(exp_i, exp_i.sum())
