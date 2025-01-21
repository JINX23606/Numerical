# -*- coding: utf-8 -*-
"""
Script 8: Applied Linear Algebra (Student Version)
Created on Sat Jan  4 06:13:27 2025
@author: User
"""

import numpy as np

# ============================================================================
# 8.1 Using 2-Dimensional NumPy Arrays as Matrices
# ============================================================================
# Matrices in NumPy are represented as 2-dimensional arrays. Below are examples:

# Example 8.1: Matrix initialization
A   = np.array([[1, 3], [1, 2]])         # A_2x2, a square matrix
B   = np.array([[1, 2, 3], [1, 2, 4]])  # B_2x3, a non-square matrix
I_2 = np.eye(2)                          # 2x2 identity matrix
a   = np.array([[1, 2, 3]])              # Row vector
b   = np.array([[9], [8]])               # Column vector

print("Matrix A:\n", A)
print("Matrix B:\n", B)
print("Matrix I_2:\n", I_2)
print("Matrix a:\n", a)
print("Matrix b:\n", b)

# ============================================================================
# 8.2 Elementary Operations
# ============================================================================

# 8.2.1 Scalar Multiplication
# Example 8.2: Multiply each element of a matrix by a scalar
C = 2 * A
print("\n2 * A:\n", C)

# 8.2.2 Matrix Addition & Subtraction
# Matrices must have the same shape for element-wise operations
# Example 8.3: Matrix addition & subtraction
print("\nA + C:\n", A + C)
print("A - C:\n", A - C)

# Example 8.4 (Optional): Handle incompatible shapes
D = np.array([[1, 2, 3], [1, 1, 1]])
E = np.array([[1, 2], [1, 5]])
if D.shape == E.shape:
    print("\nD + E:\n", D + E)
    print("D - E:\n", D - E)
else:
    print("Matrix addition & subtraction are undefined for matrices of different shapes.")

# 8.2.3 Matrix Multiplication
# Conditions: For A_mxp and B_qxn, p must equal q for multiplication
# Example 8.5: Matrix multiplication
G = np.array([[1, 2, 3], [1, 2, 4]])
H = np.array([[2, 3], [2, 4], [2, 5]])
print("np.dot(G,H): \n" , np.dot(G, H))
print("np.matmul(G,H): \n" , np.matmul(G, H))
print("G @ H: \n" , G @ H)


# Example 8.6 (Optional): Check compatibility before multiplication
if G.shape[1] == H.shape[0]:
    P = G @ H
    print("\nMatrix Product (P):\n", P)
else:
    print("\nMatrix Multiplication is undefined for incompatible shapes.")

# 8.2.4 Other Useful Operations
# Example 8.7: Transpose of a matrix
PT_1 = P.T
PT_2 = P.transpose()
print("\nTranspose of P using .T:\n", PT_1)
print("Transpose of P using .transpose():\n", PT_2)

# Example 8.8: Trace of a matrix
tr_P = np.trace(P)
print("\nTrace of P:\n", tr_P)

# ============================================================================
# 8.3 Determinant & Inversion
# ============================================================================

# 8.3.1 Determinant
# Example 8.9: Calculate determinant
A = np.array([[1, 3], [1, 2]])
det_A = np.linalg.det(A)
print("\nDeterminant of A:\n", det_A)

# 8.3.2 Matrix Inversion
# Example 8.10: Calculate inverse
if det_A != 0:
    inv_A = np.linalg.inv(A)
    print("\nInverse of A:\n", inv_A)
else:
    print("\nA is singular and not invertible.")

# ============================ END ==========================================