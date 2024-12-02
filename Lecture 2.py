a = 'sarah'
print(a)
len(a)
b =[1,2,3,4,5]
sum(b)

#function
def mul(a,b):    
    return a*b
z = mul(5,2)
print(z)

# (1.4) object and methods
#   data and 
#   methods that operate on the data
y = 'demand'
y.capitalize()
y.count('')

#(1.5) modules packages
# (i) A module is a file containing a collection of fns
# (ii) A package is a derectiory organizing
#   modules
import math_operations as mo
result = mo.add(2, 5)
print(result)
lob = mo.subtract(7, 4)
print(lob)
rob = mo.subtract(8, 7)
print(rob)

# 3rd party
#modules: math , datetime , matplotlib.pyplot
#packages: numpy,pandas

import math as mt
sqrt = mt.sqrt(4)
print(sqrt)
print(mt.pi)

import matplotlib.pyplot as plt
names = ['A','B','C']
values= [5,8,3]
my_bar = plt.show(names,values)

import numpy as np
np.mean(values)
