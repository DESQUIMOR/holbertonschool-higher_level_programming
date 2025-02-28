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
    if not isinstance(m_a, list) or not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not isinstance(m_b, list) or not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")
    if not all(isinstance(num, (int, float)) for row in m_a for num in row):
        raise TypeError("m_a should contain only integers or floats")
    if not all(isinstance(num, (int, float)) for row in m_b for num in row):
        raise TypeError("m_b should contain only integers or floats")
    if not m_a or any(len(row) == 0 for row in m_a):
        raise ValueError("m_a can't be empty")
    if not m_b or any(len(row) == 0 for row in m_b):
        raise ValueError("m_b can't be empty")
    if len(set(len(row) for row in m_a)) > 1:
        raise TypeError("each row of m_a must be of the same size")
    if len(set(len(row) for row in m_b)) > 1:
        raise TypeError("each row of m_b must be of the same size")
    
    return np.matmul(m_a, m_b).tolist()
