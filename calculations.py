import numpy as np

# Values for constants:
N = 200  # Number of stars
G = 1.0  # Simplified gravitational constant
dt = 0.01  # Simplified change in time
softening = 0.1  # To avoid divide by zero
trail_length = 30  # To track & visualize motion over time

np.random.seed(1)

# Initialize masses
masses = np.random.uniform(0.5, 2.0, N)


# Positions & velocities
positions = np.random.randn(N, 2) * 0.5
velocities = (np.random.randn(N, 2) * 0.3) / np.sqrt(masses)[:, np.newaxis]


# For loop to add rotation:
for i in range(N):
    x, y = positions[i]

    # Rotation
    velocities[i][0] += -y * 0.2
    velocities[i][1] += x * 0.2

    # Slight explosion
    velocities[i] += positions[i] * 0.1


# Trail history
history = []
for i in range(N):
    history.append([])
