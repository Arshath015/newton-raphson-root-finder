from src.newton_raphson import NewtonRaphson
from src.function import Function
import sys
if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python main.py <initial_guess>')
        sys.exit(1)
    initial_guess = float(sys.argv[1])
    f = Function(lambda x: x**2 - 2)
    nr = NewtonRaphson(f, initial_guess)
    root = nr.find_root()
    print(root)