# heatsim

Finite-difference simulation of 2D heat diffusion on a rectangular plate, with fixed (Dirichlet) or insulated (Neumann)
boundaries.

This repository is a **demo** for the EVERSE DashVERSE dashboards: it plays the part of simulation code that is
half-way to good practice, and it improves over a few commits.

## Usage

```sh
pip install -r requirements.txt
python examples/hot_corner.py
```

```python
from heatsim import Plate, simulate
plate = Plate(nx=50, ny=50, alpha=1e-4)
field = simulate(plate, steps=500, dt=0.1)
```

## Contact

Questions: open an issue.
