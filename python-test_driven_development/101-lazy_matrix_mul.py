#!/usr/bin/python3
"""
Module for matrix multiplication using NumPy
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices using NumPy

    Args:
        m_a (list of lists): First matrix
        m_b (list of lists): Second matrix

    Returns:
        numpy.ndarray: Result of matrix multiplication

    Raises:
        TypeError: If m_a or m_b is not a list or list of lists
        ValueError: If matrices cannot be multiplied
    """
    # Check if m_a is a list
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")

    # Check if m_b is a list
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    # Check if m_a is a list of lists
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")

    # Check if m_b is a list of lists
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    # Check if m_a is empty
    if len(m_a) == 0 or any(len(row) == 0 for row in m_a):
        raise ValueError("m_a can't be empty")

    # Check if m_b is empty
    if len(m_b) == 0 or any(len(row) == 0 for row in m_b):
        raise ValueError("m_b can't be empty")

    # Check if all elements in m_a are integers or floats
    for row in m_a:
        if not all(isinstance(elem, (int, float)) for elem in row):
            raise TypeError("m_a should contain only integers or floats")

    # Check if all elements in m_b are integers or floats
    for row in m_b:
        if not all(isinstance(elem, (int, float)) for elem in row):
            raise TypeError("m_b should contain only integers or floats")

    # Check if m_a is a rectangle (all rows have the same size)
    if len(set(len(row) for row in m_a)) > 1:
        raise TypeError("each row of m_a must be of the same size")

    # Check if m_b is a rectangle (all rows have the same size)
    if len(set(len(row) for row in m_b)) > 1:
        raise TypeError("each row of m_b must be of the same size")

    # Check if matrices can be multiplied (columns of m_a = rows of m_b)
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # All checks passed, perform matrix multiplication
    try:
        return np.matmul(m_a, m_b)
    except Exception as e:
        # This is a fallback for any unexpected NumPy errors
        # Should not typically be reached due to our prior checks
        if "shapes" in str(e):
            shapes_a = f"({len(m_a)},{len(m_a[0])})"
            shapes_b = f"({len(m_b)},{len(m_b[0])})"
            return f"shapes {shapes_a} and {shapes_b} not aligned: {len(m_a[0])} (dim 1) != {len(m_b)} (dim 0)"
        else:
            return str(e)
