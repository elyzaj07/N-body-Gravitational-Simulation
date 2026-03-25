import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


N = 200  # Number of stars
G = 1.0  # Simplified gravitational constant
dt = 0.01  # Simplified change in time
softening = 0.1  # To avoid divide by zero
trail_length = 40  # To track & visualize motion over time


np.random.seed(1)
positions = np.random.randn(N, 2) * 0.5
velocities = np.random.randn(N, 2) * 0.3


# For loop to add rotation:

for i in range(N):
    x, y = positions[i]

    # Rotation
    velocities[i][0] += -y * 0.2
    velocities[i][1] += x * 0.2

    # Slight explosion
    velocities[i] += positions[i] * 0.1

# Initialize masses
masses = np.ones(N)

# Trail effect:
history = []
for i in range(N):
    history.append([])


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

    acc = compute_acceleration(positions)

    for i in range(N):
        velocities[i] += acc[i] * dt
        positions[i] += velocities[i] * dt


# Plot:
fig, ax = plt.subplots(figsize=(7, 7))

# dark background
ax.set_facecolor("black")
fig.patch.set_facecolor("black")

scat = ax.scatter(positions[:, 0], positions[:, 1], s=2, color="white")

# trails
lines = []
for i in range(N):
    line, = ax.plot([], [], linewidth=0.5, alpha=0.4, color="cyan")
    lines.append(line)

ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.set_title("Star Cluster Simulation", color="white")

# axes
ax.set_xlabel("X Position", color="white")
ax.set_ylabel("Y Position", color="white")


# Implementing a pause feature:

paused = False

def on_key(event):
    global paused
    if event.key == " ":
        paused = not paused

fig.canvas.mpl_connect("key_press_event", on_key)


# Implementing animation:

def animate(frame):
    global positions

    if not paused:
        update()

    scat.set_offsets(positions)

    # trails
    for i in range(N):
        history[i].append(positions[i].copy())

        if len(history[i]) > trail_length:
            history[i].pop(0)

        trail = np.array(history[i])
        lines[i].set_data(trail[:, 0], trail[:, 1])

    return [scat] + lines

ani = FuncAnimation(fig, animate, interval=20)

plt.show()
