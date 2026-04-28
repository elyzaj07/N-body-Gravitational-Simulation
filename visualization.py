import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
import calculations as calc
from physics import update, total_energy


# Background:
fig, ax = plt.subplots(figsize=(7, 7))
ax.set_facecolor("black")
fig.patch.set_facecolor("black")

scat = ax.scatter(calc.positions[:, 0], calc.positions[:, 1])

lines = []
history = [[] for _ in range(len(calc.positions))]

for _ in range(len(calc.positions)):
    line, = ax.plot([], [], linewidth=0.5, alpha=0.4, color="cyan")
    lines.append(line)

ax.set_xlim(-6, 6)
ax.set_ylim(-6, 6)


# Ability to pause/unpause and merge/turn off merge:
paused = False
def on_key(event):
    global paused

    if event.key == " ":
        paused = not paused

    if event.key == "m":
        calc.enable_merge = not calc.enable_merge
        print("Merging:", calc.enable_merge)

fig.canvas.mpl_connect("key_press_event", on_key)


# Initiate lists for data on total energya and time (plot later):
energy_history = []
time_history = []
t = 0


def animate(frame):
    global history, lines, t

    # Features when unpaused:
    if not paused:
        update()
        t += calc.dt
        energy_history.append(total_energy())
        time_history.append(t)

    previous_N = len(history)
    current_N = len(calc.positions)

    # Update trails and lines:
    if current_N != previous_N:
        history = [[] for _ in range(current_N)]

        for line in lines:
            line.remove()

        lines = []
        for _ in range(current_N):
            line, = ax.plot([], [], linewidth=0.5, alpha=0.4, color="cyan")
            lines.append(line)

    # Update scatter
    scat.set_offsets(calc.positions)

    sizes = calc.masses * 3
    scat.set_sizes(sizes)

    colors = calc.masses / calc.masses.max()
    colors = np.clip(colors, 0.35, 1.0)
    scat.set_color(plt.cm.inferno(colors))

    # Trails
    for i in range(current_N):
        history[i].append(calc.positions[i].copy())

        if len(history[i]) > calc.trail_length:
            history[i].pop(0)

        trail = np.array(history[i])
        lines[i].set_data(trail[:, 0], trail[:, 1])

    return [scat] + lines


ani = FuncAnimation(fig, animate, interval=20)


def run_animation():
    # Main simulation:
    ax.set_title("Star Cluster Simulation", color="white")
    plt.show()

    # Energy graph:
    plt.figure(figsize=(10, 6))
    plt.plot(time_history, energy_history, color='cyan')
    plt.xlabel("Time")
    plt.ylabel("Total Energy")
    plt.title("Total Energy vs Time")
    plt.grid(True)
    plt.show()
