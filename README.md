# N-body-Gravitational-Simulation
N-Body Gravitational Simulation Using Python (work in progress)

A physics simulation of gravitational interactions between multiple bodies using Newton's law of gravitation.

## Features:
- Simulates N-body gravitational systems
- Real-time animation
- Orbit trajectory visualization
- Implemented pause feature

## Physics:
Each body interacts with every other body using:
F = G * (m1 * m2) / r²
This is extended to compute acceleration and update motion over time.

## Tech Stack Used:
- Python
- NumPy
- Matplotlib

## Future features:
- Visualize stabilization of energy in N-body system
- Body merging if distance is miniscule enough
- 3D simulations

## To run simulation:
pip install numpy matplotlib
python main_simulation.py
