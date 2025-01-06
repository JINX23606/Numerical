# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 16:18:50 2025

@author: OCS
"""
#2 Dimention list of list
import numpy as np
one_dim = np.array([1,2,3]) #Sequence
two_dim = np.array([[1,2,3],[4,5,6]]) 
#Matrix 2 Row 3 Column
r_0 = [1,2,3]
r_1 = [4,5,6]
a = np.array([r_0,r_1])
print('Matrix A\n',a)
print(f'Dimention {a.ndim}')
print(a.size) #members
print(a.dtype) #int32
print(a.shape) #row #column (2,3)
#[(0,0)(0,1)(0,2)
# (1,0)(1,1)(1,2)
# (2,0)(2,1)(2,2)]
#Index
print(a[0])#row 0
print(a[0,:])#row 0 all
print(a[:,0])
print(a[:,:])
#Mutability can't change size
a[0,0] = 10
print(a)
#3 Dimantion list of list of list
three_dim = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(three_dim[1,0,0])
print('Dimention :',three_dim.ndim)
print('Type :',three_dim.dtype)
print('Size :',three_dim.size)
print('Shape :',three_dim.shape)

x = np.linspace(1,5,num=5,endpoint=False)
print(x)
y = np.arange(1,50,1 )
print(y)
#Random
np.random.seed(42)
arr1 = np.random.rand(5)
print(arr1)

x = np.eye(5)
print(x)

u = np.arange(9)
v = np.reshape(u,(3,3))
print(v)
#Boardcasting Operation
a = np.array([[5,5,5],[1,2,3]])
b = np.array([[1,1,1]])
print(a+2)

g = np.array([[1,2,3],[1,2,4]])
h = np.array([[2,3],[2,4],[2,5]])
print(np.dot(g, h))
print(np.matmul(g, h))
print(g@h)
#Transpose
print(g.T)
#Trace
#print(np.trace(g))
#Determinant
#print(np.linalg.det(g))
#Inverse
#print(np.linalg.inv(g))