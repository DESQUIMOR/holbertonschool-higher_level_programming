#!/usr/bin/python3
"""Module for matrix multiplication using NumPy."""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiply two matrices using NumPy.

    Args:
        m_a: First matrix (list of lists)
        m_b: Second matrix (list of lists)

    Returns:
        numpy.ndarray: Result of matrix multiplication

    Raises:
        ValueError: If matrices cannot be multiplied or contain invalid data
    """
    try:
        # Convert to numpy arrays to check if they're valid matrices
        a = np.array(m_a)
        b = np.array(m_b)
        
        # Check if inputs are scalar (0D arrays)
        if a.ndim == 0 or b.ndim == 0:
            raise ValueError("Scalar operands are not allowed, use '*' instead")
            
        # Perform matrix multiplication
        result = np.matmul(m_a, m_b)
        return result
    except ValueError as e:
        # Handle scalar case specifically
        if str(e) == "Scalar operands are not allowed, use '*' instead":
            raise ValueError("Scalar operands are not allowed, use '*' instead") from e
        # Pass through NumPy's shape mismatch error message
        elif "shapes" in str(e) and "not aligned" in str(e):
            raise ValueError(str(e)) from e
        # Default case for other invalid inputs
        raise ValueError("matrices cannot be multiplied") from e
