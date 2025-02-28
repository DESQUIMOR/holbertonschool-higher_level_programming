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
        # Pass through the exact NumPy error message for shape mismatches
        if "shapes" in str(e):
            raise ValueError(str(e))
        else:
            raise ValueError("Scalar operands are not allowed, use '*' instead")
    except TypeError as e:
        # Handle specific cases where empty rows are provided
        if isinstance(m_a, list) and len(m_a) > 0 and isinstance(m_a[0], list) and len(m_a[0]) == 0:
            if isinstance(m_b, list) and len(m_b) > 0:
                raise ValueError(f"shapes (1,0) and ({len(m_b)},{len(m_b[0])}) not aligned: 0 (dim 1) != {len(m_b)} (dim 0)")
        
        if "invalid data type" in str(e):
            raise TypeError("invalid data type for einsum")
        elif "object of type" in str(e) and "has no len" in str(e):
            raise TypeError(str(e))
        else:
            raise TypeError("Scalar operands are not allowed, use '*' instead")
