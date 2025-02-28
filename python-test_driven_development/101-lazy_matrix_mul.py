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
        ValueError: If matrices cannot be multiplied
    """
    try:
        result = np.matmul(m_a, m_b)
        return result
    except ValueError as e:
        if "shapes" in str(e):
            raise ValueError(str(e))
        else:
            raise ValueError("Scalar operands are not allowed, use '*' instead")
    except TypeError as e:
        if "invalid data type" in str(e):
            raise TypeError("invalid data type for einsum")
        elif "object of type" in str(e) and "has no len" in str(e):
            raise TypeError(str(e))
        else:
            raise TypeError("Scalar operands are not allowed, use '*' instead")
