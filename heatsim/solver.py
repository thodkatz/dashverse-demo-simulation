import numpy as np


def stable_dt(plate):
    """Largest stable explicit time step."""
    return plate.dx ** 2 / (4 * plate.alpha)


def step(plate, dt):
    u = plate.field
    lap = np.zeros_like(u)
    lap[1:-1, 1:-1] = (u[2:, 1:-1] + u[:-2, 1:-1] + u[1:-1, 2:] + u[1:-1, :-2] - 4 * u[1:-1, 1:-1]) / plate.dx ** 2
    u = u + plate.alpha * dt * lap
    if plate.boundary == "insulated":
        u[0, :] = u[1, :]
        u[-1, :] = u[-2, :]
        u[:, 0] = u[:, 1]
        u[:, -1] = u[:, -2]
    elif plate.boundary == "fixed":
        u[0, :] = plate.field[0, :]
        u[-1, :] = plate.field[-1, :]
        u[:, 0] = plate.field[:, 0]
        u[:, -1] = plate.field[:, -1]
    else:
        raise ValueError("unknown boundary " + plate.boundary)
    plate.field = u
    return u


def simulate(plate, steps, dt=None, callback=None):
    dt = dt or stable_dt(plate)
    if dt > stable_dt(plate):
        print("warning: dt above the stability limit")
    for i in range(steps):
        step(plate, dt)
        if callback is not None and i % 10 == 0:
            callback(i, plate.field)
    return plate.field
