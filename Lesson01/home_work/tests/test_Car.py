import pytest
from hw_Car import Car


def test_create_car():
    car1 = Car(120, 1)
    assert car1.capacity == 120
    assert car1.gas_per_km == 1
    assert car1.gas == 0


def test_fill():
    car1 = Car(120, 1)
    assert car1.gas == 0
    car1.fill(70)
    assert car1.gas == 70
    car1.fill(70)
    assert car1.gas == 120

def test_ride():
    car1 = Car(120, 1, 80)
    assert car1.gas == 80
    car1.ride(50)
    assert car1.gas == 30
    car1.ride(50)
    assert car1.gas == 0