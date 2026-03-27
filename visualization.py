import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
from calculations import N, trail_length, positions, masses, history
from physics import update

# Plot
fig, ax = plt.subplots(figsize=(7, 7))

# Dark background
ax.set_facecolor("black")
fig.patch.set_facecolor("black")

# Marker size proportional to mass
sizes = masses * 2.5

# Color intensity (light = heavier stars, darker = lighter stars)
colors = np.clip(masses / masses.max(), 0, 1)
colors = plt.cm.inferno(colors)

scat = ax.scatter(positions[:, 0], positions[:, 1], s=sizes, color=colors)

# Trails
lines = []
for i in range(N):
    line, = ax.plot([], [], linewidth=0.5, alpha=0.4, color="cyan")
    lines.append(line)


ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_title("Star Cluster Simulation", color="white")
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

    # Trails:
    for i in range(N):
        history[i].append(positions[i].copy())
        if len(history[i]) > trail_length:
            history[i].pop(0)
        trail = np.array(history[i])
        lines[i].set_data(trail[:, 0], trail[:, 1])
    return [scat] + lines


ani = FuncAnimation(fig, animate, interval=20)

def run_animation():
    plt.show()
