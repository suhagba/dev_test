"""
Re-write this NumPy code so that it is vectorized.
ie. replace the for loops with only NumPy array operations.

It might be useful to work this out with a pen and paper before writing the answer.
"""
import numpy as np

# A matrix defining how different locations (home, work, school) infect other people.
# Rows are infectors, columns are infectees.
infect_matrix = np.array([
    [0.9, 0.05, 0.05],
    [0.05, 0.9, 0.05],
    [0.05, 0.05, 0.9],
])

# Compartments of people (home, work, school).
infectors = np.array([10.0, 19.0, 35.0]) # people who can infect other people


infected = infect_matrix.dot(infectors) # number of people who got infected


print("Number of people infected (home, work, school):", infected)
