import numpy as np

# Values for constants:
N = 250  # Number of stars
G = 0.25  # Simplified gravitational constant
dt = 0.005  # Simplified change in time
softening = 0.1  # To avoid divide by zero
trail_length = 50  # To track & visualize motion over time
merge_distance = 0.01 # Merges if distance reaches this value
enable_merge = False # Merge feature initially off

np.random.seed(1)

# Initialize masses
masses = np.random.uniform(0.5, 2.0, N)


# Positions & velocities
positions = np.random.randn(N, 2) * 0.5
velocities = (np.random.randn(N, 2) * 0.3) / np.sqrt(masses)[:, np.newaxis]


# For loop to add rotation:
for i in range(len(positions)):
    x, y = positions[i]

    # Rotation
    velocities[i][0] += -y * 0.5
    velocities[i][1] += x * 0.5

    # Slight explosion
    velocities[i] += positions[i] * 0.05


# Trail history
history = []
for i in range(len(positions)):
    history.append([])
