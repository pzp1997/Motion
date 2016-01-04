#!/usr/bin/env python2.7

import numpy as np
from munkres import Munkres

munk = Munkres()


def create_distance_matrix(posit, predict):
    """Returns a distance matrix from given
    positions ``posit`` and predictions ``predict``"""
    
    dist_mat = np.empty((len(posit), len(predict)))

    for i, pt1 in enumerate(posit):
        for j, pt2 in enumerate(predict):
            dist_mat[i][j] = dist_btwn(pt1, pt2)

    return dist_mat


def dist_btwn(pt1, pt2):
    return ((pt1[0]-pt2[0])**2 + (pt1[1]-pt2[1])**2)**0.5


def pad_to_square(mat, pad_val=0):
    if mat.shape[0] > mat.shape[1]:
        pad_width = ((0,0), (0,mat.shape[0]-mat.shape[1]))
    else:
        pad_width = ((0,mat.shape[1]-mat.shape[0]), (0,0))

    return np.pad(mat, pad_width, mode='constant', constant_values=pad_val)


def find_ids_of_objects(positions, predictions):
    distance_matrix = create_distance_matrix(positions, predictions)
    distance_matrix = pad_to_square(distance_matrix, np.amax(distance_matrix))
    indices = m.compute(distance_matrix)
    return indices
