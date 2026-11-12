import numpy as np
import pytest

from heatsim import Plate, simulate, stable_dt


def test_insulated_plate_conserves_heat():
    plate = Plate(nx=20, ny=20, alpha=0.2, boundary="insulated")
    plate.set_hot_spot(10, 10, 3, 100.0)
    before = plate.field[1:-1, 1:-1].sum()
    simulate(plate, steps=50)
    assert plate.field[1:-1, 1:-1].sum() == pytest.approx(before, rel=0.05)


def test_heat_spreads_out():
    plate = Plate(nx=20, ny=20, alpha=0.2)
    plate.set_hot_spot(10, 10, 2, 100.0)
    peak = plate.field.max()
    simulate(plate, steps=50)
    assert plate.field.max() < peak


def test_stable_dt():
    assert stable_dt(Plate(nx=4, ny=4, alpha=0.25)) == 1.0


def test_unknown_boundary():
    with pytest.raises(ValueError):
        simulate(Plate(nx=4, ny=4, alpha=0.1, boundary="periodic"), steps=1)
