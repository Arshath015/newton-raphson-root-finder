## Newton-Raphson Root Finding Submodule
![Python](https://img.shields.io/badge/python-3.10-blue.svg)
![MIT License](https://img.shields.io/badge/License-MIT-yellow.svg)
A submodule implementing the Newton-Raphson root finding technique from first principles.
## Table of Contents
* [Overview](#overview)
* [Tech Stack](#tech-stack)
* [Architecture](#architecture)
* [Theoretical Background](#theoretical-background)
* [Installation](#installation)
* [Usage](#usage)
* [API Reference](#api-reference)
* [Case Studies](#case-studies)
* [Testing](#testing)
* [Limitations](#limitations)
* [Roadmap](#roadmap)
* [License](#license)
## Overview
The Newton-Raphson method is a root finding technique used to find successively better approximations to the roots of a real-valued function.
## Tech Stack
* Python 3.10
* NumPy
## Architecture
```text
+---------------+
|  NewtonRaphson  |
+---------------+
|  +-----------+  |
|  |  Function  |  |
|  +-----------+  |
|  +-----------+  |
|  |  Convergence|  |
|  +-----------+  |
+---------------+
```
## Theoretical Background
The Newton-Raphson method uses the first few terms of the Taylor series of a function f(x) in the vicinity of a suspected root to produce successively better approximations to the root. The method starts with an initial guess for the root, then iteratively applies a correction to the guess using the formula: x_n+1 = x_n - f(x_n) / f'(x_n).
Convergence analysis is performed by checking the absolute difference between successive approximations. If the difference is less than a specified tolerance, the method converges.
For a function f(x) with a root at x = r, the Newton-Raphson method converges quadratically, meaning that the number of correct digits in the approximation roughly doubles with each iteration.
## Installation
First, install the required packages using pip: 
pip install -r requirements.txt
Then, clone this repository: 
git clone https://github.com/your-username/newton-raphson-root-finder.git
## Usage
Here is an example usage of the NewtonRaphson class:
```python
from src.newton_raphson import NewtonRaphson
from src.function import Function

# Define a function
f = Function(lambda x: x**2 - 2)

# Create a NewtonRaphson object
nr = NewtonRaphson(f, 1.0)

# Find the root
root = nr.find_root()
print(root)
```
## API Reference
* `class NewtonRaphson(function: Function, initial_guess: float)`: The main class for the Newton-Raphson method.
* `class Function(f: Callable[[float], float])`: A class representing a mathematical function.
* `def find_root(self, tolerance: float = 1e-5, max_iter: int = 100) -> float`: Finds the root of the function using the Newton-Raphson method.
## Case Studies
See [case-study.md](case_studies/case-study.md) for a real-world example of using this submodule.
## Testing
See [tests](tests) for the test suite.
## Limitations
The Newton-Raphson method requires the function to be differentiable and the initial guess to be sufficiently close to the root.
## Roadmap
* Improve the convergence analysis to handle more complex functions.
* Add support for multiple roots.
## License
This submodule is licensed under the MIT License.