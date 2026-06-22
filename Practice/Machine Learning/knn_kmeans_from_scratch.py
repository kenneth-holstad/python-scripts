# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 10:06:36 2026
"""

import numpy as np

'''
An alternative design choice would be to build one more general
"unsupervised method" class and have KNN/KMeans operate within that
but I think it is simpler to define them separately
'''

class KNN:
    def __init__(self, k):
        self.k = k

    def fit(self, X, y):
        self.X_train, self.y_train = X, y   # "training" = just storing data

    def predict(self, X):
        # compute distances, find k nearest, vote/average
        ...


class KMeans:
    def __init__(self, k):
        self.k = k

    def fit(self, X):
        # initialize centroids, then loop: assign -> recompute -> repeat
        ...

    def predict(self, X):
        # assign to nearest centroid
        ...

class PCA:
    def __init__(self, k):
        self.k = k

# general stuff needed

'''
use sklearn only to pull iris/MNIST? any other examples? digits, cancer datasets
could use curl or something instead
actually - this will be out in its own demo folder away from the actual code
so i'll probably just use the sklearn import it's fine
'''

# distance function can be shared between KNN/KMeans
def euclidean_distances(X, Y):
    return np.sqrt(((X[:, None, :] - Y[None, :, :]) ** 2).sum(axis=2))

class StandardScaler:
    def fit(self, X): ...
    def transform(self, X): ...
    
def train_test_split(X, y, test_size=0.2, seed=None):
    rng = np.random.default_rng(seed)
    n = len(X)
    idx = rng.permutation(n)
    split = int(n * (1 - test_size))
    train_idx, test_idx = idx[:split], idx[split:]
    return X[train_idx], X[test_idx], y[train_idx], y[test_idx]