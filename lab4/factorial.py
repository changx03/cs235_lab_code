"""
The code is written for COMPSCI235 Lab 4 Flask and Jinja. 


Author: Luke Change (xcha011@aucklanduni.ac.nz) 
Date: 23/07/2022
"""

import numpy as np


def compute_factorial(value: int):
    """Computes the factorial of a given input."""
    list_values = np.arange(1, value + 1)
    factorial = list_values.prod()
    return factorial
