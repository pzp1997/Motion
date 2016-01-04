import numpy as np

"""
def pad_to_square(mat, pad_val=0):
    max_dim = max(mat.shape)
    diff_dim = max_dim - min(mat.shape)

    if mat.shape[0] > mat.shape[1]:
        return np.hstack((mat, [[pad_val] * diff_dim] * max_dim))
    if mat.shape[1] > mat.shape[0]:
        return np.vstack((mat, [[pad_val] * max_dim] * diff_dim))
    return mat
"""

def pad_to_square(mat, pad_val=0):
    if mat.shape[0] > mat.shape[1]:
        return np.hstack(
            (mat, [[pad_val] * (mat.shape[0] - mat.shape[1])] * mat.shape[0]))
    if mat.shape[0] < mat.shape[1]:
        return np.vstack(
            (mat, [[pad_val] * mat.shape[1]] * (mat.shape[1] - mat.shape[0])))
    return mat

def pad_to_square(a, pad_value=0):
    m = a.reshape((a.shape[0], -1))
    padded = pad_value * np.ones(2 * [max(m.shape)], dtype=m.dtype)
    padded[0:m.shape[0], 0:m.shape[1]] = m
    return padded

def pad_to_square(mat, pad_val=0):
    padded = np.full((max(mat.shape), max(mat.shape)), pad_val)
    padded[:mat.shape[0],:mat.shape[1]] = mat
    return padded


def hungarian_algo(cost_mat):
    for r in cost_mat:
        r -= min(r)

def pad_to_square(mat, pad_val=0):
    if mat.shape[0] > mat.shape[1]:
        pad_width = ((0,0), (0,mat.shape[0]-mat.shape[1]))
    else:
        pad_width = ((0,mat.shape[1]-mat.shape[0]), (0,0))

    return np.pad(mat, pad_width, mode='constant', constant_values=pad_val)


class MultiTracker(object):
    def __init__(self):
        first = True

    def update(arr):
        
        
        
