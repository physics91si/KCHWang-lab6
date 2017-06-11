import numpy as np
import matplotlib.pyplot as plt

# Part 1: Indices and 2D matrices
arr = np.zeros((9, 9))
arr[:, 0:3] = 1
arr[-1, :] = 1
arr[[4, 7, 1], [5, 7, 8]] = 1
plt.spy(arr)
plt.savefig('arr')