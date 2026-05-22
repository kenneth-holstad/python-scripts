# -*- coding: utf-8 -*-
"""
Created on Wed May 20 18:22:36 2026

@author: kolst
"""

import torch
import torch.nn as nn
from torchvision import datasets, transforms
import matplotlib.pyplot as plt
import numpy as np

# Define a transform to convert images to tensors
transform = transforms.ToTensor()

# Download/load MNIST
train_dataset = datasets.MNIST(root='./data', train=True, download=True, transform=transform)
test_dataset = datasets.MNIST(root='./data', train=False, download=True, transform=transform)

''' if data wasn't pre-split
from torch.utils.data import random_split
generator = torch.Generator().manual_seed(42)
train_dataset, test_dataset = random_split(full_dataset, [0.8, 0.2], generator=generator)
'''

# Create data loaders
train_loader = torch.utils.data.DataLoader(train_dataset, batch_size=32, shuffle=True)
test_loader = torch.utils.data.DataLoader(test_dataset, batch_size=32, shuffle=False)

