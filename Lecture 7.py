# -*- coding: utf-8 -*-
"""
Script 6 Introduction to Python (Student version)
Created on Fri Jan  3 04:21:26 2025
@author: HSS
"""
import numpy as np

# ===========================================================================
# 6.1 N-Dimensional Numpy Array
# ===========================================================================
#
# An N-dimensional numpy array is a data structure provided by Numpy. It has the
# following properties:
#   (i) Homogeneous data type,
#   (ii) Fixed Size,
#   (iii) Ordered Collection,
#   (iv) Mutable.
#
# 6.1.1) 1-Dimensional Numpy Arrays
#
# Concept: A list of data points.
#
# Creation  : A list + np.array()

# (i) Some Examples

# Example 6.1: Creating a 1-D numpy array.
[1,2,3,4]
x_1 = np.array([1,2,3,4])
print(x_1)

# Geometric Interpretation: a sequence of numbers
#
# Useful Methods: ndim, size, dtype, shape
list_1 = [1,2,3,4]
x_1 = np.array(list_1)
print('NNumber of dimensions:',x_1.ndim)
print('Number of elements:',x_1.size)
print('NumbeData type:',x_1.dtype)
print('Shape:',x_1.shape) #จำนวนสมาชิก

# Example 6.2: Inspecting a 2-D numpy array.
list_2 = ["1", "2", "3", "4"]
x_2 = np.array(list_2)
print(x_2)
print("Number of dimensions:", x_2.ndim)
print("Number of elements:", x_2.size)
print("Data type:", x_2.dtype)
print("Shape:", x_2.shape)
# Example 6.3: A 1-D numpy array of strings

# Example 6.4: A 1-D numpy array of floating numbers
x_4 = np.array([1,2.0,'3'])
print(x_4)
print("Data type:", x_4.dtype)
# (ii) Some Key Insights
#
# (ii-a) Type Coersion/ Type Promotion

# (ii-b) Ordered & Mutable Objects

# (ii-c) Slicing

# (ii-d) no distinction b/w rows and columns

# ----------------------------------------------------------------------------
# 6.1.2) 2-Dimensional Numpy Arrays
#
# Concept: A list of lists (of data points).
#
# Creation  : A list of lists + np.array()

# (i) Some Examples

# Example 6.5: Creating a 2-D numpy array of integers.

# Geometric Interpretation: a matrix of numbers

# Example 6.6: A 2-D numpy array as a row vector.

# Example 6.7: A 2-D numpy array as a column vector.

# (ii) Indexing (Ordered Collection)

# Example 6.8: Indexing a 2-D numpy array.

# (iii) Mutability

# ----------------------------------------------------------------------------
# 6.1.3) 3-Dimensional Numpy Arrays
#

# Impression: A list of lists of lists.
#
# Creation  : A list of lists of lists + np.array()

# (i) An Example
#
# Example 6.9: A 3-D numpy array of integers

# Geometric Interpretation: a list of matrices; slices of matrices.

# (ii) Indexing

# (iii) Generalization
# The idea of numpy arrays extends to N-dimensions. While these can be 
# visualized as arrays of arrays, geometric interpretation becomes limited 
# beyond 3 dimensions.
#
# ============================================================================
# 6.2 Useful Numpy Arrays Creation Functions
# ============================================================================

# 6.2.1) For 1-D Arrays

# (i) linspace()
#
# Syntax 6.1 ----------------------------------------------------------------
# numpy.linspace(start, stop, num=50, endpoint = True)
# ---------------------------------------------------------------------------

# Example 6.10:
# np.linspace(1,5)  # uncomment to see the result

# Example 6.11:
# np.linspace(1,5,5)  # uncomment to see the result

# Example 6.12:
# np.linspace(1,5,5,False)  # uncomment to see the result

# (ii) arange()
#
# Syntax 6.2 ----------------------------------------------------------------
# numpy.arange(start, stop, step=1)
# ---------------------------------------------------------------------------

# Example 6.13:
# np.arange(2,8)  # uncomment to see the result

# Example 6.14:
# np.linspace(2,8,2)  # uncomment to see the result

# (iii) random.rand() & random.seed()
#
# Syntax 6.3 ----------------------------------------------------------------
# numpy.random.rand(n)
# ---------------------------------------------------------------------------

# Example 6.15:

# Syntax 6.4 ----------------------------------------------------------------
# numpy.random.seed(seed_value)
# ---------------------------------------------------------------------------

# Example 6.16:

# 6.2.2) For 2-D Arrays

# (i) eye()
#
# Syntax 6.4 ----------------------------------------------------------------
# numpy.eye(N)
# ---------------------------------------------------------------------------

# Example 6.17:

# (ii) arange() & reshape()
#
# Syntax 6.5 ----------------------------------------------------------------
# numpy.reshape(a, newshape)
# ---------------------------------------------------------------------------

# Example 6.18:

# Alternatively,

# Example 6.19:

# 6.2.3) For N-D Arrays

# (i) ones()
#
# Syntax 6.6 ----------------------------------------------------------------
# numpy.ones(shape)
# ---------------------------------------------------------------------------

# Example 6.20:

# (ii) zeros()
#
# Syntax 6.7 ----------------------------------------------------------------
# numpy.zeros(shape)
# ---------------------------------------------------------------------------

# Example 6.21:

    

# ===========================================================================
# 6.3 Broadcasting Operations
# ===========================================================================

# Given two scalars, say x and y, operators such as
#
#                         +,     -,    *,     /
#
# perform standard algebraic calculations
x,y = 2,4
x+y
x-y
x*y
x/y

# What will happen when x or y (or both) are numpy arrays?

# Case 1: x is a scalar and y is a numpy array
# Example 6.21:


# Case 2: x and y are numpy arrays with the same shape
# Example 6.22:

# Case 3: x and y are numpy arrays with different shapes
#
# ----------> beyond the scope of this class !!!

# ===========================================================================
# 6.4 Vectorization
# ===========================================================================

# Why use numpy for arrays, instead of list?

# ======================== END ==============================================
