import pytest
from drone import Drone

def test_distance_to():
    d = Drone(0, 0, 10, 100)
    assert d.distance_to(3,4) == 5.0

def test_move_toward_reduces_fuel():
    d = Drone(0,0,10,100)
    d.move_toward(3, 4)
    assert d.fuel < 100

def test_move_toward_already_at_target():
    d = Drone(5,5,10,100)
    result = d.move_toward(5,5)
    assert result == 0.0

def test_fuel_does_not_go_negative():
    d = Drone(0,0,10,5)
    d.move_toward(100,100)
    assert d.fuel >= 0