from typing import Callable
from src.function import Function
import numpy as np
class NewtonRaphson:
    def __init__(self, function: Function, initial_guess: float):
        self.function = function
        self.initial_guess = initial_guess
    def find_root(self, tolerance: float = 1e-5, max_iter: int = 100) -> float:
        x_n = self.initial_guess
        for _ in range(max_iter):
            f_x_n = self.function.evaluate(x_n)
            f_prime_x_n = self.function.derivative(x_n)
            x_n_plus_1 = x_n - f_x_n / f_prime_x_n
            if abs(x_n_plus_1 - x_n) < tolerance:
                return x_n_plus_1
            x_n = x_n_plus_1
        raise RuntimeError('Failed to converge')