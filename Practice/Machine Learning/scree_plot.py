# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 23:41:23 2026

@author: google
"""

import matplotlib.pyplot as plt
import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import make_blobs

# 1. Generate dummy high-dimensional data
X, _ = make_blobs(n_samples=200, n_features=10, random_state=42)

# 2. Scale the data (Crucial step for PCA)
X_scaled = StandardScaler().fit_transform(X)

# 3. Fit PCA with all components
pca = PCA()
pca.fit(X_scaled)

# 4. Extract the variance explained by each component
exp_variance = pca.explained_variance_ratio_

# 5. Plot the elbow (scree) plot
plt.figure(figsize=(8, 5))
plt.plot(range(1, len(exp_variance) + 1), exp_variance, marker='o', linestyle='--')
plt.title("PCA Elbow Plot (Scree Plot)")
plt.xlabel("Number of Principal Components")
plt.ylabel("Proportion of Variance Explained")
plt.xticks(range(1, len(exp_variance) + 1))
plt.grid(True)
plt.show()
