#!/usr/bin/python3
"""
Module that defines lazy_matrix_mul function using NumPy.
"""

import numpy as np

def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices using NumPy.

    Args:
        m_a (list of lists of ints/floats): First matrix.
        m_b (list of lists of ints/floats): Second matrix.
    
    Returns:
        list of lists of ints/floats: Resulting matrix.
    
    Raises:
        TypeError: If m_a or m_b is not a list of lists of integers/floats.
        ValueError: If m_a or m_b is empty or if they cannot be multiplied.
    """
    try:
        return np.matmul(m_a, m_b).tolist()
    except ValueError:
        raise ValueError("m_a and m_b can't be multiplied")
    except TypeError:
        raise TypeError("Both matrices must be lists of lists of integers or floats")
