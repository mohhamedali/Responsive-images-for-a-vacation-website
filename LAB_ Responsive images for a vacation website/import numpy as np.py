import numpy as np
import matplotlib.pyplot as plt

def rule_110(cell, left, center, right):
    if left == 1 and center == 1 and right == 1:
        return 0
    if left == 1 and center == 1 and right == 0:
        return 1
    if left == 1 and center == 0 and right == 1:
        return 1
    if left == 1 and center == 0 and right == 0:
        return 0
    if left == 0 and center == 1 and right == 1:
        return 1
    if left == 0 and center == 1 and right == 0:
        return 1
    if left == 0 and center == 0 and right == 1:
        return 1
    if left == 0 and center == 0 and right == 0:
        return 0

def evolve_array(array):
    new_array = np.zeros_like(array)
    for i in range(1, len(array) - 1):
        new_array[i] = rule_110(array[i - 1], array[i], array[i + 1])
    return new_array

# Initialize the array
array = np.zeros(10)
array[5] = 1  # Set the middle cell to 1 as initial condition

# Evolve the array for 10 iterations
iterations = 10
patterns = [array.copy()]
for _ in range(iterations):
    array = evolve_array(array)
    patterns.append(array.copy())

# Visualize the resulting patterns
plt.imshow(patterns, cmap='binary', interpolation='nearest')
plt.show()
