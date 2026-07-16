from typing import Callable
import numpy as np
class Function:
    def __init__(self, f: Callable[[float], float]):
        self.f = f
    def evaluate(self, x: float) -> float:
        return self.f(x)
    def derivative(self, x: float) -> float:
        h = 1e-7
        return (self.evaluate(x + h) - self.evaluate(x - h)) / (2 * h)