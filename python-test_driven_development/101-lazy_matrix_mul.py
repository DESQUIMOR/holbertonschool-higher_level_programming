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
    # Check for empty rows in the first matrix
    if isinstance(m_a, list) and len(m_a) == 1 and isinstance(m_a[0], list) and len(m_a[0]) == 0:
        if isinstance(m_b, list) and len(m_b) > 0 and isinstance(m_b[0], list) and len(m_b[0]) > 0:
            raise ValueError(f"shapes (1,0) and ({len(m_b)},{len(m_b[0])}) not aligned: 0 (dim 1) != {len(m_b)} (dim 0)")
    
    # Check for empty rows in the second matrix
    if isinstance(m_b, list) and len(m_b) == 1 and isinstance(m_b[0], list) and len(m_b[0]) == 0:
        if isinstance(m_a, list) and len(m_a) > 0 and isinstance(m_a[0], list) and len(m_a[0]) > 0:
            raise ValueError(f"shapes ({len(m_a)},{len(m_a[0])}) and (1,0) not aligned: {len(m_a[0])} (dim 1) != 1 (dim 0)")
    
    # If not capturing the special empty row cases, proceed with normal matmul
    try:
        return np.matmul(m_a, m_b)
    except ValueError as e:
        if "shapes" in str(e):
            raise ValueError(str(e))
        else:
            raise ValueError("Scalar operands are not allowed, use '*' instead")
    except TypeError:
        raise TypeError("Scalar operands are not allowed, use '*' instead")
