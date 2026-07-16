import pytest
from src.newton_raphson import NewtonRaphson
from src.function import Function
@pytest.mark.parametrize('initial_guess, expected_root', [(1.0, 1.4142135623730951), (2.0, 1.4142135623730951)])
def test_newton_raphson(initial_guess, expected_root):
    f = Function(lambda x: x**2 - 2)
    nr = NewtonRaphson(f, initial_guess)
    root = nr.find_root()
    assert abs(root - expected_root) < 1e-5