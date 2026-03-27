import numpy as np
from calculations import N, G, dt, softening, masses, positions, velocities


# Computations for gravitational acceleration:

def compute_acceleration(positions):
    acceleration = np.zeros_like(positions)
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            dx = positions[j][0] - positions[i][0]
            dy = positions[j][1] - positions[i][1]
            distance = np.sqrt(dx**2 + dy**2) + softening
            force = G * masses[j] / (distance**3)
            acceleration[i][0] += force * dx
            acceleration[i][1] += force * dy
    return acceleration


# Updating positions and velocities over time:

def update():
    global positions, velocities
    acceleration = compute_acceleration(positions)
    for i in range(N):
        velocities[i] += acceleration[i] * dt
        positions[i] += velocities[i] * dt
