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

# (ii) Indexing
t_1 = (10, 20, 30, 40)
print(t_1[0])  # First element
print(t_1[2])  # Third element
print(t_1[-1]) # Last element
# print(t_1[4])  # Uncomment to see IndexError

# (iii) Immutability
# We argue that tuples are immutable. To illustrate this, consider:
t_1 = (1, 2, 3)
#t_1[0] = 10  # Uncomment to see TypeError
#t_1.append(4) # Uncomment to see TypeError

# (iv) List vs Tuple: Which to use?
#
# Use a tuple when you want an immutable sequence.
# Use a list when you need a mutable sequence.
#
# Example 6: Chinese Economy
#  Year    GDP (trillions)   Population (in billions)
#  2013      9.607              -
#  2014     10.48               -
#  2015     11.06              1.371

# cross-sectional data for 2015  ---> tuple is prefered (why?)
CHN_2015 = ('China', 2015, 11.06, 1.37)
print(CHN_2015)
# We do not expect the values to change for this particular record. A tuple is 
# ideal here because it is immutable. This ensures that once we store the 
# information for China in 2015, we cannot accidentally change any of these 
# values, preserving the integrity of the data.


# Time-Series for GDP   ---> list is prefered (why?)
CHN_GDP = [9.607, 10.48, 11.06]
print(CHN_GDP)
# A list is more suitable for this scenario because we expect to update the 
# data over time.


# (v)  zip()
#      We can use zip() with list() to generate a list of tuples. 
# 
# In detail, the zip() function in Python is used to pair elements from two or 
# more iterables (e.g., lists, tuples) together into tuples. It stops when the 
# shortest input iterable is exhausted.
countries = ['China', 'India', 'USA']
gdp_values = [11.06, 2.87, 21.43]
z = zip(countries, gdp_values)
print(z)                                # a generator
# In the previous line, z is a zip object, which is a generator. It doesn't 
# contain the actual pairs yet. It will generate them only when you iterate 
# over it.
country_gdp = list(z)
print(country_gdp)
# We convert the zip object z into a list, which forces it to consume the 
# generator and produce the list of tuples.
#
# After this, the generator is exhausted, meaning it can't be reused.
m = list(z)
print(m)   # output: []

# (vi) enumerate()
#      We can use enumerate() with list() to generate a list of tuples.
#
# In detail, the enumerate() function in Python adds a counter to an iterable 
# and returns it as an enumerate object, which can be converted into a list of 
# tuples.
countries = ['China', 'India', 'USA']
e = enumerate(countries)
print(e)
indexed_countries = list(e)
print(indexed_countries)
# Similarly,
o = list(e)
print(o)
# Generators in Python, like the ones returned by zip() and enumerate(), can 
# only be iterated once. After they are consumed, they are exhausted and cannot 
# be reused.

# (vi) slicing
# Let x be an iterable (list or tuple). Then, slicing 
# x[start:end:step] 
# allows us to take a portion of x by selecting elements based on 3 parameters:
#
# Parameters  meaning                              required  default
#  start    the index used as a start (inclusive)    no      0        if step>0
#                                                           -1        if step<0
#  end      the index to stop (exclusive)            no      len(x)   if step>0
#                                                           -len(x)-1 if step<0
#  step     the increment/decrement between indices  no      1
#
# Examples
a = [1, 2, 3, 4, 5, 6, 7, 8]
print(a[::])
print(a[:5])
print(a[2:])
print(a[2:5])
print(a[2:7:2])

b = (1,2,3,4,5,6,7,8)
print(b[:5])#1,2,3,4,5
print(b[2:])#3,4,5,6,7,8
print(b[2:5])#3,4,5
print(b[2:7:2])

c = [1, 2, 3, 4, 5, 6]
print(c[2:-1])

d = [1, 2, 3, 4, 5, 6]
print(d[::-1])

#===========================================================================
# 3.3 Regular Dictionaries
#===========================================================================
#
# (i) Structure
#
# A dictionary is structured as:
#
#       {key_1: value_1, key_2: value_2, ..., key_n: value_n}
#
# Keys must be immutable objects (e.g., strings, numbers, or tuples),
# while values can be any type of Python object.

# Example 1: A simple dictionary
my_dict_1 = {  'a': 1, 
               'b': 2,
               'c': 3 }
print("Dictionary 1:", my_dict_1)
print("Type of my_dict_1:", type(my_dict_1))
print("Length of my_dict_1:", len(my_dict_1))

# Example 2: A dictionary with multiline formatting
one_usd_equals = {
               'Baht': 34.65, 
               'Ringgit': 4.61, 
               'Dong': 24245.00,
               'Singapore Dollar': 1.32
                }
print("Dictionary 2:", one_usd_equals)

# Example 3: integers as keys and strings as values
genderdict = {0:'male', 1:'female'}

# Example 4: Caution
caution = {
            (0,1,2): 'tuples can be keys',
            1: 'integers can be keys',
            (1,2,3): 'lists cannot be keys'}
print(caution)

# (ii) Accessing Elements
# Regular dictionaries are not ordered, so use keys instead of indices to 
# access elements.

print("Value associated with key 'a':", my_dict_1['a'])
print("Value associated with key 'a':", my_dict_1['d'])   # error

# Use the `.get()` method to safely access elements and avoid KeyError.
# If the key doesn't exist, `.get()` returns None or a specified default value.
print("Using .get() with an existing key:", my_dict_1.get('b'))
print("Using .get() with a non-existing key:", my_dict_1.get('d', "Not Found"))
print("Using .get() with a non-existing key:", my_dict_1.get('d'))

# (iii) Updating Dictionary Items
# Dictionaries are mutable, so you can add, update, or delete key-value pairs.
my_dict_1['d'] = 4  # Adding a new key-value pair
print("After adding 'd':", my_dict_1)

my_dict_1['a'] = 10  # Updating the value of an existing key
print("After updating 'a':", my_dict_1)

# (iv) Some Useful Methods
# .keys()   - Returns all keys in the dictionary as a view object.
# .values() - Returns all values in the dictionary as a view object.
# .items()  - Returns all key-value pairs as tuples in a view object.
# .pop(key) - Removes a key-value pair and returns the value.
# .clear()  - Removes all key-value pairs from the dictionary.
# .update() - Updates the dictionary with key-value pairs from another 
#             dictionary or iterable of key-value pairs.

print("Keys in my_dict_1:", my_dict_1.keys())
print(type(my_dict_1.keys()))
print('List of the keys:',list(my_dict_1.keys()))


print("Values in my_dict_1:", my_dict_1.values())
type(my_dict_1.values())
print('List of the values:',list(my_dict_1.values()))


print("Key-value pairs in my_dict_1:", my_dict_1.items())
type(my_dict_1.items())
print('List of the key-value pairs:',list(my_dict_1.items()))

# Using the .update() method
update_dict = {'e': 5, 'f': 6}
my_dict_1.update(update_dict)
print("After updating with another dictionary:", my_dict_1)

# Removing a key-value pair using .pop()
removed_value = my_dict_1.pop('b')
print("Value removed:", removed_value)
print("Dictionary after removing 'b':", my_dict_1)

# Clearing all items
my_dict_1.clear()
print("Dictionary after clearing all items:", my_dict_1)
type(my_dict_1)

#============================================================================
# 3.4 Sets
#============================================================================
# A set in Python is an unordered collection of unique items. Sets are mutable, 
# meaning you can add or remove elements. They are commonly used for operations 
# like unions, intersections, and difference between collections.

# Create a set
my_set = {1, 2, 3, 4}
print(my_set)  # Output: {1, 2, 3, 4}

# Add and remove elements
my_set.add(5)
my_set.remove(2)
print(my_set)  # Output: {1, 3, 4, 5}

# Set operations
set_a = {1, 2, 3}
set_b = {3, 4, 5}
print(set_a | set_b)  # Union: {1, 2, 3, 4, 5}
print(set_a & set_b)  # Intersection: {3}
print(set_a - set_b)  # Difference: {1, 2}

#============================================================================
# 3.5 Ordered Dictionaries
#============================================================================
# An ordered dictionary (OrderedDict) is a dictionary subclass that remembers 
# the order in which keys were first inserted. In modern Python (version 3.7+), 
# the built-in dict itself preserves insertion order, but OrderedDict still 
# provides additional methods for reordering.
from collections import OrderedDict

# Create an ordered dictionary
ordered_dict = OrderedDict()
ordered_dict['a'] = 1
ordered_dict['b'] = 2
ordered_dict['c'] = 3

print(ordered_dict)  # Output: OrderedDict([('a', 1), ('b', 2), ('c', 3)])

# Move an item to the end
ordered_dict.move_to_end('b')
print(ordered_dict)  # Output: OrderedDict([('a', 1), ('c', 3), ('b', 2)])


#============================================================================
# 3.6 Frozensets
#============================================================================
# A frozenset is an immutable version of a set. Unlike a regular set, you 
# cannot add or remove elements from a frozenset after it's created. They are 
# useful when you need a hashable collection of items.
# Create a frozenset
my_frozenset = frozenset([1, 2, 3, 4])
print(my_frozenset)  # Output: frozenset({1, 2, 3, 4})

# Use frozensets in a dictionary
my_dict = {my_frozenset: "immutable set"}
print(my_dict)  # Output: {frozenset({1, 2, 3, 4}): 'immutable set'}

# Frozenset operations (like regular sets)
another_frozenset = frozenset([3, 4, 5])
print(my_frozenset | another_frozenset)  # Union: frozenset({1, 2, 3, 4, 5})

#my_frozenset.add(5) # Uncomment to see AttributeError

#=============================================================================