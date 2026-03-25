import numpy as np
import matplotlib.pyplot as plt


masses = []
# Scaled value for the gravitational constant:
G = 1.0
# Increment for dt (change in time):
dt = 0.01


# Finding the acceleration by applying the distance between two masses:

def acceleration_calculation(positions, masses):
    n = len(masses)
    acceleration = np.zeros_like(positions)

    for i in range(n):
        for j in range(n):
            if i == j:
                continue

            r = positions[j] - positions[i]
            distance = np.linalg.norm(r)
            acceleration[i] += G * masses[j] * r / (distance ** 3)

    return acceleration


# To update the motion over time:

def update(positions, velocities, masses):
    acceleration = acceleration_calculation(positions, masses)
    velocities += acceleration * dt
    positions += velocities * dt

    return positions, velocities


# To record position:

steps = 1000
trajectory = []
for step in range(steps):
    positions, velocities = update(positions, velocities, masses)
    trajectory.append(positions.copy())

trajectory = np.array(trajectory)


# To plot orbits:

for i in range(len(masses)):
    plt.plot(trajectory[:, i, 0], trajectory[:, i, 1])

plt.xlabel("x")
plt.ylabel("y")
plt.title("N-body Simulation")
plt.show()


# Animating the N-body simulation:

plt.ion()

for step in range(steps):
    positions, velocities = update(positions, velocities, masses)
    plt.clf()
    plt.scatter(positions[:, 0], positions[:, 1])
    plt.xlim(-20, 20)
    plt.ylim(-20, 20)
    plt.pause(0.01)
plt.ioff()
plt.show()


# Kinetic energy calculation:

def kinetic_energy(velocities, masses):
    speed_sq = np.sum(velocities ** 2, axis = 1)
    return 0.5 * np.sum(masses * speed_sq)

n = 100
