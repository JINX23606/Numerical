#Exercise 7
import math as m
x,y = 1.05,1.02
result = m.log(x)-m.log(y)
print(f'Result :{result:.2f}')
#----------------------------

#Exercise 8
x = "What's wrong with this string" 
print(x)

#----------------------------

#Exercise 9
x,y = 'Hello','World'
print(x+' '+y)

#----------------------------

#Exercise 10
test = 'abc'
new_word = test.replace('c','d')
print(new_word)

#----------------------------

#Exercise 15
x = 2
y = 2
z = 4
# Statement 1
x > z #False
# Statement 1
x == y #True
# Statement 3
(x < y) and (x > y) #False
# Statement 4
(x < y) or (x > y) #False
# Statement 5
(x <= y) and (x >= y) #True
# Statement 6
True and ((x < z) or (x < y)) #True

#----------------------------

#Exercise 16
all([True, True, True]) #True
all([False, True, False]) #False
all([False, False, False]) #False
any([True, True, True]) #True
any([False, True, False]) #True
any([False, False, False]) #False