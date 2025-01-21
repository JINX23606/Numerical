# -*- coding: utf-8 -*-
"""
Lecture 1 Basic Python
Created on Mon Nov 25 17:20:50 2024

@author: OCS
"""
# 1.1 Atomic Data type
#
#----------int,float,str,bool
# (i) int
-3
3
500
type(3)
# (ii) float
2.5
type(2.5)
# (iii) str
'Ink'
# (iv) bool
1 < 2
type(2<5)
True
1 == 2

# 1.2 Var
#
# (i) var = data
x = 500
x
y = x
a = 'b'
print(a) 
# (ii) update
a = 500
a += 50
print(a)

# (iii) multiple assignment
x,y,z = 3,5,'mom'
print(x,y,z)

    
# (iv) keywords
alpha = 0.3 
print(alpha)

help("keywords")
