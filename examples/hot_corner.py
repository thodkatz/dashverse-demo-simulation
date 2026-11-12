import matplotlib.pyplot as plt

from heatsim import Plate, simulate

plate = Plate(nx=60, ny=40, alpha=0.2, boundary="insulated")
plate.set_hot_spot(5, 5, 4, 100.0)
field = simulate(plate, steps=400)
plt.imshow(field, cmap="inferno")
plt.colorbar(label="temperature")
plt.savefig("hot_corner.png")
