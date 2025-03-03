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
        TypeError: If invalid data types are used
    """
    # Check for empty rows in the first matrix
    if isinstance(m_a, list) and len(m_a) == 1 and isinstance(m_a[0], list) and len(m_a[0]) == 0:
        if isinstance(m_b, list) and len(m_b) > 0 and isinstance(m_b[0], list) and len(m_b[0]) > 0:
            raise ValueError(f"shapes (1,0) and ({len(m_b)},{len(m_b[0])}) not aligned: 0 (dim 1) != {len(m_b)} (dim 0)")
    
    # Check for empty rows in the second matrix
    if isinstance(m_b, list) and len(m_b) == 1 and isinstance(m_b[0], list) and len(m_b[0]) == 0:
        if isinstance(m_a, list) and len(m_a) > 0 and isinstance(m_a[0], list) and len(m_a[0]) > 0:
            raise ValueError(f"shapes ({len(m_a)},{len(m_a[0])}) and (1,0) not aligned: {len(m_a[0])} (dim 1) != 1 (dim 0)")
    
    # Check for non-numeric elements
    if isinstance(m_a, list) and all(isinstance(row, list) for row in m_a):
        for row in m_a:
            if any(not isinstance(item, (int, float)) for item in row):
                raise TypeError("invalid data type for einsum")
                
    if isinstance(m_b, list) and all(isinstance(row, list) for row in m_b):
        for row in m_b:
            if any(not isinstance(item, (int, float)) for item in row):
                raise TypeError("invalid data type for einsum")
    
    # Check for irregular shaped matrices (not all rows have same number of columns)
    if isinstance(m_a, list) and all(isinstance(row, list) for row in m_a) and len(m_a) > 0:
        row_lengths = [len(row) for row in m_a]
        if len(set(row_lengths)) > 1:
            raise ValueError("setting an array element with a sequence.")
            
    if isinstance(m_b, list) and all(isinstance(row, list) for row in m_b) and len(m_b) > 0:
        row_lengths = [len(row) for row in m_b]
        if len(set(row_lengths)) > 1:
            raise ValueError("setting an array element with a sequence.")
    
    # Check for matrices that cannot be multiplied because of shape mismatch
    if (isinstance(m_a, list) and isinstance(m_b, list) and
        len(m_a) > 0 and len(m_b) > 0 and
        all(isinstance(row, list) for row in m_a) and all(isinstance(row, list) for row in m_b)):
        
        # Get shapes
        rows_a = len(m_a)
        cols_a = len(m_a[0]) if rows_a > 0 and len(m_a[0]) > 0 else 0
        rows_b = len(m_b)
        cols_b = len(m_b[0]) if rows_b > 0 and len(m_b[0]) > 0 else 0
        
        # Check if matrices can be multiplied
        if cols_a != rows_b:
            raise ValueError(f"shapes ({rows_a},{cols_a}) and ({rows_b},{cols_b}) not aligned: {cols_a} (dim 1) != {rows_b} (dim 0)")
    
    # If not capturing the special cases, proceed with normal matmul
    try:
        return np.matmul(m_a, m_b)
    except ValueError as e:
        if "shapes" in str(e):
            raise ValueError(str(e))
        elif "setting an array element with a sequence" in str(e):
            raise ValueError("setting an array element with a sequence.")
        else:
            raise ValueError("Scalar operands are not allowed, use '*' instead")
    except TypeError:
        raise TypeError("Scalar operands are not allowed, use '*' instead")
