import numpy as np
import calculations as calc


def compute_acceleration(positions, masses):
    n = len(positions)
    acc = np.zeros_like(positions)

    for i in range(n):
        for j in range(n):
            if i == j:
                continue

            dx = positions[j][0] - positions[i][0]
            dy = positions[j][1] - positions[i][1]
            dist = np.sqrt(dx**2 + dy**2) + calc.softening

            force = calc.G * masses[j] / (dist**3)
            acc[i][0] += force * dx
            acc[i][1] += force * dy

    return acc


def merge_bodies(positions, velocities, masses):
    merged = set()
    new_pos, new_vel, new_mass = [], [], []

    n = len(positions)

    for i in range(n):
        if i in merged:
            continue

        for j in range(i + 1, n):
            if j in merged:
                continue

            dx = positions[j][0] - positions[i][0]
            dy = positions[j][1] - positions[i][1]
            dist = np.sqrt(dx**2 + dy**2)

            if dist < calc.merge_distance:
                m1, m2 = masses[i], masses[j]
                total = m1 + m2

                pos = (positions[i]*m1 + positions[j]*m2) / total
                vel = (velocities[i]*m1 + velocities[j]*m2) / total

                new_pos.append(pos)
                new_vel.append(vel)
                new_mass.append(total)

                merged.add(i)
                merged.add(j)
                break

        if i not in merged:
            new_pos.append(positions[i])
            new_vel.append(velocities[i])
            new_mass.append(masses[i])

    return np.array(new_pos), np.array(new_vel), np.array(new_mass)


def update():
    acc = compute_acceleration(calc.positions, calc.masses)

    calc.velocities += acc * calc.dt
    calc.positions += calc.velocities * calc.dt

    # Only merge if enabled:
    if calc.enable_merge:
        calc.positions, calc.velocities, calc.masses = merge_bodies(
            calc.positions, calc.velocities, calc.masses
        )


# Calculating the system's total energy (potential energy + kinetic energy):
def total_energy():
    KE, PE = 0.0, 0.0
    n = len(calc.positions)

    for i in range(n):
        KE += 0.5 * calc.masses[i] * np.sum(calc.velocities[i]**2)

    for i in range(n):
        for j in range(i + 1, n):
            dx = calc.positions[j][0] - calc.positions[i][0]
            dy = calc.positions[j][1] - calc.positions[i][1]
            dist = np.sqrt(dx**2 + dy**2) + calc.softening

            PE -= calc.G * calc.masses[i] * calc.masses[j] / dist

    return KE + PE
