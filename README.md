# N-body-Gravitational-Simulation
N-Body Gravitational Simulation Using Python (work in progress)

A physics simulation of gravitational interactions between multiple bodies using Newton's law of gravitation.

## Features:
- Simulates N-body gravitational systems
- Real-time animation
- Orbit trajectory visualization
- Implemented pause feature (press spacebar)
- Turn on/off body merging feature (press m)
- Total energy graph (potential energy + kinetic energy) as a function of time

## Physics:
Each body interacts with every other body using:
$F = {G {m_1 m_2} \over {r²}}$
\
This is extended to compute acceleration and update motion over time.
To calculate the total energy, the Virial Theorem is used:
$2KE = PE$
This demonstrates conservation of energy when body merging is off.

## Tech Stack Used:
- Python
- NumPy
- Matplotlib

## Future Features:
- 3D simulations
- Tidal fields
- Energy loss in stars

## To Run Simulation:
- pip install numpy matplotlib
- python main_simulation.py
- Press "m" key to turn on/off merging
- Press spacebar to pause/unpause
