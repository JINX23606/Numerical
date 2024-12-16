"""
Created on Mon Dec 16 16:08:42 2024

@author: OCS
"""
#                           Order Mutable
#Lists                        y      y /
#Tuples                       y      n /
#(Regular) Dictionaries       n      y /
#Sets                         n      y
#Frozensets                   n      n
#Ordered Dictionary           y      y

#List
my_list = [20,10,30,40,50]
print(my_list)
type(my_list)
len(my_list)

l_2 = ['a','b']
l_3 = [1,1.5,'b',1<2]
l_4 = [l_2,l_3]
l_5 = []

#(ii) index
print(my_list[1])
print(my_list[0])
print(my_list[4])
#my_list[5] undefinded
print(my_list[-1])
print(my_list[-2])

#(iii) Mutability
m2 = [1]
m2=[0]
m2[0] = 2
print(m2)

m3 = [3]
m3
#Not Mutation
m3 = [4]
m3
#(iv) Some Methods
my_list = [20,10,30,40,50]
#reverse
my_list.reverse()
print(my_list)

#Sorting
my_list.sort()
print(my_list)

#Append
my_list.append([70,80])
my_list.remove([70,80])
my_list.extend([70,80])
print(my_list)

#(v) lists & Booleans
# all any in
my_bool_1 = [True,True]
my_bool_2 = [True,False]
my_bool_3 = [False,False]
my_bool_4 = []

all(my_bool_1)
all(my_bool_2)
all(my_bool_3)
all(my_bool_4)

any(my_bool_1)
any(my_bool_2)
any(my_bool_3)
any(my_bool_4)

# in
my_num = [1,2,3,4]
print(3 in my_num)
print(5 in my_num)

#(vi) range() & list()
# I want to get [1,2,3,4,...,100] 
r = range(1,101)
r_list = list(r)
print(r_list)

#range (a,N,d) -> squence of int
#
# Parmerters        meaning              required?          default
#     a         start(inclusive)             x                 0
#     N         end(exclusive)               /                 -
#     d              step                    x                 1

r = range(2,10,2)
r_list = list(r)
print(r_list)

r = range(5)    # N = 5 (0,5,1)
print(list(r))

r = range(3,7) # N = 7 a = 3 (3,7,1) 
print(list(r))

r = range(7,3) # N = 3 a = 7 (7,3,1)
print(list(r))

r = range(10,0,-2)
print(list(r))

x = ['c','b','a']
x.sort()
print(x)

#Turples
t_1 = (1,2,3,4,5)
print(t_1)
type(t_1)
len(t_1)

t_2 = ('a','b')
t_3 = (True,1.5)
t_4 = (t_2,t_3)
t_5 = ()

# (iv) Indexing (Ordered)
t_1[0]
t_1[-1]

#Dictionary
x = {
     'a':1,
     'b':3}

