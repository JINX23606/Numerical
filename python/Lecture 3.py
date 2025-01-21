#integer
print(type(10))
#floating point number
print(type(10.0))
# (i) math_operatoin
x = 6
y = 3
print('x+y :',x+y)
print('x-y :',x-y)
print('x*y :',x-y)
print('x/y :',x/y)
print('x**y :',x**y)
# (ii) Order of Operation
# PEMDAS -> (). ** , * , / , + , -
a = 2+5**2
print(a)

#string
#(i) Creation
string1 = 'Hello'
string2 = 'World'
string3 = 'This is a string with space'
#(ii) Basic Operations
# + *
greeting = string1+' '+string3
repeater = 'Hi!'*3
x,y = '1','2'
x+y
x*5
#(iii) Some method 
text = 'Pyhton Programing'
print(text.upper())
print(text.lower())
print(text.capitalize())
print(text.title())
print(text.count(''))
print(text.count('m'))
print(text.count('mm'))
print(text.replace('Programing','Is easy'))
# (iv) f-string
country = 'Vietnam'
GDP = 223.9
Year = 2017
print(f'{country} had ${GDP} Billions GDP in {Year}.')
print('{} had ${} Billions GDP in {}.'.format(country,GDP,Year))
# (v) formatting numbers
#
# Decimal Places
print(f'GDP :{GDP:.2f}')
# Comma
population = 6461315684564
print(f'Population =: {population:,}')

#Percentage
growth_rate = 0.025
print(f'Growth : {growth_rate:.1%}')

# Boolean
#(i) Direct
a = True
b = False
type(a)
type(b)

#(ii) Using Logical Operators [and,or,not]
a and b
a or b
not a
not a or b
(not a or b) and (not b or a )

#(iii) Comparison Operators
1 > 2
1 >=2
1 < 2
1 <=2
1 == 2
1 != 2