from src.newton_raphson import NewtonRaphson
from src.function import Function
# Define a function
f = Function(lambda x: x**2 - 2)
# Create a NewtonRaphson object
nr = NewtonRaphson(f, 1.0)
# Find the root
root = nr.find_root()
print(root)