import numpy as np


class Plate:
    """A rectangular plate on a regular grid."""

    def __init__(self, nx, ny, alpha, dx=1.0, boundary="fixed", initial=None):
        self.nx = nx
        self.ny = ny
        self.alpha = alpha
        self.dx = dx
        self.boundary = boundary
        self.field = np.zeros((ny, nx)) if initial is None else np.array(initial, dtype=float)

    def set_hot_spot(self, x, y, radius, temperature):
        yy, xx = np.mgrid[0:self.ny, 0:self.nx]
        mask = (xx - x) ** 2 + (yy - y) ** 2 <= radius ** 2
        self.field[mask] = temperature
