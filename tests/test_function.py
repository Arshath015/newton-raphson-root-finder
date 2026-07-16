import pytest
from src.function import Function
@pytest.mark.parametrize('x, expected_value', [(1.0, 1.0), (2.0, 4.0)])
def test_function_evaluate(x, expected_value):
    f = Function(lambda x: x**2)
    assert f.evaluate(x) == pytest.approx(expected_value)