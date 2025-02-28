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
        # Convert input lists to numpy arrays and perform multiplication
        result = np.matmul(m_a, m_b)
        return result
    except ValueError as e:
        raise ValueError("matrices cannot be multiplied") from e
    except Exception:
        raise ValueError("matrices contain invalid data")
