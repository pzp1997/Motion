#!/usr/bin/env python2.7

import numpy as np
from munkres import Munkres
from operator import itemgetter

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
    """Returns distance between ``pt1`` and ``pt2``"""
    return ((pt1[0]-pt2[0])**2 + (pt1[1]-pt2[1])**2)**0.5


def pad_to_square(mat, pad_val=0):
    """Returns a square matrix of ``mat`` padded with ``pad_val``"""
    
    pad_width = (((0,0), (0,mat.shape[0]-mat.shape[1]))
                 if mat.shape[0] > mat.shape[1] else
                 ((0,mat.shape[1]-mat.shape[0]), (0,0)))

    return np.pad(mat, pad_width, mode='constant', constant_values=pad_val)


def find_ids_of_objects(positions, predictions):
    """Returns the new indices of each object based on Hungarian Algorithm"""
    if len(positions) < 1 or len(predictions) < 1:
        return []
    
    distance_matrix = create_distance_matrix(positions, predictions)
    distance_matrix = pad_to_square(distance_matrix, np.amax(distance_matrix))
    
    indices = munk.compute(distance_matrix)
    indices = [idx[1] for idx in indices if idx[1] < len(predictions)]

    new_order = itemgetter(*indices)(predictions)
    return new_order if len(indices) > 1 else (new_order,)
