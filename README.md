# N-body-Gravitational-Simulation
N-Body Gravitational Simulation Using Python (work in progress)

A physics simulation of gravitational interactions between multiple bodies using Newton's law of gravitation.

## Features:
- Simulates N-body gravitational systems
- Real-time animation
- Orbit trajectory visualization
- Implemented pause feature
- Turn on/off body merging feature
- Total energy graph (potential energy + kinetic energy) as a function of time

## Physics:
Each body interacts with every other body using:
$F = G {m_1 * m_2} \over r²$
\
This is extended to compute acceleration and update motion over time.

## Tech Stack Used:
- Python
- NumPy
- Matplotlib

## Future Features:
- 3D simulations

## To Run Simulation:
- pip install numpy matplotlib
- python main_simulation.py
